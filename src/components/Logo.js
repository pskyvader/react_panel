import React, { Component } from 'react';
import Image from './Image';

const API = 'http://localhost:8080/';
class Logo extends Component {
    resource = 'logo/'
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
            const id = 2;
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