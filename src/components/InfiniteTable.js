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
            content = <TableRow key={items[index][0]}>
                {Object.values(items[index]).map(column => (
                    <TableCell component="th" scope="row">
                        {column.toString()}
                    </TableCell>
                ))}
            </TableRow>

        }




        return <div style={style}>{content}</div>;
    };

    const itemCount = hasNextPage ? items.length + 1 : items.length;

    const classes = useStyles();

    return (

        <TableContainer component={Paper}>
            <Table className={classes.table} aria-label="simple table">
                <TableHead>
                    <TableRow>
                        {columns.map(column => (
                            <TableCell align="right" key={column.dataKey}>{column.label}</TableCell>
                        ))}
                    </TableRow>
                </TableHead>
                <TableBody>

                    <AutoSizer>
                        {({ height, width }) => (
                            <InfiniteLoader
                                isItemLoaded={isItemLoaded}
                                itemCount={itemCount}
                                loadMoreItems={loadMore}

                            >

                                {({ onItemsRendered, ref }) => (
                                    <FixedSizeList
                                        height={height}
                                        width={width}
                                        itemCount={itemCount}
                                        itemSize={120}
                                        onItemsRendered={onItemsRendered}
                                        ref={ref}
                                    >


                                        {Item}
                                    </FixedSizeList>
                                )}

                            </InfiniteLoader>
                        )}
                    </AutoSizer>

                </TableBody>
            </Table>
        </TableContainer>




    )
};

export default InfiniteTable;