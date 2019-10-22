import React, { Component } from 'react';

const API = 'http://localhost:8080/admin/';
class Logo extends Component {
    resource = 'logo'
    constructor(props) {
        super(props);
        this.state = {
          data: null,
        };
    }
    componentDidMount() {
        fetch(API + this.resource)
            .then(response => response.json())
            .then(data => this.setState({ img: data.img }));
    }

    render() {
        console.log(this.state);
        return (
            <img src="{this.state}" alt="" />
        )
    }
}
export default Logo;