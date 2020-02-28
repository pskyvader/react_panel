import * as React from 'react';
import InfiniteLoader from "react-window-infinite-loader";
import { AutoSizer } from 'react-virtualized';
import { WindowScroller } from 'react-virtualized';
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
        this.minWidth = 245;
        this.minWidthlg = 290;
        this.maxWidth = 345;
        this.gutterSize = 30;
        this.overscanByPixels = 0;

        this._cellRenderer = this._cellRenderer.bind(this);
        this._onResize = this._onResize.bind(this);
        this._renderAutoSizer = this._renderAutoSizer.bind(this);
        this._renderMasonry = this._renderMasonry.bind(this);
        this._setMasonryRef = this._setMasonryRef.bind(this);
        this.columnWidth = this.cellwidth(true);
        this._cache = new CellMeasurerCache({
            defaultHeight: 250,
            defaultWidth: this.columnWidth,
            fixedWidth: true,
        });


    }

    isItemLoaded = index => !this.hasNextPage || index < this.items.length;

    getMinwidth = () => this._width < 1280 ? this.minWidth : this.minWidthlg;

    cellwidth(return_value = false) {
        let width = 0;
        if (this._width !== 0 && this._columnCount !== 0) {
            width = Math.floor((this._width / this._columnCount) - this.gutterSize);
        }
        if (width < this.getMinwidth()) {
            width = this.getMinwidth();
        } else if (width > this.maxWidth) {
            width = this.maxWidth;
        }

        if (return_value) {
            return width;
        }
        this.columnWidth = width;
    }



    render() {
        return (
            <InfiniteLoader
                isItemLoaded={this.isItemLoaded}
                itemCount={this.itemCount}
                loadMoreItems={this.loadMore}>
                {
                ({ onRowsRendered }) => {
                    console.log(onRowsRendered);
                        return (
                            <WindowScroller overscanByPixels={this.overscanByPixels} scrollElement={window}>
                                {({ height, isScrolling, registerChild, onChildScroll, scrollTop }) => (
                                    this._renderAutoSizer({ height, isScrolling, registerChild, onChildScroll, scrollTop, onRowsRendered })
                                )}

                            </WindowScroller>
                        )

                    }
                }
            </InfiniteLoader>
        )
    }

    _calculateColumnCount() {
        this._columnCount = Math.floor(this._width / (this.columnWidth + this.gutterSize));
    }

    _cellRenderer({ index, key, parent, style }) {
        const cell = this.items[index];
        return (
            <CellMeasurer cache={this._cache} index={index} key={key} parent={parent}>
                <div style={{ ...style, width: this.columnWidth }}>
                    <ModuleCard element={cell} />
                </div>
            </CellMeasurer>
        );
    }

    _initCellPositioner() {
        if (typeof this._cellPositioner === 'undefined') {
            let columnWidth = this.columnWidth;
            this._cellPositioner = createCellPositioner({
                cellMeasurerCache: this._cache,
                columnCount: this._columnCount,
                columnWidth,
                spacer: this.gutterSize,
            });
        }
    }

    _onResize({ width }) {
        this._width = width;
        this.columnWidth = this.getMinwidth();
        this._calculateColumnCount();
        this.cellwidth();

        this._resetCellPositioner();
        this._masonry.recomputeCellPositions();
    }

    _renderAutoSizer({ height, scrollTop, onRowsRendered }) {
        this._height = height;
        this._scrollTop = scrollTop;
        console.log(onRowsRendered);


        return (
            <AutoSizer
                disableHeight
                height={height}
                onResize={this._onResize}
                overscanByPixels={this.overscanByPixels}
                scrollTop={this._scrollTop}>
                {this._renderMasonry}
            </AutoSizer>
        );
    }

    _renderMasonry({ width }) {
        this._width = width;
        this.columnWidth = this.getMinwidth();
        this._calculateColumnCount();
        this.cellwidth();

        this._initCellPositioner();


        return (
            <Masonry
                autoHeight={true}
                cellCount={this.items.length}
                cellMeasurerCache={this._cache}
                cellPositioner={this._cellPositioner}
                cellRenderer={this._cellRenderer}
                height={this._height}
                overscanByPixels={this.overscanByPixels}
                ref={this._setMasonryRef}
                scrollTop={this._scrollTop}
                width={width}
            />
        );
    }

    _resetCellPositioner() {
        let columnWidth = this.columnWidth;

        this._cellPositioner.reset({
            columnCount: this._columnCount,
            columnWidth,
            spacer: this.gutterSize,
        });
    }

    _setMasonryRef(ref) {
        this._masonry = ref;
    }
}