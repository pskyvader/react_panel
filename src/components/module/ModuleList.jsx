import React from 'react';
import { gql } from 'apollo-boost';
import Resolve from '../Resolve';
import InfiniteList from './InfiniteList';



const formatField=(field)=>{
    field=field.split('_');
    let field2=field.map((y,i)=> (i>0)? y.charAt(0).toUpperCase() + y.slice(1):y);
    let field3=field2.join("");
    return field3; 
}


const action_list=['action','delete'];
const action_names=['url_detalle','urlDetalle'];

function ModuleList(props) {
    let { module, tipo, config } = props;
    let config_mostrar=null;
    let fields = ['id'];
    if (config !== null && config !== false) {
        const module_data = config.hijo[0];
        console.log(module_data.permisos.mostrar);
        const fields_filter = module_data.permisos.mostrar.filter(x =>(!action_list.includes(x['tipo']) && !action_names.includes(x['field']))  );
        // fields = fields_filter.map(x => formatField(x['field']));
        fields = fields_filter.map(x => x['field']);
        config_mostrar=module_data.permisos.mostrar.map(x => {
            x['field']=formatField(x['field']);
            return x;
        });
        console.log(fields);
    }

    const vars = { first: 100, after: ''}
    if (tipo > 0) {
        vars['tipo'] = tipo;
    }
    if (fields.includes("orden")){
        vars['sort'] = "orden ASC";
    }

    tipo=0;

    const table_query = 'all' + module.charAt(0).toUpperCase() + module.slice(1);
    const GET_LIST = gql(`
    query get_list($first:Int!,$after:String,$sort:String){
        $table(first:$first,after:$after,sort:$sort,$tipo){
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
            config_mostrar={config_mostrar}
            moreItemsLoading={loading}
            loadMore={loadMore}
            hasNextPage={hasNextPage}
            enableDrag={fields.includes("orden")}
            {...props}
        />
    )

};

export default ModuleList;