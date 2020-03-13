import { useQuery } from '@apollo/react-hooks';
import { gql } from 'apollo-boost';
import ErrorLink from './ErrorLink';

function Mutation(props) {
    const {table,input}=props;
    console.log(input);
    const table_update = 'update' + table.charAt(0).toUpperCase() + table.slice(1);
    const UPDATE_LIST = gql(`
    mutation update_list{
        $table_update(input:$input){
            $table{
                id
            }
        }
    }
    `.replace('$table', table).replace('$table_update', table_update).replace('$input', JSON.stringify(input)));
    return UPDATE_LIST;
}

export default Mutation;