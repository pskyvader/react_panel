def parse_get(query_string):
    from cgi import parse_qs

    get = dict(parse_qs(query_string))
    if "url" in get:
        del get["url"]
    for k, u in get.items():
        if len(u) == 1:
            get[k] = u[0]
    get = format_array(get)
    get = parse_values(get)
    return get