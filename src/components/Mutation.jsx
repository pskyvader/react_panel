import { useMutation } from '@apollo/react-hooks';
import { gql } from 'apollo-boost';

const stringify = (obj_from_json) => {
    if (typeof obj_from_json !== "object" || Array.isArray(obj_from_json)) {
        return JSON.stringify(obj_from_json);
    }
    let props = Object.keys(obj_from_json).map(key => `${key}:${stringify(obj_from_json[key])}`).join(",");
    return `{${props}}`;
}

export const CreateMutation = ({ table,fields, input }) => {
    const table_update = 'update' + table.charAt(0).toUpperCase() + table.slice(1);
    let query_list = `
    mutation update_element(${fields}){
        ${table_update}(input:${input}){
            ${table}{
            id
          }
        }
      }`;
    const UPDATE_LIST = gql(query_list);
    return UPDATE_LIST;
}




export const Mutation = ({ mutation_list }) => {
    const [addTodo, { data }] = useMutation(mutation_list);
    console.log(addTodo,data);
    return [addTodo,  data ];
}