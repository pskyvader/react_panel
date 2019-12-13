import React, { Component } from 'react';
import Image from './Image';
import Url from './Url';

const API = process.env.REACT_APP_API_URL;
class Logo extends Component {
    resource = 'logo';
    sub = 'portada';
    logo = '';
    title = '';
    constructor(props) {
        super(props);
        this.id = props.id;
        this.size = props.size;
    }
    componentDidMount() {
        console.log('asdf',this);
        if (this.logo === '') {
            fetch(Url(API, this.resource, this.id, this.sub, this.size))
                .then(response => response.json())
                .then(data => {
                    this.logo = data.foto;
                    this.title = data.titulo;
                });
        }else{
            console.log(this.logo);
        }

    }

    render() {
        return (
            <Image image={this.logo} title={this.title} />
        )
    }
}
export default Logo;