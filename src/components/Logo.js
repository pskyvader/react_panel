import React, { Component } from 'react';
import Image from './Image';
import Url from './Url';

class Logo extends Component {
    resource = 'logo';
    sub = 'portada';
    constructor(props) {
        super(props);
        this.id = props.id;
        this.size = props.size;
        this.state = {
            foto: "",
            title: "",
        };
    }
    componentDidMount() {
        this.get_logo();
    }


    get_logo() {
        console.log('asdf');
        if (this.state.foto === '') {
            fetch(Url(this.resource, this.id, this.sub, this.size))
                .then(response => response.json())
                .then(data => {
                    this.setState({ foto: data.foto, title: data.titulo });
                });
        }
    }

    render() {
        return (
            <Image image={this.state.foto} title={this.state.title} />
        )
    }
}
export default Logo;