import React, { Component } from 'react';
import Image from './Image';
import Url from './Url';

const API = 'http://localhost:8080';
class Logo extends Component {
    resource ='logo';
    sub='portada';
    constructor(props) {
        this.id=props.id;
        this.size=props.size;
        super(props);
        this.state = {
            logo: "",
            title: "",
        };
    }
    componentDidMount() {
        this.get_logo();
    }


    get_logo() {
        if (this.state.logo === '') {
            const id = this.state.id;
            const size = this.state.size;
            fetch(Url(API,resource, id, sub,size ))
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