import * as React from 'react';
// import PropTypes from 'prop-types';
// import Immutable from 'immutable';
import InfiniteLoader from "react-window-infinite-loader";
import { AutoSizer, List } from 'react-virtualized';
import { Grid } from '@material-ui/core';
import ModuleCard from './ModuleCard';


const STATUS_LOADING = 1;
const STATUS_LOADED = 2;

export default class InfiniteList extends React.PureComponent {
    //   static contextTypes = {
    //     list: PropTypes.instanceOf(Immutable.List).isRequired,
    //   };

    constructor(props) {
        super(props);

        this.state = {
            loadedRowCount: 0,
            loadedRowsMap: {},
            loadingRowCount: 0,
        };

        this._timeoutIdMap = {};

        this._rowRenderer = this._rowRenderer.bind(this);
        this.items = props.items;
        this.moreItemsLoading = props.moreItemsLoading;
        this.loadMore = props.loadMore;
        this.hasNextPage = props.hasNextPage;
        this.itemCount = this.hasNextPage ? this.items.length + 1 : this.items.length;
    }
    isItemLoaded = index => !this.hasNextPage || index < this.items.length;

    componentWillUnmount() {
        Object.keys(this._timeoutIdMap).forEach(timeoutId => {
            clearTimeout(timeoutId);
        });
    }

    render() {
        return (
            <InfiniteLoader
                isItemLoaded={this.isItemLoaded}
                itemCount={this.itemCount}
                loadMoreItems={this.loadMore}>
                {({ onRowsRendered, registerChild }) => (
                    <AutoSizer disableHeight>
                        {({ width }) => (
                            <List
                                ref={registerChild}
                                height={200}
                                onRowsRendered={onRowsRendered}
                                rowCount={this.items.length}
                                rowHeight={30}
                                rowRenderer={this._rowRenderer}
                                width={width}
                            />
                        )}
                    </AutoSizer>
                )}
            </InfiniteLoader>
        );
    }


    _rowRenderer({ index, key, style }) {
        console.log(index, key, style,this.items);
        let element=this.items[index];

        let content = (
            <ModuleCard {...element} />
        );

        return (
            <Grid item xs={12} sm key={key}>
                {content}
                </Grid>
        );
    }
}