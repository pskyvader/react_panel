class LocalStorage {
    // 1 day default 
    static get(key, default_value = null, expiration_time = 1) {
        var value = JSON.parse(localStorage.getItem(key));
        if (value == null) {
            this.set(key, default_value, expiration_time);
        } else {
            if (value.expiration_time < Date.now()) {
                this.set(key, default_value, expiration_time);
            } else {
                return value.data;
            }
        }

        return default_value;
    }
    static set(key, value, expiration_time = 1) {
        if (value != null) {
            expiration_time = Date.now() + expiration_time * 24 * 60 * 60 * 1000;
            localStorage.setItem(key, JSON.stringify({
                data: value,
                expiration_time: expiration_time
            }));
        }
    }

}

export default LocalStorage;