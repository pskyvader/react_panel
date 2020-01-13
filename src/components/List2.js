import React from 'react';
import LinearProgress from '@material-ui/core/LinearProgress';
import Paper from '@material-ui/core/Paper';

import { useQuery } from '@apollo/react-hooks';
import { gql } from 'apollo-boost';
import VirtualizedTable from './VirtualizedTable';
import Resolve from './Resolve';


export default function List(props) {
    const vars = { first: 10, after: '' }
    const table_query = 'all' + props.table;
    const GET_LIST = gql(`
    query get_list($first:Int!,$after:String){
        $table(first:$first,after:$after){
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
    `.replace('$table', table_query).replace('$fields', props.fields));
    
    const columns = [];
    props.fields.forEach(element => {
        columns.push(
            {
                width: 500,
                label: element,
                dataKey: element,
            }
        );
    });


    const { items, loading, loadMore, hasNextPage } = Resolve({query: GET_LIST,table:table_query,vars:vars});

    return (
        <Paper style={{ height: 400, width: '100%' }}>
            <VirtualizedTable
                rowCount={items.length}
                rowGetter={({ index }) => items[index]}
                columns={columns}
            />
        </Paper>
    );
}