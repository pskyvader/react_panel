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
                // .then(data => {
                //     this.foto=data.foto;
                //     this.title= data.titulo;
                // });
        }
    }

    render() {
        if (this.state && this.state.foto !== '') {
            console.log(this,this.state.foto,'ok');
            return (
                <Image image={this.state.foto} title={this.state.title} />
            )
        }else{
            console.log(this,this.state.foto);
            return null;
        }
    }
}
export default Logo;