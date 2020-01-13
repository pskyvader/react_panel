import React from 'react';
import { FixedSizeList } from 'react-window';
import InfiniteLoader from "react-window-infinite-loader";
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

import AutoSizer from 'react-virtualized-auto-sizer';
import VirtualizedTable from './VirtualizedTable';

class InfiniteTable {
    constructor(props) {
        super(props);
        this.id = props.id;
        this.state = {
            loadedData: props.items
        }
    }

    loadMoreRows = ({ startIndex, stopIndex }) => {
        const { items, loading, loadMore, hasNextPage } = this.props.loadMore();
        this.setState({ loadedData: items });
    }

    isItemLoaded = index => !this.props.hasNextPage || !!this.state.loadedData[index];
    itemCount = this.props.hasNextPage ? this.state.loadedData.length + 1 : this.state.loadedData.length;

    render() {

        return (
            <InfiniteLoader 
            isItemLoaded={this.isItemLoaded} 
            itemCount={this.itemCount} 
            loadMoreItems={this.loadMoreRows} 
            >

                {({ onItemsRendered, ref }) => (
                    <Paper style={{ height: 400, width: '100%' }}>
                        

                    </Paper>

                )}

            </InfiniteLoader >



        )
    }

};

export default InfiniteTable;