import * as React from 'react';
// import PropTypes from 'prop-types';
// import Immutable from 'immutable';
import InfiniteLoader from "react-window-infinite-loader";
import { AutoSizer, List } from 'react-virtualized';


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
        console.log(props);
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
        console.log(this.items,this.isItemLoaded);
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
        const { loadedRowsMap } = this.state;

        console.log(index, key, style,this.items);
        const row = this.items.get(index);

        let content;

        if (loadedRowsMap[index] === STATUS_LOADED) {
            content = row.name;
        } else {
            content = (
                <div style={{ width: row.size }} />
            );
        }

        return (
            <div key={key} style={style}>
                {content}
            </div>
        );
    }
}