import React from 'react';
import InfiniteLoader from "react-window-infinite-loader";
import Paper from '@material-ui/core/Paper';
import VirtualizedTable from './VirtualizedTable';

const InfiniteTable = ({ items, moreItemsLoading, loadMore, hasNextPage, columns }) => {
    const isItemLoaded = index => !hasNextPage || index < items.length;
    const itemCount = hasNextPage ? items.length + 1 : items.length;

    const onScroll=({ clientHeight, scrollHeight, scrollTop })=>{
        console.log('scroll',clientHeight, scrollHeight, scrollTop);
        if(scrollTop>=(scrollHeight-clientHeight)*0.7  || clientHeight<0){
            console.log('mayor');
            if (!moreItemsLoading && hasNextPage){
                console.log('loading');
                loadMore();
            }
        }
    };



    return (
        <InfiniteLoader
            isItemLoaded={isItemLoaded}
            itemCount={itemCount}
            loadMoreItems={loadMore}
        >

            {({ onRowsRendered, registerChild }) => (
                <Paper style={{ height: 700, width: '100%' }}>
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
    )
};

export default InfiniteTable;