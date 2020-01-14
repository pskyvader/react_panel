import React from 'react';
import InfiniteLoader from "react-window-infinite-loader";
<<<<<<< HEAD
import { makeStyles } from '@material-ui/core/styles';
// import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
=======
>>>>>>> 5da314366bbdac8a5834421f99c737a2a0039823
import Paper from '@material-ui/core/Paper';
import VirtualizedTable from './VirtualizedTable';

<<<<<<< HEAD
import { AutoSizer, Column, Table } from 'react-virtualized';

const useStyles = makeStyles({
    table: {
        minWidth: 650,
    },
});
















const cellRenderer = ({ cellData, columnIndex }) => {
    const { columns, classes, rowHeight, onRowClick } = this.props;
    return (
        <TableCell
            component="div"
            className={clsx(classes.tableCell, classes.flexContainer, { [classes.noClick]: onRowClick == null, })}
            variant="body"
            style={{ height: rowHeight }}
            align={(columnIndex != null && columns[columnIndex].numeric) || false ? 'right' : 'left'}
        >
            {cellData}
        </TableCell>
    );
};

const headerRenderer = ({ label, columnIndex }) => {
    const { headerHeight, columns, classes } = this.props;

    return (
        <TableCell
            component="div"
            className={clsx(classes.tableCell, classes.flexContainer, classes.noClick)}
            variant="head"
            style={{ height: headerHeight }}
            align={columns[columnIndex].numeric || false ? 'right' : 'left'}
        >
            <span>{label}</span>
        </TableCell>
    );
};
















const InfiniteTable = ({ items, moreItemsLoading, loadMore, hasNextPage, columns }) => {
=======
const InfiniteTable = ({ items, moreItemsLoading, loadMore, hasNextPage, columns,height }) => {
>>>>>>> 5da314366bbdac8a5834421f99c737a2a0039823
    const isItemLoaded = index => !hasNextPage || index < items.length;
    const itemCount = hasNextPage ? items.length + 1 : items.length;

<<<<<<< HEAD
    const Item = ({ index, style }) => {
        let content;
        if (!isItemLoaded(index)) {
            content = "Loading...";
            if(moreItemsLoading){
                content+=" Loading ...";
            }
        } else {
            content = items[index].username;
            content = <TableRow key={items[index][0]}>
                {Object.values(items[index]).map(column => (
                    <TableCell component="th" scope="row">
                        {column.toString()}
                    </TableCell>
                ))}
            </TableRow>

=======
    const onScroll = ({ clientHeight, scrollHeight, scrollTop }) => {
        if (scrollTop >= (scrollHeight - clientHeight) * 0.7) {
            if (!moreItemsLoading && hasNextPage) {
                loadMore();
            }
>>>>>>> 5da314366bbdac8a5834421f99c737a2a0039823
        }
    };

    const  max_height=()=>{
        if(items.length*48<=height){
            return (items.length)*48;
        }else return height;
    }


    const rowHeight=400;
    const headerHeight=20;
    const tableProps=null;

    return (
        <AutoSizer>
            {({ height, width }) => (
                <Table height={height} width={width} rowHeight={rowHeight} gridStyle={{ direction: 'inherit', }} headerHeight={headerHeight} className={classes.table} {...tableProps}  >
                    
                    

                    <InfiniteLoader
                                isItemLoaded={isItemLoaded}
                                itemCount={itemCount}
                                loadMoreItems={loadMore}

                            >


                    
                    {columns.map(({ dataKey, ...other }, index) => {
                        return (
                            <Column
                                key={dataKey}
                                headerRenderer={headerProps =>
                                    this.headerRenderer({
                                        ...headerProps,
                                        columnIndex: index,
                                    })
                                }
                                className={classes.flexContainer}
                                cellRenderer={this.cellRenderer}
                                dataKey={dataKey}
                                {...other}
                            />
                        );
                    })}


                                {({ onItemsRendered, ref }) => (
                                    <FixedSizeList
                                        height={450}
                                        width={200}
                                        itemCount={itemCount}
                                        itemSize={120}
                                        onItemsRendered={onItemsRendered}
                                        ref={ref}
                                    >


                                        {Item}
                                    </FixedSizeList>
                                )}

                            </InfiniteLoader>





                </Table>
            )}
        </AutoSizer>
    );






    return (
<<<<<<< HEAD

        <AutoSizer>
        {({ height, width }) => (
        <TableContainer component={Paper} >
            <Table className={classes.table} aria-label="simple table">
                <TableHead>
                    <TableRow>
                        {columns.map(column => (
                            <TableCell align="left" key={column.dataKey}>{column.label}</TableCell>
                        ))}
                    </TableRow>
                </TableHead>
                <TableBody>

                            <InfiniteLoader
                                isItemLoaded={isItemLoaded}
                                itemCount={itemCount}
                                loadMoreItems={loadMore}

                            >

                                {({ onItemsRendered, ref }) => (
                                    <FixedSizeList
                                        height={450}
                                        width={200}
                                        itemCount={itemCount}
                                        itemSize={120}
                                        onItemsRendered={onItemsRendered}
                                        ref={ref}
                                    >


                                        {Item}
                                    </FixedSizeList>
                                )}

                            </InfiniteLoader>
                        

                </TableBody>
            </Table>
        </TableContainer>
        )}
        </AutoSizer>
=======
        <InfiniteLoader
            isItemLoaded={isItemLoaded}
            itemCount={itemCount}
            loadMoreItems={loadMore}
        >

            {({ onRowsRendered, registerChild }) => (
                <Paper style={{ height: max_height(), width: '100%' }}>
                    <VirtualizedTable
                        rowCount={items.length}
                        rowGetter={({ index }) => items[index]}
                        columns={columns}
                        ref={registerChild}
                        onRowsRendered={onRowsRendered}
                        onScroll={onScroll}
                        loading={moreItemsLoading}

                    />
                </Paper>
            )}
        </InfiniteLoader>
>>>>>>> 5da314366bbdac8a5834421f99c737a2a0039823
    )
};

export default InfiniteTable;