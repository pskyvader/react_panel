import { useQuery } from '@apollo/react-hooks';
import { gql } from 'apollo-boost';
import ErrorLink from './ErrorLink';

function Mutation(props) {
    const { table, multiple_inputs } = props;
    let query_list = "";
    multiple_inputs.forEach(input => {
        query_list += unitquery(input, table);
    });


    let query = `
    mutation update_list{
        $unitquery
    }
    `.replace('$unitquery', query_list);

    const UPDATE_LIST = gql(query);
    return UPDATE_LIST;
}


function unitquery(input, table) {
    let input_final = "{" + Object.keys(input).map((key, index) => {
        return key + ":" + input[key];
    }) + "}";

    const table_update = 'update' + table.charAt(0).toUpperCase() + table.slice(1);

    let unitquery = `
        $table_update(input:$input){
            $table{
                id
            }
        }
    `.replace('$table_update', table_update).replace('$table', table).replace('$input', input_final);
    return unitquery;
}





export default Mutation;