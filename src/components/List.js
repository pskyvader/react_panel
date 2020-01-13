import React, { PureComponent } from 'react';
import { gql } from 'apollo-boost';
import InfiniteTable from './InfiniteTable';
import Resolve from './Resolve';


function List(props) {
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


    const {error, items, loading, loadMore, hasNextPage } = Resolve({query: GET_LIST,table:table_query,vars:vars});

    if (error){
    return (<div>Error {error}</div>)
    }else{

        return (
            <InfiniteTable
                items={items}
                moreItemsLoading={loading}
                loadMore={loadMore}
                hasNextPage={hasNextPage}
                columns={columns}
            />
        );
    }

}
export default List;