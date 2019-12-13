import React, { Component } from 'react';
import Image from './Image';
import Url from './Url';
import Local_storage from './Local_storage';

class Logo extends Component {
    resource = 'logo';
    sub = 'portada';
    constructor(props) {
        super(props);
        this.id = props.id;
        this.size = props.size;
        this.url = Url(this.resource, this.id, this.sub, this.size);
        this.state = Local_storage.get(this.url, { foto: '', title: '' });
    }
    componentDidMount() {
        this.get_logo();
    }


    get_logo() {
        if (this.state.foto === '') {
            fetch(Url(this.resource, this.id, this.sub, this.size))
                .then(response => response.json())
                .then(data => {
                    this.setState({ foto: data.foto, title: data.titulo });
                    Local_storage.get(this.url, this.state);
                });
        }
    }

    render() {
        if (this.state.foto !== '') {
            return (
                <Image image={this.state.foto} title={this.state.title} />
            )
        } else {
            return null;
        }
    }
}
export default Logo;