function Url(...args) {
    var final_url = '';
    var k=0;
    args.forEach(e=> {
        if (k > 0) final_url += '/';
        final_url += e;
        k++;
    });
    return final_url;
}
export default Url;