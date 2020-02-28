import * as React from 'react';
// import PropTypes from 'prop-types';
// import Immutable from 'immutable';
import InfiniteLoader from "react-window-infinite-loader";
import { AutoSizer, List } from 'react-virtualized';
import { WindowScroller } from 'react-virtualized';
import { Grid } from '@material-ui/core';
import ModuleCard from './ModuleCard';

export default class InfiniteList extends React.PureComponent {

    constructor(props) {
        super(props);

        this.state = {
            scrollToIndex: -1,
        };

        this._rowRenderer = this._rowRenderer.bind(this);
        this.items = props.items;
        this.moreItemsLoading = props.moreItemsLoading;
        this.loadMore = props.loadMore;
        this.hasNextPage = props.hasNextPage;
        this.itemCount = this.hasNextPage ? this.items.length + 1 : this.items.length;
    }
    isItemLoaded = index => !this.hasNextPage || index < this.items.length;


    render() {
        const { scrollToIndex } = this.state;
        console.log(this.items.length);
        return (

            <InfiniteLoader
                isItemLoaded={this.isItemLoaded}
                itemCount={this.itemCount}
                loadMoreItems={this.loadMore}>
                {({ onRowsRendered, registerChild }) => (
                    <WindowScroller
                        ref={this._setRef}
                        scrollElement={window}>
                        {({ height, isScrolling, registerChild, onChildScroll, scrollTop }) =>{
                            return (
                                <div >
                                    <AutoSizer disableHeight>
                                        {({ width }) => (
                                            <div ref={registerChild}>
                                                <List
                                                    ref={el => { window.listEl = el; }}
                                                    autoHeight
                                                    height={height}
                                                    isScrolling={isScrolling}
                                                    onScroll={onChildScroll}
                                                    overscanRowCount={2}
                                                    onRowsRendered={onRowsRendered}
                                                    rowCount={this.items.length}
                                                    rowHeight={442}
                                                    rowRenderer={this._rowRenderer}
                                                    scrollToIndex={scrollToIndex}
                                                    scrollTop={scrollTop}
                                                    width={width}
                                                />
                                            </div>
                                        )}
                                    </AutoSizer>
                                </div>
                            )
                        } 
                        }
                    </WindowScroller>
                )}
            </InfiniteLoader>
        )
    }


    _rowRenderer({ index, key }) {
        let element = this.items[index];

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