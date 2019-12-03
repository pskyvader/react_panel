import React, { Component } from 'react';
import Image from './Image';
import Url from './Url';

const API = 'http://localhost:8080';
class Logo extends Component {
    constructor(props) {
        super(props);
        this.state = {
            logo: "",
            title: ""
        };
    }
    componentDidMount() {
        this.get_logo();
    }


    get_logo() {
        if (this.state.logo === '') {
            const resource = 'logo'
            const id = 2;
            const sub = 'portada';
            const url=Url(API,resource, id, sub );
            console.log(url);
            fetch(API + this.resource + id)
                .then(response => response.json())
                .then(data => {
                    this.setState({ logo: data.foto, title: data.titulo });
                });
        }
    }

    render() {
        return (
            <Image image={this.state.logo} title={this.state.title} />
        )
    }
}
export default Logo;