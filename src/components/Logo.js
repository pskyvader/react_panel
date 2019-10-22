import React, { Component } from 'react';
import Image from './Image';

const API = 'http://localhost:8080/admin/';
class Logo extends Component {
    resource = 'logo/'
    constructor(props) {
        super(props);
        this.state = {
            logo: ""
        };
        this.get_logo();
    }
    componentDidMount() {
        this.get_logo();
    }

    get_logo() {
        if (this.state.logo===''){
            const id=2;
            fetch(API + this.resource+id)
            .then(response => response.json())
            .then(data => {
                this.setState({ logo: data.foto ,title:data.titulo})
            });
        }
    }

    render() {
        return (
            <Image image="{this.state.logo}" alt="{this.state.title}"/>
        )
    }
}
export default Logo;