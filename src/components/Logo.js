import React, { Component } from 'react';
import Image from './Image';
import Url from './Url';

class Logo extends Component {
    resource = 'logo';
    sub = 'portada';
    state={foto:'',title:''};
    constructor(props) {
        super(props);
        this.id = props.id;
        this.size = props.size;
    }
    componentDidMount() {
        this.get_logo();
    }


    get_logo() {
        if (this.state.foto === '') {
            fetch(Url(this.resource, this.id, this.sub, this.size))
                .then(response => response.json())
                .then(data => {
                    this.setState({ foto: data.foto, title: data.titulo });
                });
        }
    }

    render() {
        console.log('render');
        if (this.state.foto !== '') {
            return (
                <Image image={this.state.foto} title={this.state.title} />
            )
        }else{
            return null;
        }
    }
}
export default Logo;