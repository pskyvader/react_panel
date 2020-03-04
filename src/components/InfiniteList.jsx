import * as React from 'react';
import InfiniteLoader from "react-window-infinite-loader";
import { AutoSizer } from 'react-virtualized';
import { WindowScroller } from 'react-virtualized';
import ModuleCard from './ModuleCard';
import { CellMeasurer, CellMeasurerCache } from 'react-virtualized';
import { createCellPositioner } from 'react-virtualized/dist/commonjs/Masonry';
import { Masonry } from 'react-virtualized';
import LinearProgress from '@material-ui/core/LinearProgress';
import {Grid} from 'react-virtualized';



export default class InfiniteList extends React.PureComponent {

    constructor(props) {
        super(props);

        this.state={
            items : props.items,
            moreItemsLoading : props.moreItemsLoading,
            loadMore : props.loadMore,
            hasNextPage : props.hasNextPage,
            itemCount : props.hasNextPage ? props.items.length + 1 : props.items.length
        }
        


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

    onScroll = ({ clientHeight, scrollHeight, scrollTop }) => {
        console.log('on scroll');
        if (scrollTop >= (scrollHeight - clientHeight) * 0.8) {
            if (!this.state.moreItemsLoading && this.state.hasNextPage) {
                let t=this;
                t.setState({
                    moreItemsLoading : true
                });
                this.state.loadMore(function(val){
                    if(t.props.items.length!==t.state.items.length){
                        t.setState({
                            items : t.props.items,
                            moreItemsLoading : t.props.moreItemsLoading,
                            loadMore : t.props.loadMore,
                            hasNextPage : t.props.hasNextPage,
                            itemCount : t.props.hasNextPage ? t.props.items.length + 1 : t.props.items.length
                        });
                    }
                    console.log('load more');
                });
            }
        }
    };

    isItemLoaded = index => !this.state.hasNextPage || index < this.state.items.length;

    getMinwidth = () =>{
        return this._width < 1280 ? this.minWidth : this.minWidthlg;
    } 

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

    render_progress = () => {
         return this.props.loading ? <LinearProgress /> : <div></div> 
        }

    render() {
        return (
            <InfiniteLoader
                isItemLoaded={this.state.isItemLoaded}
                itemCount={this.state.itemCount}
                loadMoreItems={this.state.loadMore}>
                {
                    ({ onRowsRendered }) => {
                        return (
                            <React.Fragment>
                                {this.render_progress()}
                                <WindowScroller overscanByPixels={this.overscanByPixels} scrollElement={window}>
                                    {({ height, isScrolling, registerChild, onChildScroll, scrollTop }) => (
                                        this._renderAutoSizer({ height, isScrolling, registerChild, onChildScroll, scrollTop, onRowsRendered })
                                    )}

                                </WindowScroller>
                            </React.Fragment>
                        )

                    }
                }
            </InfiniteLoader>
        )
    }

    _calculateColumnCount() {
        this._columnCount = Math.floor(this._width / (this.columnWidth + this.gutterSize));
    }

    _cellRenderer222({ index, key, parent, style }) {
        const cell = this.state.items[index];
        console.log()
        return (
            <CellMeasurer cache={this._cache} index={index} key={key} parent={parent}>
                <div style={{ ...style, width: this.columnWidth }}>
                    <ModuleCard element={cell} />
                </div>
            </CellMeasurer>
        );
    }
    _cellRenderer({columnIndex, key, rowIndex, style}) {
        const cell=this.state.items[rowIndex];
        return (
          <div key={key} style={style}>
            <ModuleCard element={cell} />
          </div>
        );
      }

    _initCellPositioner() {
        if (typeof this._cellPositioner === 'undefined') {
            let columnWidth = this.columnWidth;
            console.log("_initCellPositioner",this._width,columnWidth,this._columnCount,this.gutterSize);
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
        // this._masonry.recomputeCellPositions();
    }

    _renderAutoSizer({ height, scrollTop, onRowsRendered }) {
        this._height = height;
        this._scrollTop = scrollTop;


        return (
            <AutoSizer
                disableHeight
                height={height}
                onResize={this._onResize}
                overscanByPixels={this.overscanByPixels}
                scrollTop={this._scrollTop}>
                {({width}) => (
                    this._renderMasonry({ width, onRowsRendered })
                )}
            </AutoSizer>
        );
    }

    _renderMasonry({ width,onRowsRendered }) {
        this._width = width;
        this.columnWidth = this.getMinwidth();
        this._calculateColumnCount();
        this.cellwidth();

        this._initCellPositioner();
        let rowCount=1;
        rowCount=(this._columnCount>0)?this.state.items.length/this._columnCount:1;
        rowCount=(rowCount<1)?1:rowCount;

        return (
            <Grid
            autoHeight={true}
    cellRenderer={this._cellRenderer}
    columnCount={this._columnCount}
    columnWidth={this.columnWidth}
    height={300}
    rowCount={rowCount}
    rowHeight={300}
    width={this._width}
    onScroll={this.onScroll}
  />
        )

        return (
            <Masonry
                autoHeight={true}
                cellCount={this.state.items.length}
                cellMeasurerCache={this._cache}
                cellPositioner={this._cellPositioner}
                cellRenderer={this._cellRenderer}
                onCellsRendered={onRowsRendered}
                height={this._height}
                overscanByPixels={this.overscanByPixels}
                ref={this._setMasonryRef}
                scrollTop={this._scrollTop}
                width={width}
                onScroll={this.onScroll}
            />
        );
    }

    _resetCellPositioner() {
        let columnWidth = this.columnWidth;
        console.log("_resetCellPositioner",this._width,columnWidth,this._columnCount,this.gutterSize);

        this._cellPositioner.reset({
            columnCount: this._columnCount,
            columnWidth,
            spacer: this.gutterSize,
        });
    }

    _setMasonryRef(ref) {
        console.log("_setMasonryRef",this._width);
        this._masonry = ref;
    }
}