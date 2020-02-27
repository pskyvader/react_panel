import React from 'react';
import InfiniteLoader from "react-window-infinite-loader";
import { makeStyles } from '@material-ui/core/styles';
import VirtualizedList from './VirtualizedList';


const useStyles = makeStyles(theme => ({
    grid: {
        display: 'flex',
        justifyContent: 'center',
        [theme.breakpoints.up('md')]: {
            justifyContent: 'flex-start',
        },

    },
}));


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