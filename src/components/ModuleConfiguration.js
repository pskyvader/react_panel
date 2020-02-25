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
        query{
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
    if (cache.length > 0) {
        return cache;
    } else {
        return ModuleConfigurationCache(props, url_cache);
    }
}

export default ModuleConfiguration;