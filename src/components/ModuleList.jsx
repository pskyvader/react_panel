import React from 'react';
import { gql } from 'apollo-boost';
import Resolve from './Resolve';
import InfiniteList from './InfiniteList';

function ModuleList(props) {
    let { module, tipo, config } = props;
    let fields = ['id'];
    if (config !== null && config !== false) {
        const module_data = config.hijo[0];
        const fields_filter = module_data.permisos.mostrar.filter(x => (x['tipo'] === 'active' || x['tipo'] === 'text'));
        fields = fields_filter.map(x => x['field']);
    }

    const vars = { first: 10, after: '' }
    if (tipo > 0) {
        vars['tipo'] = tipo;
    }
    tipo=0;

    const table_query = 'all' + module.charAt(0).toUpperCase() + module.slice(1);
    const GET_LIST = gql(`
    query get_list($first:Int!,$after:String){
        $table(first:$first,after:$after,$tipo){
            pageInfo{
                endCursor
                hasNextPage
            }
            edges{
                node{
                    $fields
                }
            }
        }
    }
    `.replace('$table', table_query).replace('$fields', fields).replace('$tipo', (tipo > 0) ? 'tipo:' + tipo : ''));

    const { items, loading, loadMore, hasNextPage, error } = Resolve({ query: GET_LIST, table: table_query, vars: vars });

    if (error) {
        return error;
    }

    if (config === null) {
        return "Loading...";
    } else if (!config) {
        return "Module " + module + " not allowed for this user";
    }else if(items.length===0){
        return "";
    }

    return (
        <InfiniteList
            items={items}
            moreItemsLoading={loading}
            loadMore={loadMore}
            hasNextPage={hasNextPage}
            height={700}
        />
    )

};

export default ModuleList;