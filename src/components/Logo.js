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
        return (
            <img src="{this.state.img}" alt="" />
        )
    }
}
export default Logo;