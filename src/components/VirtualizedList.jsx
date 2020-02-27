import React, { Fragment } from 'react';
import PropTypes from 'prop-types';
import clsx from 'clsx';
import { withStyles } from '@material-ui/core/styles';
import TableCell from '@material-ui/core/TableCell';
import { AutoSizer, Column, Table } from 'react-virtualized';
import LinearProgress from '@material-ui/core/LinearProgress';
import ModuleCard from './ModuleCard';
import Paper from '@material-ui/core/Paper';
import { Grid } from '@material-ui/core';


const styles = theme => ({
    flexContainer: { display: 'flex', alignItems: 'center', boxSizing: 'border-box', },
    table: { '& .ReactVirtualized__Table__headerRow': { flip: false, paddingRight: theme.direction === 'rtl' ? '0px !important' : undefined, }, },
    tableRow: { cursor: 'pointer', },
    tableRowHover: { '&:hover': { backgroundColor: theme.palette.grey[200], }, },
    tableCell: { flex: 1, },
    noClick: { cursor: 'initial', },
});



class MuiVirtualizedTable extends React.PureComponent {
    static defaultProps = { headerHeight: 48, rowHeight: 48, };

    
    render_progress=()=>{
        return this.props.loading?<LinearProgress/>:<div></div> 
    }

    render() {
        const { classes, columns, rowHeight, headerHeight, ...tableProps } = this.props;
        return (
            <Fragment>
            {this.render_progress()}
            <AutoSizer>
                {({ height, width }) => (
                    
                    <Grid
                        container
                        direction="row"
                        justify="flex-start"
                        alignItems="flex-start" spacing={3}
                    >
                        {tableProps.items.map((element, index) => {
                            return (
                                <Grid item xs={12} sm className={classes.grid} key={index}>
                                    <ModuleCard {...element} />
                                </Grid>
                            )
                        })}
                    </Grid>
                )}
            </AutoSizer>
            </Fragment>
        );
    }
}

MuiVirtualizedTable.propTypes = {
    classes: PropTypes.object.isRequired,
    columns: PropTypes.arrayOf( PropTypes.shape({ dataKey: PropTypes.string.isRequired, label: PropTypes.string.isRequired, numeric: PropTypes.bool, width: PropTypes.number.isRequired, }), ).isRequired,
    headerHeight: PropTypes.number,
    onRowClick: PropTypes.func,
    rowHeight: PropTypes.number,
};

const VirtualizedTable = withStyles(styles)(MuiVirtualizedTable);

export default VirtualizedTable;
