function Url(...args) {
    var final_url = '';
    args.forEach(
        function(e, k) {
            if (k > 0) final_url += '/';
            final_url += e;
        }
    );
    return final_url;
}
export default Url;