import { useQuery } from '@apollo/react-hooks';
import { gql } from 'apollo-boost';
import ErrorLink from './ErrorLink';


const unitquery = (input, index, table) => {
    const table_update = 'update' + table.charAt(0).toUpperCase() + table.slice(1);
    let unitquery = `
    $table_update(input:$input){
        $table{
            id
        }
    }`.replace('$table_update', table_update).replace('$table', table).replace('$input', stringify(input));
    let query = `
    mutation update_list_$index{
        $unitquery
    }
    `.replace('$unitquery', unitquery).replace('$index', index);
    return query;
}


const stringify = (obj_from_json) => {
    if (typeof obj_from_json !== "object" || Array.isArray(obj_from_json)) {
        return JSON.stringify(obj_from_json);
    }
    let props = Object.keys(obj_from_json).map(key => `${key}:${stringify(obj_from_json[key])}`).join(",");
    return `{${props}}`;
}




export const CreateMutation = ({ table, multiple_inputs }) => {
    let query_list = "";
    multiple_inputs.forEach((input, index) => {
        query_list += unitquery(input, index, table);
    });
    const UPDATE_LIST = gql(query_list);
    return UPDATE_LIST;
}

export const Mutation = ({ mutation_list }) => {
    const { loading, error, data } = useQuery(mutation_list);
    if (loading) return null;
    if (error) return { 'error': error };
    if (data.module === null) {
        return false;
    }
}