import React, { PureComponent } from 'react';
import LinearProgress from '@material-ui/core/LinearProgress';
import Paper from '@material-ui/core/Paper';

import { useQuery } from '@apollo/react-hooks';
import { gql } from 'apollo-boost';
import InfiniteTable from './InfiniteTable';
import Resolve from './Resolve';


class List2 extends PureComponent {
    constructor(props) {
        super(props);
        this.state = {
            items: [],
            moreItemsLoading: false,
            hasNextPage: true,
            after: '',
            first: 10
        };

        this.loadMore = this.loadMore.bind(this);
        this.table = 'all' + props.table;
        this.GET_LIST = gql(`
        query get_list($first:Int!,$after:String){
            pageInfo{
                hasNextPage
            }
            $table(first:$first,after:$after){
                edges{
                    node{
                        $fields
                    }
                }
            }
        }
        `.replace('$table', this.table).replace('$fields', props.fields));

        this.columns = [];
        props.fields.forEach(element => {
            this.columns.push(
                {
                    width: 500,
                    label: element,
                    dataKey: element,
                }
            );
        });
    }



    loadMore() {
        this.setState({ isNextPageLoading: true }, () => {
            var vars = { variables: { first: this.state.first, after: this.state.after }, notifyOnNetworkStatusChange: true }
            const { loading, error, data } = useQuery(this.GET_LIST, vars);
            if (loading) return <LinearProgress />;
            if (error) return 'Error';
            //console.log(data[table]);

            var rows = [];

            data[this.table]['edges'].forEach(element => {
                var e = element['node'];
                for (var key in e) {
                    if (e.hasOwnProperty(key)) {
                        e[key] = e[key].toString();
                    }
                }
                rows.push(e);
            });

            this.setState(state => ({
                hasNextPage: data[this.table]['pageInfo']['hasNextPage'],
                isNextPageLoading: false,
                items: [...state.items].concat(
                    rows
                )
            }));

        });
    }


    render() {
        const { items, moreItemsLoading, hasNextPage } = this.state;

        return (
            <InfiniteTable
                items={items}
                moreItemsLoading={moreItemsLoading}
                loadMore={this.loadMore}
                hasNextPage={hasNextPage}
            />
        );
    }



}

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
        <InfiniteTable
            items={items}
            moreItemsLoading={loading}
            loadMore={loadMore}
            hasNextPage={hasNextPage}
            columns={columns}
        />
    );
}
export default List;