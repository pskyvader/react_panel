import * as React from 'react';
// import PropTypes from 'prop-types';
// import Immutable from 'immutable';
import InfiniteLoader from "react-window-infinite-loader";
import { AutoSizer, List } from 'react-virtualized';
import { WindowScroller } from 'react-virtualized';
import { Grid } from '@material-ui/core';
import ModuleCard from './ModuleCard';
import { CellMeasurer, CellMeasurerCache } from 'react-virtualized';
import { createCellPositioner } from 'react-virtualized/dist/commonjs/Masonry';
import { Masonry } from 'react-virtualized';



export default class InfiniteList extends React.PureComponent {

    constructor(props) {
        super(props);
        this.items = props.items;
        this.moreItemsLoading = props.moreItemsLoading;
        this.loadMore = props.loadMore;
        this.hasNextPage = props.hasNextPage;
        this.itemCount = this.hasNextPage ? this.items.length + 1 : this.items.length;


        this._columnCount = 0;
        this.minWidth=245;
        this.maxWidth=345;

        this.state = {
            height: 300,
            gutterSize: 30,
            overscanByPixels: 0,
            windowScrollerEnabled: true,
        };

        this._cellRenderer = this._cellRenderer.bind(this);
        this._onResize = this._onResize.bind(this);
        this._renderAutoSizer = this._renderAutoSizer.bind(this);
        this._renderMasonry = this._renderMasonry.bind(this);
        this._setMasonryRef = this._setMasonryRef.bind(this);
        this.state.columnWidth = this.cellwidth(true);
        this._cache = new CellMeasurerCache({
            defaultHeight: 250,
            defaultWidth: this.state.columnWidth,
            fixedWidth: true,
        });


    }


    isItemLoaded = index => !this.hasNextPage || index < this.items.length;


    componentDidMount() {
        this.cellwidth();
    }

    cellwidth(return_value = false,width=0) {
        if (width<this.minWidth){
            width=this.minWidth;
        }else if(width>this.maxWidth){
            width=this.maxWidth;
        }
        if (return_value) {
            return width;
        }
        this.setState({ columnWidth: width });
    }



    render() {
        const { overscanByPixels } = this.state;
        return (
            <InfiniteLoader
                isItemLoaded={this.isItemLoaded}
                itemCount={this.itemCount}
                loadMoreItems={this.loadMore}>
                {({ onRowsRendered }) => (
                    <WindowScroller overscanByPixels={overscanByPixels} scrollElement={window}>
                        {({ height, isScrolling, registerChild, onChildScroll, scrollTop }) => (
                            this._renderAutoSizer({ height, isScrolling, registerChild, onChildScroll, scrollTop, onRowsRendered })
                        )}

                    </WindowScroller>
                    // this._renderAutoSizer({onRowsRendered})
                )}
            </InfiniteLoader>
        )
    }

    _calculateColumnCount() {
        const { columnWidth, gutterSize } = this.state;
        this._columnCount = Math.floor(this._width / (columnWidth + gutterSize));
        if (this._width!==0 && this._columnCount!==0){
            let new_width=(this._width/this._columnCount)-gutterSize;
            if (new_width!==columnWidth){
                console.log(new_width);
                this.cellwidth(false,new_width);
            }
        }
    }

    _cellRenderer({ index, key, parent, style }) {
        const { columnWidth } = this.state;

        const cell = this.items[index];

        return (
            <CellMeasurer cache={this._cache} index={index} key={key} parent={parent}>
                <div style={{ ...style, width: columnWidth }}>
                    <ModuleCard element={cell} />
                </div>
            </CellMeasurer>
        );
    }

    _initCellPositioner() {
        if (typeof this._cellPositioner === 'undefined') {
            const { columnWidth, gutterSize } = this.state;

            this._cellPositioner = createCellPositioner({
                cellMeasurerCache: this._cache,
                columnCount: this._columnCount,
                columnWidth,
                spacer: gutterSize,
            });
        }
    }

    _onResize({ width }) {
        this._width = width;

        this._calculateColumnCount();
        this._resetCellPositioner();
        this._masonry.recomputeCellPositions();
    }

    _renderAutoSizer({ height, scrollTop }) {
        this._height = height;
        this._scrollTop = scrollTop;

        const { overscanByPixels } = this.state;

        return (
            <AutoSizer
                disableHeight
                height={height}
                onResize={this._onResize}
                overscanByPixels={overscanByPixels}
                scrollTop={this._scrollTop}>
                {this._renderMasonry}
            </AutoSizer>
        );
    }

    _renderMasonry({ width }) {
        this._width = width;

        this._calculateColumnCount();
        this._initCellPositioner();

        const { height, overscanByPixels, windowScrollerEnabled } = this.state;

        return (
            <Masonry
                autoHeight={windowScrollerEnabled}
                cellCount={this.items.length}
                cellMeasurerCache={this._cache}
                cellPositioner={this._cellPositioner}
                cellRenderer={this._cellRenderer}
                height={windowScrollerEnabled ? this._height : height}
                overscanByPixels={overscanByPixels}
                ref={this._setMasonryRef}
                scrollTop={this._scrollTop}
                width={width}
            />
        );
    }

    _resetCellPositioner() {
        const { columnWidth, gutterSize } = this.state;

        this._cellPositioner.reset({
            columnCount: this._columnCount,
            columnWidth,
            spacer: gutterSize,
        });
    }

    _setMasonryRef(ref) {
        this._masonry = ref;
    }
}