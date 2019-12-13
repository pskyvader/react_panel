function Local_storage(...args) {
    var final_Local_storage = args.join('/');
    return API + '/' + final_Local_storage;
}
export default Local_storage;