import { useQuery } from '@apollo/react-hooks';
import { gql } from 'apollo-boost';
import ErrorLink from './ErrorLink';

function Mutation(props) {
    const { table, multiple_inputs } = props;
    let query_list = "";
    multiple_inputs.forEach((input,index) => {
        query_list += unitquery(input,index, table);
    });


    // let query = `
    // mutation update_list{
    //     $unitquery
    // }
    // `.replace('$unitquery', query_list);

    console.log(query_list);

    const UPDATE_LIST = gql(query_list);
    return UPDATE_LIST;
}


const unitquery=(input,index, table) =>{
    let input_final = "{" + Object.keys(input).map(key =>  key + ':"' + input[key]+'"' ) + "}";


    const table_update = 'update' + table.charAt(0).toUpperCase() + table.slice(1);
    let unitquery = `
        $table_update(input:$input){
            $table{
                id
            }
        }
    `.replace('$table_update', table_update).replace('$table', table).replace('$input', input_final);
    let query = `
    mutation update_list_$index{
        $unitquery
    }
    `.replace('$unitquery', unitquery).replace('$index', index);
    return query;
}





export default Mutation;