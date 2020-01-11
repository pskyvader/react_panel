import React from 'react';
import { FixedSizeList } from 'react-window';
import Table from '@material-ui/core/Table';
import InfiniteLoader from "react-window-infinite-loader";
import TableContainer from '@material-ui/core/TableContainer';
import Paper from '@material-ui/core/Paper';
import { makeStyles } from '@material-ui/core/styles';


const useStyles = makeStyles({
    table: {
      minWidth: 650,
    },
  });


const InfiniteTable = ({ items, moreItemsLoading, loadMore, hasNextPage,columns}) => {
    const isItemLoaded = index => !hasNextPage || index < items.length;

    const Item = ({ index, style }) => {
        let content;
        if (!isItemLoaded(index)) {
          content = "Loading...";
        } else {
          content = items[index].username;
        }
    
        return <div style={style}>{content}</div>;
      };

  const itemCount = hasNextPage ? items.length + 1 : items.length;

  const classes = useStyles();

  return (
    <InfiniteLoader
      isItemLoaded={isItemLoaded}
      itemCount={itemCount}
      loadMoreItems={loadMore}

    >

<TableContainer component={Paper}>
      <Table className={classes.table} aria-label="simple table">
        <TableHead>
          <TableRow>
          {columns.map(column => (
              <TableCell align="right">{column.label}</TableCell>
          ))}
          </TableRow>
        </TableHead>
        <TableBody>
            
      {({ onItemsRendered, ref }) => (
        <FixedSizeList
          height={500}
          width={500}
          itemCount={itemCount}
          itemSize={120}
          onItemsRendered={onItemsRendered}
          ref={ref}
        >
          {Item}
        </FixedSizeList>
      )}
        </TableBody>
      </Table>
    </TableContainer>

  </InfiniteLoader>
  )
};

export default InfiniteTable;