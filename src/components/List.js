import React, { PureComponent } from 'react';
import { gql } from 'apollo-boost';
import InfiniteTable2 from './InfiniteTable2';
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


    const { items, loading, loadMore, hasNextPage } = Resolve({query: GET_LIST,table:table_query,vars:vars});

    return (
        <InfiniteTable2
            items={items}
            moreItemsLoading={loading}
            loadMore={loadMore}
            hasNextPage={hasNextPage}
            columns={columns}

            rowHeight={100}
            rowCount={500}
        />
    );
}
export default List;