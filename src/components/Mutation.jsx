import { gql } from 'apollo-boost';
import { useMutation } from '@apollo/react-hooks';

// const stringify = (obj_from_json) => {
//     if (typeof obj_from_json !== "object" || Array.isArray(obj_from_json)) {
//         return JSON.stringify(obj_from_json);
//     }
//     let props = Object.keys(obj_from_json).map(key => `${key}:${stringify(obj_from_json[key])}`).join(",");
//     return `{${props}}`;
// }

let count=0;

export const CreateMutation = ({ table, fields, input }) => {
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

export const Mutation = ({ mutationquery, query, variables, mutation = "" }) => {
    let extrafunction = {};
    if (mutation === "order") {
        extrafunction = {
            update(cache, { data: mf }) {
                const querycache = cache.readQuery({ query: query, variables: variables });
                const querykey = Object.keys(querycache)[0];
                const elementcache = querycache[querykey];

                console.log(elementcache.edges);

                let finaldata = {};
                finaldata[querykey] = elementcache;

                cache.writeQuery({
                    query: query,
                    variables: variables,
                    data: finaldata,
                });
            }
        }
    }

    const [mutation_function, data] = useMutation(mutationquery, extrafunction);
    const count_mutations=(props)=>{
        return mutation_function(props);
    }
    return count_mutations;
}
