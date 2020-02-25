import React from 'react';
import ModuleCard from '../components/ModuleCard';import {
    Grid,
} from '@material-ui/core';
import {
    useQuery
} from '@apollo/react-hooks';
import {
    gql
} from 'apollo-boost';

import ErrorLink from './ErrorLink';
import LocalStorage from './LocalStorage';

function ModuleConfigurationCache(props) {
    const {
        url_cache,
        idadministrador,
        module,
        tipo
    } = props;
    const GET_MODULES = gql `
    query get_all_module ($idadministrador:Int!,$module:String!,$tipo:Int){
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

    const variables = {
        variables: {
            idadministrador: idadministrador,
            module: module,
            tipo: tipo
        },
    };

    const {
        loading,
        error,
        data
    } = useQuery(GET_MODULES, variables);
    if (loading) return null;
    if (error) return ErrorLink(error);
    LocalStorage.set(url_cache, data.module);

    return data.module;
}


function ModuleConfiguration(props) {
    const url_cache = 'get_module_id_' + props.idadministrador + '_module_' + props.module + '_tipo_' + props.tipo;
    var cache = LocalStorage.get(url_cache, []);
    if (cache.length == 0) {
        return cache = ModuleConfigurationCache(props, url_cache);
    }

    return ( <
        Grid container direction = "row"
        justify = "flex-start"
        alignItems = "flex-start"
        spacing = {
            3
        } >
        {
            array.map((element, index) => {
                return ( <
                    Grid item xs = {
                        12
                    }
                    sm className = {
                        classes.grid
                    }
                    key = {
                        index
                    } >
                    <
                    ModuleCard / >
                    <
                    /Grid>
                )
            })
        } <
        /Grid>)
    }

    export default ModuleConfiguration;