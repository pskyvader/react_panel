import React from 'react';
import InfiniteLoader from "react-window-infinite-loader";
import { AutoSizer } from 'react-virtualized';
import { WindowScroller } from 'react-virtualized';
import ModuleCard from './ModuleCard';
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
            itemCount : props.hasNextPage ? props.items.length + 1 : props.items.length,
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
        this.columnWidth = this.cellwidth(true);
    }

    onScroll = ({ clientHeight, clientWidth, scrollHeight, scrollLeft, scrollTop, scrollWidth }) => {
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
         return this.props.moreItemsLoading ? <LinearProgress /> : <div></div> 
        }

    render() {
        return (
            <InfiniteLoader
                isItemLoaded={this.state.isItemLoaded}
                itemCount={this.state.itemCount}
                loadMoreItems={this.state.loadMore}
                >
                {
                    ({ onRowsRendered, ref }) => {
                        return (
                            <React.Fragment >
                                {this.render_progress()}
                                <WindowScroller overscanByPixels={this.overscanByPixels} scrollElement={window} ref={ref}>
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

    _cellRenderer({columnIndex, key, rowIndex, style}) {
        const cell=this.state.items[rowIndex];
        return (
          <div key={key} style={style}>
            <ModuleCard element={cell} />
          </div>
        );
      }


    _onResize({ width }) {
        this._width = width;
        this.columnWidth = this.getMinwidth();
        this._calculateColumnCount();
        this.cellwidth();
    }

    _renderAutoSizer({ height, scrollTop, onRowsRendered ,onChildScroll}) {
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
                    this._renderMasonry({ width,height,onRowsRendered })
                )}
            </AutoSizer>
        );
    }

    _renderMasonry({ width,height,onRowsRendered }) {
        this._width = width;
        this.columnWidth = this.getMinwidth();
        this._calculateColumnCount();
        this.cellwidth();
        
        let rowCount=1;
        rowCount=(this._columnCount>0)? Math.floor(this.state.items.length/this._columnCount):1;
        rowCount=(rowCount<1)?1:rowCount;
        let height1=this.props.TypographyRef.current.offsetHeight;
        const height2=this.props.drawerHeaderRef.current.offsetHeight;

        let nodeStyle1 = window.getComputedStyle(this.props.TypographyRef.current);
        let slideMarginRight1 = nodeStyle1.getPropertyValue('margin-bottom');
        height1+=parseFloat(slideMarginRight1);

        let nodeStyle = window.getComputedStyle(this.props.mainRef.current);
        let slideMarginRight = nodeStyle.getPropertyValue('padding-top');

        const height3=parseInt(slideMarginRight)*2;
        const height4=4; //loader
        
        let gridHeight=height-(height1+height2+height3+height4);
        if(gridHeight<300){
            gridHeight=300;
        }


        return(
            <Grid
              cellRenderer={this._cellRenderer}
              columnWidth={this.columnWidth}
              columnCount={this._columnCount}
              height={gridHeight}
              noContentRenderer={this._noContentRenderer}
              overscanColumnCount={0}
              overscanRowCount={0}
              rowHeight={300}
              rowCount={rowCount}
              width={this._width}
              onScroll={this.onScroll}
            />
        )
        
    }

}