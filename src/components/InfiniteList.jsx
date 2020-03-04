import React, { useState } from 'react';
import InfiniteLoader from "react-window-infinite-loader";
import { AutoSizer } from 'react-virtualized';
import { WindowScroller } from 'react-virtualized';
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


    // const onScroll2 = ({ clientHeight, scrollHeight, scrollTop }) => {
    //     if (scrollTop >= (scrollHeight - clientHeight) * 0.8) {
    //         if (!state.moreItemsLoading && state.hasNextPage) {
    //             let t = this;
    //             t.setState({
    //                 moreItemsLoading: true
    //             });
    //             state.loadMore(function (val) {
    //                 if (t.props.items.length !== t.state.items.length) {
    //                     t.setState({
    //                         items: t.props.items,
    //                         moreItemsLoading: t.props.moreItemsLoading,
    //                         loadMore: t.props.loadMore,
    //                         hasNextPage: t.props.hasNextPage,
    //                         itemCount: t.props.hasNextPage ? t.props.items.length + 1 : t.props.items.length
    //                     });
    //                 }
    //             });
    //         }
    //     }
    // };

    const isItemLoaded = index => !hasNextPage || index < items.length;
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
        return props.moreItemsLoading ? <LinearProgress /> : <div></div>
    }
    const _calculateColumnCount = (width) => {
        const minColumnWidth=getMinwidth(width)
        SetcolumnCount(Math.floor(width / minColumnWidth ));
    }

    const _cellRenderer = ({ columnIndex, key, rowIndex, style }) => {
        const cell = items[rowIndex];
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


    const RenderGrid = ({ width, height,onRowsRendered }) => {
        _calculateColumnCount(width);
        cellwidth(width);

        let rowCount = 1;
        rowCount = (columnCount > 0) ? Math.floor(items.length / columnCount) : 1;
        rowCount = (rowCount < 1) ? 1 : rowCount;
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
        if (gridHeight < 300) {
            gridHeight = 300;
        }

        // return null;

        return (
            <Grid
                cellRenderer={_cellRenderer}
                columnWidth={columnWidth}
                columnCount={columnCount}
                height={gridHeight}
                overscanColumnCount={0}
                overscanRowCount={0}
                rowHeight={300}
                rowCount={rowCount}
                width={width}
                onScroll={onScroll}
                onSectionRendered={onRowsRendered}
            />
        )

    }



    return (
        <InfiniteLoader
            isItemLoaded={isItemLoaded}
            itemCount={itemCount}
            loadMoreItems={loadMore}
        >
            {
                ({ onRowsRendered, ref }) => {
                    return (
                        <React.Fragment >
                            {render_progress()}
                            <WindowScroller scrollElement={window} ref={ref}>
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









