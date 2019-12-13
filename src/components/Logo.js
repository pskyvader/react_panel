import React, { Component } from 'react';
import Image from './Image';
import Url from './Url';

class Logo extends Component {
    resource = 'logo';
    sub = 'portada';
    foto='';
    title='';
    constructor(props) {
        super(props);
        this.id = props.id;
        this.size = props.size;
    }
    componentDidMount() {
        this.get_logo();
    }


    get_logo() {
        if (this.foto === '') {
            fetch(Url(this.resource, this.id, this.sub, this.size))
                .then(response => response.json())
                .then(data => {
                    this.foto= data.foto;
                    this.title= data.titulo;
                });
        }
    }

    render() {
        console.log('render',Logo.foto,this.title,this);
        return (
            <Image image={this.foto} title={this.title} />
        )
    }
}
export default Logo;