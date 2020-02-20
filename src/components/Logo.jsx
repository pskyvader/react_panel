import React from 'react';
import Image from './Image';
import LocalStorage from './LocalStorage';

import { useQuery } from '@apollo/react-hooks';
import { gql } from 'apollo-boost';
import ErrorLink from './ErrorLink';


function Logo_cache(props, cache, url_cache) {
    const GET_LOGO = gql`
    query get_logo($idlogo: Int!,$width:String,$height:String) {
        logo(idlogo: $idlogo) {
            titulo
            foto(portada:true){
                edges{
                    node{
                        idimage
                        url(width:$width,height:$height){
                            tag
                            url
                        }
                    }
                }
            }
        }
    }`;

    const variables = { variables: { idlogo: props.id, width: props.width, height: props.height }, };
    const { loading, error, data } = useQuery(GET_LOGO, variables);
    if (loading) return <Image />;
    if (error) return ErrorLink(error);


    cache['image'] = data.logo.foto;
    cache['title'] = data.logo.titulo;
    LocalStorage.set(url_cache, cache);

    return <Image image={cache['image']} title={cache['title']} />;
}

function Logo(props) {
    const url_cache = 'get_logo_id_' + props.id + '_width_' + props.width + '_height_' + props.height;
    var cache = LocalStorage.get(url_cache, { image: '', title: '' });
    if (cache['image'] !== '' && cache['title'] !== '') {
        return <Image image={cache['image']} title={cache['title']} />;
    } else {
        return Logo_cache(props, cache, url_cache);
    }
}



export default Logo;