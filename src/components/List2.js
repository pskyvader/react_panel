import React from 'react';
import LinearProgress from '@material-ui/core/LinearProgress';
import Paper from '@material-ui/core/Paper';

import { useQuery } from '@apollo/react-hooks';
import { gql } from 'apollo-boost';
import VirtualizedTable from './VirtualizedTable';


export default function List(props) {
    const table = 'all' + props.table;

    const GET_LIST = gql(`
    query get_list{
        $table(first:100){
            edges{
                node{
                    $fields
                }
            }
        }
    }
    `.replace('$table', table).replace('$fields', props.fields));


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

    const { loading, error, data } = useQuery(GET_LIST);
    if (loading) return <LinearProgress />;
    if (error) return 'Error';
    //console.log(data[table]);

    var rows = [];

    data[table]['edges'].forEach(element => {
        var e = element['node'];
        for (var key in e) {
            if (e.hasOwnProperty(key)) {
                e[key] = e[key].toString();
            }
        }
        rows.push(e);
    });

    return (
        <Paper style={{ height: 400, width: '100%' }}>
            <VirtualizedTable
                rowCount={rows.length}
                rowGetter={({ index }) => rows[index]}
                columns={columns}
            />
        </Paper>
    );
}