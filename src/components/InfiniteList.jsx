import React from 'react';
import InfiniteLoader from "react-window-infinite-loader";
import { makeStyles } from '@material-ui/core/styles';
import VirtualizedList from './VirtualizedList';
import { AutoSizer, List  } from 'react-virtualized';

const STATUS_LOADING = 1;
const STATUS_LOADED = 2;

const useStyles = makeStyles(theme => ({
    grid: {
        display: 'flex',
        justifyContent: 'center',
        [theme.breakpoints.up('md')]: {
            justifyContent: 'flex-start',
        },

    },
}));


const rowRenderer=({index, key, style}) =>{
    const {list} = this.context;
    const {loadedRowsMap} = this.state;

    const row = list.get(index);
    let content;

    if (loadedRowsMap[index] === STATUS_LOADED) {
      content = row.name;
    } else {
      content = (
        <div  style={{width: row.size}} />
      );
    }

    return (
      <div  key={key} style={style}>
        {content}
      </div>
    );
  }

const InfiniteList = ({ items, moreItemsLoading, loadMore, hasNextPage, columns, height }) => {
    const isItemLoaded = index => !hasNextPage || index < items.length;
    const itemCount = hasNextPage ? items.length + 1 : items.length;
    const classes = useStyles();

    const onScroll = ({ clientHeight, scrollHeight, scrollTop }) => {
        if (scrollTop >= (scrollHeight - clientHeight) * 0.7) {
            if (!moreItemsLoading && hasNextPage) {
                loadMore();
            }
        }
    };

    const max_height = () => {
        if (items.length * 48 <= height) {
            return (items.length) * 48;
        } else return height;
    }

    return (
              <InfiniteLoader
            isItemLoaded={isItemLoaded}
            itemCount={itemCount}
            loadMoreItems={loadMore}
        >
          {({onRowsRendered, registerChild}) => (
            <AutoSizer disableHeight>
              {({width}) => (
                <List
                  ref={registerChild}
                  height={200}
                  onRowsRendered={onRowsRendered}
                  rowCount={items.length}
                  rowHeight={30}
                  rowRenderer={rowRenderer}
                  width={width}
                />
              )}
            </AutoSizer>
          )}
        </InfiniteLoader>
    )

    return (
        <InfiniteLoader
            isItemLoaded={isItemLoaded}
            itemCount={itemCount}
            loadMoreItems={loadMore}
        >
            {({ onRowsRendered, registerChild }) => (
                <VirtualizedList
                    rowCount={items.length}
                    rowGetter={({ index }) => items[index]}
                    columns={columns}
                    ref={registerChild}
                    onRowsRendered={onRowsRendered}
                    onScroll={onScroll}
                    loading={moreItemsLoading}
                />
            )}
        </InfiniteLoader>

    )
};
export default InfiniteList;