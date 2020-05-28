import { gql } from 'apollo-boost';
import { useMutation } from '@apollo/react-hooks';
import ApolloCacheUpdater from "apollo-cache-updater";

// const stringify = (obj_from_json) => {
//     if (typeof obj_from_json !== "object" || Array.isArray(obj_from_json)) {
//         return JSON.stringify(obj_from_json);
//     }
//     let props = Object.keys(obj_from_json).map(key => `${key}:${stringify(obj_from_json[key])}`).join(",");
//     return `{${props}}`;
// }


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

let count = 0;

export const Mutation = ({ mutationquery, query, variables, mutation = "", Setsorting,table }) => {
    let extrafunction = {};
    if (mutation === "order") {
        extrafunction = {
            onError(data) {
                count--;
                if (count < 0) {
                    count = 0;
                }
                if (count === 0) {
                    Setsorting(false);
                }
            },
            refetchQueries: [{query:query,variables:variables, notifyOnNetworkStatusChange: true}],
            onCompleted(){
                count--;
                if (count < 0) {
                    count = 0;
                }
                if (count === 0) {
                    Setsorting(false);
                }
            },
        }
    }

    const [mutation_function] = useMutation(mutationquery, extrafunction);
    //console.log(data);
    const count_mutations = (props) => {
        count++;
        if (count === 1) {
            Setsorting(true);
        }
        return mutation_function(props);
    }
    return count_mutations;
}
