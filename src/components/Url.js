function Url(...args) {
    var final_url = '';
    args.forEach(e=> {
        if (k > 0) final_url += '/';
        final_url += e;
    });
    return final_url;
}
export default Url;