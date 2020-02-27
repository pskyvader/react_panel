import React from 'react';
import InfiniteLoader from "react-window-infinite-loader";
import Paper from '@material-ui/core/Paper';
import { Grid } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import ModuleCard from '../components/ModuleCard';


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
                    <Grid
                        container
                        direction="row"
                        justify="flex-start"
                        alignItems="flex-start" spacing={3}
                    >
                        {items.map((element, index) => {
                            return (
                                <Grid item xs={12} sm className={classes.grid} key={index}>
                                    <ModuleCard {...element} />
                                </Grid>
                            )
                        })}
                    </Grid>
            )}
        </InfiniteLoader>
    )
};
export default InfiniteList;