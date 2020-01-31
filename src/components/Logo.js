import React, { Component } from 'react';
import Image from './Image';
import Url from './Url';
import Local_storage from './Local_storage';

import { useQuery } from '@apollo/react-hooks';
import { gql } from 'apollo-boost';
import ErrorLink from './ErrorLink';


function Logo(props) {
    const GET_LOGO = gql`
    query get_logo($idlogo: Int!) {
        logo(idlogo: $idlogo) {
            titulo
            foto
        }
    }`;

    const variables = { variables: { idlogo: props.id }, }
    const { loading, error, data } = useQuery(GET_LOGO, variables);
    if (loading) return '...';
    if (error) return ErrorLink(error);
    console.log(data);
    return <Image image={data.foto} title={data.titulo} />;
}



class Logo2 extends Component {
    resource = 'logo';
    sub = 'portada';
    constructor(props) {
        super(props);
        this.id = props.id;
        this.size = props.size;
        this.url = Url(this.resource, this.id, this.sub, this.size);
        this.state = Local_storage.get(this.url, { foto: '', title: '' });

        this.GET_LOGO = gql`
            {
                logo
            }
            `;
    }
    componentDidMount() {
        this.get_logo();
    }


    get_logo() {
        if (this.state.foto === '') {
            fetch(this.url)
                .then(response => response.json())
                .then(data => {
                    this.setState({ foto: data.foto, title: data.titulo });
                    Local_storage.set(this.url, this.state);
                });
        }
    }

    render() {
        if (this.state.foto !== '') {
            return (
                <Image image={this.state.foto} title={this.state.title} />
            )
        } else {
            return null;
        }
    }
}

export default Logo;