import React, { useState } from 'react';
import { AutoSizer } from 'react-virtualized';
import { WindowScroller } from 'react-virtualized';
import { InfiniteLoader } from 'react-virtualized';
import ModuleCard from './ModuleCard';
import LinearProgress from '@material-ui/core/LinearProgress';
import { Grid } from 'react-virtualized';




const InfiniteList = (props) => {
    const minWidth = 245;
    const minWidthlg = 290;
    const maxWidth = 345;

    const { items, moreItemsLoading, loadMore, hasNextPage } = props;
    const [columnCount, SetcolumnCount] = useState(0);
    const [columnWidth, SetcolumnWidth] = useState(0);

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
            cell_width = Math.floor(width / columnCount);
        }
        if (cell_width < getMinwidth(width)) {
            cell_width = getMinwidth(width);
        } else if (cell_width > maxWidth) {
            cell_width = maxWidth;
        }

        SetcolumnWidth(cell_width);
    }

    const render_progress = () => {
        return moreItemsLoading ? <LinearProgress /> : <div></div>
    }
    const _calculateColumnCount = (width) => {
        const minColumnWidth = getMinwidth(width)
        SetcolumnCount(Math.floor(width / minColumnWidth));
    }

    const _cellRenderer = ({ columnIndex, key, rowIndex, style }) => {
        const startIndex = rowIndex * columnCount + columnIndex;
        console.log(columnIndex, key, rowIndex, style,startIndex);
        const cell = items[startIndex];
        return (
            <div key={key} style={style}>
                <ModuleCard element={cell} />
            </div>
        );
    }


    const _onResize = ({ width }) => {
        _calculateColumnCount(width);
        cellwidth(width);
    }

    const _renderAutoSizer = ({ height, scrollTop, onRowsRendered }) => {
        return (
            <AutoSizer
                disableHeight
                height={height}
                onResize={_onResize}
                scrollTop={scrollTop}>
                {({ width }) => (
                    RenderGrid({ width, height, onRowsRendered })
                )}
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
        if (gridHeight < 250) {
            gridHeight = 250;
        }
        return gridHeight;
    }


    const RenderGrid = ({ width, height, onRowsRendered }) => {
        _calculateColumnCount(width);
        cellwidth(width);

        let rowCount = 1;
        rowCount = (columnCount > 0) ? Math.floor(items.length / columnCount) : 1;
        rowCount = (rowCount < 1) ? 1 : rowCount;

        const gridHeight = getHeight(height);


        return (
            <Grid
                cellRenderer={_cellRenderer}
                columnWidth={columnWidth}
                columnCount={columnCount}
                height={gridHeight}
                overscanColumnCount={0}
                overscanRowCount={0}
                rowHeight={500}
                rowCount={rowCount}
                width={width}
                onScroll={onScroll}
                onSectionRendered={
                    ({ columnStartIndex, columnStopIndex, rowStartIndex, rowStopIndex }) => {
                        const startIndex = rowStartIndex * columnCount + columnStartIndex
                        const stopIndex = rowStopIndex * columnCount + columnStopIndex
                        onRowsRendered({
                            startIndex,
                            stopIndex
                        })
                    }
                }
            />
        )

    }



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









