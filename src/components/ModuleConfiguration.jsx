import React from 'react';
import { useQuery } from '@apollo/react-hooks';
import { gql } from 'apollo-boost';

import ErrorLink from './ErrorLink';
import LocalStorage from './LocalStorage';
import ModuleList from './ModuleList';

function ModuleConfigurationCache(props) {
    const {
        url_cache,
        idadministrador,
        module,
        tipo
    } = props;
    const GET_MODULES = gql`
    query get_module ($idadministrador:Int!,$module:String!,$tipo:Int){
        module(idadministrador:$idadministrador,module:$module){
            titulo
            estado
            hijo(tipo:$tipo){
                titulo
                orden
                permisos{
                    estado
                    menu(estado:true){
                        field
                        titulo
                    }  
                    mostrar(estado:true){
                        field
                        titulo
                        tipo
                    }
                    detalle(estado:true){
                        field
                        titulo
                        tipo
                    }
                }
            }
        }
    }`;

    const variables = { variables: { idadministrador: idadministrador, module: module, tipo: tipo }, };

    const { loading, error, data } = useQuery(GET_MODULES, variables);
    if (loading) return null;
    if (error) return ErrorLink(error);

    if(data.module===null){
        return false;
    }
    
    LocalStorage.set(url_cache, data.module);

    return data.module;
}


function ModuleConfiguration(props) {
    const url_cache = 'get_module_id_' + props.idadministrador + '_module_' + props.module + '_tipo_' + props.tipo;
    var config = LocalStorage.get(url_cache, null);
    if (config===null) {
        config= ModuleConfigurationCache(props, url_cache);
    }
    return(
        <ModuleList config={config} module={props.module} tipo={props.tipo}/>
    )
}

export default ModuleConfiguration;