import React, { Component } from 'react';
import Image from './Image';
import Url from './Url';

class Logo extends Component {
    resource = 'logo';
    sub = 'portada';
    foto='';
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
                    this.setState({ foto: data.foto, title: data.titulo });
                });
        }
    }

    render() {
        console.log('render',this);
        return (
            <Image image={this.foto} title={this.title} />
        )
    }
}
export default Logo;