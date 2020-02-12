const API = process.env.REACT_APP_API_URL;

function Url(...args) {
    var final_url = args.join('/');
    return API + '/' + final_url;
}

export default Url;