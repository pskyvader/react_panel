import React, { Component } from 'react';
import Image from './Image';
import Url from './Url';

const API = process.env.REACT_APP_API_URL;
class Logo extends Component {
    resource = 'logo';
    sub = 'portada';
    foto = '';
    title = '';
    constructor(props) {
        super(props);
        this.id = props.id;
        this.size = props.size;
    }
    componentDidMount() {
        if (this.foto === '') {
            fetch(Url(API, this.resource, this.id, this.sub, this.size))
                .then(response => response.json())
                .then(data => {
                    this.foto = data.foto;
                    this.title = data.titulo;
                });
        }else{
            console.log(this.foto);
        }
        this.render();
    }

    render() {
        return (
            <Image image={this.foto} title={this.title} />
        )
    }
}
export default Logo;