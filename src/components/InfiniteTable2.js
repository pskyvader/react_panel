import React from 'react';
import InfiniteLoader from "react-window-infinite-loader";
import TableCell from '@material-ui/core/TableCell';
import Paper from '@material-ui/core/Paper';
import classNames from 'clsx';
import { AutoSizer, Column, Table } from 'react-virtualized';


class InfiniteTable {
    state = {
        rowHeight: 0,
        loadedData: [],
    }
    constructor(props) {
        this.id = props.id;

        this.state = {
            loadedData: props.items
        }
    }
    getRowClassName = ({ index }) => {
        const { classes, rowClassName, onRowClick } = this.props;
        return classNames(classes.tableRow, classes.tableRowHover, classes.flexContainer, rowClassName)
    }

    cellRenderer = ({ cellData, columnIndex = null, rowIndex }) => {
        const { classes } = this.props
        return (
            <TableCell
                component="div"
                variant="body"
                className={classNames(classes.tableCell, classes.flexContainer)}
                style={{ height: this.state.rowHeight }}
            >
                {cellData.toString()}
            </TableCell>
        )
    }


    headerRenderer = ({ dataKey }) => {
        const { classes } = this.props;
        return (
            <TableCell
                component="div"
                className={classNames(classes.tableCell, classes.flexContainer)}
                variant="head"
            >
                {dataKey.toUpperCase()}
            </TableCell>
        )
    }


    loadMoreRows = () => {
        const { items, loading, loadMore, hasNextPage } = this.props.loadMore();
        this.setState({ loadedData: items });
    }

    isItemLoaded = index => !this.props.hasNextPage || !!this.state.loadedData[index];
    itemCount = this.props.hasNextPage ? this.state.loadedData.length + 1 : this.state.loadedData.length;

    componentDidMount() {
        this.setState({ rowHeight: this.props.rowHeight });
        this.loadMoreRows();
    }

    render() {
        const { classes, columns, rowHeight, headerHeight } = this.props;
        return (
            <InfiniteLoader
                isItemLoaded={this.isItemLoaded}
                itemCount={this.itemCount}
                loadMoreItems={this.loadMoreRows}
            >

                {({ onRowsRendered, registerChild }) => (
                    <Paper style={{ height: 400, width: '100%' }}>

                        <Table
                            ref={registerChild}
                            className={classes.table}
                            rowHeight={this.state.rowHeight}
                            rowCount={this.state.loadedData.length}
                            width={400}
                            height={'100%'}
                            headerHeight={40}
                            rowGetter={({ index }) => this.state.loadedData[index]}
                            onRowsRendered={onRowsRendered}
                            rowClassName={this.getRowClassName}
                        >

                            {this.props.columns.map((col) => {
                                return (
                                    <Column
                                        key={col.dataKey}
                                        label={col.label}
                                        dataKey={col.dataKey}
                                        headerRenderer={this.headerRenderer}
                                        className={classNames(classes.flexContainer)}
                                        cellRenderer={this.cellRenderer}
                                        width={col.width}
                                    />
                                )
                            })}

                        </Table>

                    </Paper>

                )}

            </InfiniteLoader >



        )
    }

};

export default InfiniteTable;