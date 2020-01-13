import React from 'react';
import InfiniteLoader from "react-window-infinite-loader";
import TableCell from '@material-ui/core/TableCell';
import Paper from '@material-ui/core/Paper';
import { AutoSizer, Column, Table } from 'react-virtualized';
import { withStyles } from '@material-ui/core/styles';
import PropTypes from 'prop-types';
import clsx from 'clsx';




const styles = theme => ({
    flexContainer: { display: 'flex', alignItems: 'center', boxSizing: 'border-box', },
    table: { '& .ReactVirtualized__Table__headerRow': { flip: false, paddingRight: theme.direction === 'rtl' ? '0px !important' : undefined, }, },
    tableRow: { cursor: 'pointer', },
    tableRowHover: { '&:hover': { backgroundColor: theme.palette.grey[200], }, },
    tableCell: { flex: 1, },
    noClick: { cursor: 'initial', },
});



class MuiInfiniteTable extends React.PureComponent {
    static defaultProps = { headerHeight: 48, rowHeight: 48, };
    state = {
        loadedData: [],
    }
    constructor(props) {
        super(props);
        console.log(props);

        this.state = {
            loadedData: props.items
        }
    }
    getRowClassName = ({ index }) => {
        const { classes, rowClassName, onRowClick } = this.props;
        return clsx(classes.tableRow, classes.tableRowHover, classes.flexContainer, rowClassName)
    }

    cellRenderer = ({ cellData, columnIndex = null, rowIndex }) => {
        const { classes } = this.props
        return (
            <TableCell
                component="div"
                variant="body"
                className={clsx(classes.tableCell, classes.flexContainer)}
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
                className={clsx(classes.tableCell, classes.flexContainer)}
                variant="head"
            >
                {dataKey.toUpperCase()}
            </TableCell>
        )
    }


    loadMoreRows = () => {
        this.setState({ loadedData: this.props.items });
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
                loadMoreItems={this.props.loadMore}
            >

                {({ onRowsRendered, registerChild }) => (
                    <Paper style={{ height: 400, width: '100%' }}>
                        <AutoSizer>
                            {({ height, width }) => (
                                <Table
                                    ref={registerChild}
                                    className={classes.table}
                                    rowHeight={rowHeight}
                                    rowCount={this.state.loadedData.length}
                                    height={width}
                                    width={height}
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
                                                className={clsx(classes.flexContainer)}
                                                cellRenderer={this.cellRenderer}
                                                width={col.width}
                                            />
                                        )
                                    })}

                                </Table>
                            )}
                        </AutoSizer>
                    </Paper>

                )}

            </InfiniteLoader >



        )
    }

};



MuiInfiniteTable.propTypes = {
    classes: PropTypes.object.isRequired,
    columns: PropTypes.arrayOf(PropTypes.shape({ dataKey: PropTypes.string.isRequired, label: PropTypes.string.isRequired, numeric: PropTypes.bool, width: PropTypes.number.isRequired, })).isRequired,
    headerHeight: PropTypes.number,
    onRowClick: PropTypes.func,
    rowHeight: PropTypes.number,
};

const InfiniteTable = withStyles(styles)(MuiInfiniteTable);


export default InfiniteTable;