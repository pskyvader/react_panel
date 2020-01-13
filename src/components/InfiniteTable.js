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

const useStyles = makeStyles({
    table: {
        minWidth: 650,
    },
});


const InfiniteTable = ({ items, moreItemsLoading, loadMore, hasNextPage, columns }) => {
    const isItemLoaded = index => !hasNextPage || index < items.length;

    const Item = ({ index, style }) => {
        let content;
        if (!isItemLoaded(index)) {
            content = "Loading...";
        } else {
            content = items[index].username;
            var key=Object.values(items[index])[0];

            content = <TableRow key={key}>
                {Object.values(items[index]).map(column => (
                    <TableCell key={key+column.toString()} component="th" scope="row">
                        {column.toString()}
                    </TableCell>
                ))}
            </TableRow>

        }

        return <div style={style}>{content}</div>;
    };

    const itemCount = hasNextPage ? items.length + 1 : items.length;

    return (
        <InfiniteLoader
            isItemLoaded={isItemLoaded}
            itemCount={itemCount}
            loadMoreItems={loadMore}

        >

            {({ onItemsRendered, ref }) => (

                <Paper style={{ height: 400, width: '100%' }}>
                    <FixedSizeList
                        height={400}
                        itemCount={itemCount}
                        itemSize={120}
                        onItemsRendered={onItemsRendered}
                        ref={ref}
                    >


                        {Item}
                    </FixedSizeList>

                </Paper>

            )}

        </InfiniteLoader>



    )
};

export default InfiniteTable;