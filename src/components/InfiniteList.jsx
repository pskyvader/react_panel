import * as React from 'react';
// import PropTypes from 'prop-types';
// import Immutable from 'immutable';
import InfiniteLoader from "react-window-infinite-loader";
import { AutoSizer, List } from 'react-virtualized';
import { WindowScroller } from 'react-virtualized';
import { Grid } from '@material-ui/core';
import ModuleCard from './ModuleCard';
import {CellMeasurer, CellMeasurerCache} from 'react-virtualized';
import {Masonry} from 'react-virtualized';
import {createCellPositioner} from 'react-virtualized/dist/commonjs/Masonry/createCellPositioner';

export default class InfiniteList extends React.PureComponent {

    constructor(props) {
        super(props);

        this.items = props.items;
        this.moreItemsLoading = props.moreItemsLoading;
        this.loadMore = props.loadMore;
        this.hasNextPage = props.hasNextPage;
        this.itemCount = this.hasNextPage ? this.items.length + 1 : this.items.length;


        this._columnCount = 0;

        this._cache = new CellMeasurerCache({
            defaultHeight: 250,
            defaultWidth: 200,
            fixedWidth: true,
        });

        this.state = {
            columnWidth: 200,
            height: 300,
            gutterSize: 10,
            overscanByPixels: 0,
            windowScrollerEnabled: false,
        };

        this._cellRenderer = this._cellRenderer.bind(this);
        this._onResize = this._onResize.bind(this);
        this._renderAutoSizer = this._renderAutoSizer.bind(this);
        this._renderMasonry = this._renderMasonry.bind(this);
        this._setMasonryRef = this._setMasonryRef.bind(this);

    }
    isItemLoaded = index => !this.hasNextPage || index < this.items.length;


    render() {
        const { overscanByPixels } = this.state;
        return (
            <InfiniteLoader
                isItemLoaded={this.isItemLoaded}
                itemCount={this.itemCount}
                loadMoreItems={this.loadMore}>
                {({ onRowsRendered }) => (
                    <WindowScroller overscanByPixels={overscanByPixels}>
                    {this._renderAutoSizer({onRowsRendered})}
                  </WindowScroller>
                )}
            </InfiniteLoader>
        )
    }

    _calculateColumnCount() {
        const {columnWidth, gutterSize} = this.state;
    
        this._columnCount = Math.floor(this._width / (columnWidth + gutterSize));
      }
    
      _cellRenderer({index, key, parent, style}) {
        const {list} = this.context;
        const {columnWidth} = this.state;
    
        const datum = list.get(index % list.size);
    
        return (
          <CellMeasurer cache={this._cache} index={index} key={key} parent={parent}>
            <div>
              <div>
                {index}
              </div>
              {datum.random}
            </div>
          </CellMeasurer>
        );
      }
    
      _initCellPositioner() {
        if (typeof this._cellPositioner === 'undefined') {
          const {columnWidth, gutterSize} = this.state;
    
          this._cellPositioner = createCellPositioner({
            cellMeasurerCache: this._cache,
            columnCount: this._columnCount,
            columnWidth,
            spacer: gutterSize,
          });
        }
      }
    
      _onResize({width}) {
        this._width = width;
    
        this._calculateColumnCount();
        this._resetCellPositioner();
        this._masonry.recomputeCellPositions();
      }
    
      _renderAutoSizer({onRowsRendered,height, scrollTop}) {
        this._height = height;
        this._scrollTop = scrollTop;
    
        const {overscanByPixels} = this.state;
    
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
    
      _renderMasonry({width}) {
        this._width = width;
    
        this._calculateColumnCount();
        this._initCellPositioner();
    
        const {height, overscanByPixels, windowScrollerEnabled} = this.state;
    
        return (
          <Masonry
            autoHeight={windowScrollerEnabled}
            cellCount={1000}
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
    
      // This is a bit of a hack to simulate newly loaded cells
      _resetList = () => {
        const ROW_HEIGHTS = [25, 50, 75, 100];
    
        const {list} = this.context;
        list.forEach(datum => {
          datum.size = ROW_HEIGHTS[Math.floor(Math.random() * ROW_HEIGHTS.length)];
        });
    
        this._cache.clearAll();
        this._resetCellPositioner();
        this._masonry.clearCellPositions();
      };
    
      _resetCellPositioner() {
        const {columnWidth, gutterSize} = this.state;
    
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