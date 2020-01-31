# from wsgiref.simple_server import make_server
import passenger_wsgi


from wsgiref.simple_server import WSGIServer, WSGIRequestHandler
import multiprocessing.pool


class ThreadPoolWSGIServer(WSGIServer):
    """WSGI-compliant HTTP server.  Dispatches requests to a pool of threads."""

    def __init__(self, thread_count=None, *args, **kwargs):
        """If 'thread_count' == None, we'll use multiprocessing.cpu_count() threads."""
        WSGIServer.__init__(self, *args, **kwargs)
        self.thread_count = thread_count
        self.pool = multiprocessing.pool.ThreadPool(self.thread_count)

    # Inspired by SocketServer.ThreadingMixIn.
    def process_request_thread(self, request, client_address):
        try:
            self.finish_request(request, client_address)
            self.shutdown_request(request)
        except:
            self.handle_error(request, client_address)
            self.shutdown_request(request)

    def process_request(self, request, client_address):
        self.pool.apply_async(
            self.process_request_thread, args=(request, client_address)
        )


def make_server(host, port, app, thread_count=None, handler_class=WSGIRequestHandler):
    """Create a new WSGI server listening on `host` and `port` for `app`"""
    httpd = ThreadPoolWSGIServer(thread_count, (host, port), handler_class)
    httpd.set_app(app)
    return httpd


port = 8080
srv = make_server("", port, passenger_wsgi.application, thread_count=40)

print("En port {}... ctrl-c to quit server.".format(port))

try:
    srv.serve_forever()
except KeyboardInterrupt:
    srv.server_close()
    print("Server Stopped")
except:
    srv.server_close()
    print("Server Stopped")
