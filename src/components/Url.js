function Url(...args) {
    var final_url = args.join('/');
    return final_url;
}
export default Url;