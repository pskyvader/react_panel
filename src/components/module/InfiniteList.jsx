import React, { useState } from 'react';
import { AutoSizer,Grid ,WindowScroller,InfiniteLoader} from 'react-virtualized';
import ModuleCard from './ModuleCard';
import LinearProgress from '@material-ui/core/LinearProgress';
import {sortableContainer, sortableElement} from 'react-sortable-hoc';
import arrayMove from 'array-move';




const InfiniteList = (props) => {
    const minWidth = 275;
    const minWidthlg = 320;
    const maxWidth = 375;
    const scrollbarSize = 20;

    const { items, moreItemsLoading, loadMore, hasNextPage } = props;
    const [columnCount, SetcolumnCount] = useState(0);
    const [rowCount, SetrowCount] = useState(0);
    const [columnWidth, SetcolumnWidth] = useState(0);
    const [rowHeight, SetrowHeight] = useState(100);
    const [list, Setlist] = useState(null);

    const isItemLoaded = ({ index }) => {
        return !hasNextPage || index < items.length
    };
    const itemCount = hasNextPage ? items.length + 1 : items.length;

    const onScroll = ({ clientHeight, scrollHeight, scrollTop }) => {
        if (scrollTop >= (scrollHeight - clientHeight) * 0.7) {
            if (!moreItemsLoading && hasNextPage) {
                loadMore();
            }
        }
    };

    const getMinwidth = (width) => {
        return width < 1280 ? minWidth : minWidthlg;
    }

    const cellwidth = (width) => {
        let cell_width = 0;
        if (width !== 0 && columnCount !== 0) {
            cell_width = Math.floor((width-scrollbarSize) / columnCount);
        }
        if (cell_width < getMinwidth(width)) {
            cell_width = getMinwidth(width);
        } else if (cell_width > maxWidth && width>=768) {
            cell_width = maxWidth;
        }

        SetcolumnWidth(cell_width);
    }

    const render_progress = () => {
        return moreItemsLoading ? <LinearProgress /> : <div></div>
    }
    const calculateColumnCount = (width) => {
        const minColumnWidth = getMinwidth(width)
        SetcolumnCount(Math.floor((width-scrollbarSize) / minColumnWidth));
    }
    const calculateRowCount = () => {
        let rowCount = 1;
        rowCount = (columnCount > 0) ? Math.floor(items.length / columnCount) : 1;
        rowCount = (rowCount < 1) ? 1 : rowCount;
        SetrowCount(rowCount);
    }

    const _cellRenderer = ({ columnIndex, key, rowIndex, style }) => {
        const startIndex = rowIndex * columnCount + columnIndex;
        const zindex=rowCount*columnCount-startIndex;

        const cell = items[startIndex];
        if (cell===undefined){
            return null;
        }
        
        return <SortableItem index={startIndex} cell={cell} key={key} style={{...style,zIndex:zindex}}/>;

        return (
            <div key={key} style={{...style,zIndex:zindex}}>
                <ModuleCard element={cell} Height={rowHeight} setHeight={SetrowHeight}  />
            </div>
        );
    }

    const SortableItem = sortableElement(({cell,style}) => {
        return (
            <div style={style}>
                <ModuleCard element={cell} Height={rowHeight} setHeight={SetrowHeight}  />
            </div>
        );
      });


    const _onResize = ({ width }) => {
        // SetrowHeight(100);
        calculateColumnCount(width);
        cellwidth(width);
    }

    const onSortEnd = ({oldIndex, newIndex}) => {
        if (oldIndex === newIndex) {
          return;
        }
    
        let {items} = props;
    
          items= arrayMove(items, oldIndex, newIndex);
    
        // We need to inform React Virtualized that the items have changed heights
        // This can either be done by imperatively calling the recomputeRowHeights and
        // forceUpdate instance methods on the `List` ref, or by passing an additional prop
        // to List that changes whenever the order changes to force it to re-render
        list.recomputeRowHeights();
        list.forceUpdate();
      };

      
      const registerListRef = (listInstance) => {
        Setlist(listInstance);
      };

    const _renderAutoSizer = ({ height, scrollTop, onRowsRendered }) => {



        return (
            <AutoSizer
                disableHeight
                height={height}
                onResize={_onResize}
                scrollTop={scrollTop}>
                {({ width }) => {
                    // return  RenderGrid({ width, height, onRowsRendered })
                    return <SortableVirtualList
                    getRef={registerListRef}
                    items={items}
                    onSortEnd={onSortEnd}
                    width={width}
                    height={height}
                    onRowsRendered={onRowsRendered}
                  />
                
                    }
                
                }
            </AutoSizer>
        );
    }

    const getHeight = (height) => {
        let height1 = props.TypographyRef.current.offsetHeight;
        const height2 = props.drawerHeaderRef.current.offsetHeight;

        let nodeStyle1 = window.getComputedStyle(props.TypographyRef.current);
        let slideMarginRight1 = nodeStyle1.getPropertyValue('margin-bottom');
        height1 += parseFloat(slideMarginRight1);

        let nodeStyle = window.getComputedStyle(props.mainRef.current);
        let slideMarginRight = nodeStyle.getPropertyValue('padding-top');

        const height3 = parseInt(slideMarginRight) * 2;
        const height4 = 4; //loader

        let gridHeight = height - (height1 + height2 + height3 + height4);
        if (gridHeight < 350) {
            gridHeight = 350;
        }
        return gridHeight;
    }


    const RenderGrid = (props) => {
        const { width, height, onRowsRendered }=props;
        calculateColumnCount(width);
        cellwidth(width);
        calculateRowCount();

        const gridHeight = getHeight(height);


        return (
            <Grid
                cellRenderer={_cellRenderer}
                columnWidth={columnWidth}
                columnCount={columnCount}
                height={gridHeight}
                overscanColumnCount={0}
                overscanRowCount={0}
                rowHeight={rowHeight}
                rowCount={rowCount}
                width={width}
                onScroll={onScroll}
                onSectionRendered={
                    ({ columnStartIndex, columnStopIndex, rowStartIndex, rowStopIndex }) => {
                        const startIndex = rowStartIndex * columnCount + columnStartIndex;
                        const stopIndex = rowStopIndex * columnCount + columnStopIndex;
                        return onRowsRendered({ startIndex, stopIndex });
                    }
                }
            />
        )

    }

    
    const SortableVirtualList = sortableContainer(RenderGrid);




    return (
        <InfiniteLoader
            isRowLoaded={isItemLoaded}
            loadMoreRows={loadMore}
            rowCount={itemCount}
        >
            {
                ({ onRowsRendered, registerChild }) => {
                    return (
                        <React.Fragment >
                            {render_progress()}
                            <WindowScroller scrollElement={window} ref={registerChild}>
                                {({ height, isScrolling, registerChild, onChildScroll, scrollTop }) => (
                                    _renderAutoSizer({ height, isScrolling, registerChild, onChildScroll, scrollTop, onRowsRendered })
                                )}

                            </WindowScroller>
                        </React.Fragment>
                    )

                }
            }
        </InfiniteLoader>
    )

}



export default InfiniteList;









