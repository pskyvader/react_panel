import React, { Component } from 'react';
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
        const { img } = this.state;
        return (
            <img src="{img}" alt="" />
        )
    }
}
export default Logo;