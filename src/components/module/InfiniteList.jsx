import React, { useState } from 'react';
import { AutoSizer, WindowScroller, InfiniteLoader } from 'react-virtualized';
import LinearProgress from '@material-ui/core/LinearProgress';
import SortableList from "./SortableList";

const InfiniteList = (props) => {
    const minWidth = 275;
    const minWidthlg = 320;
    const maxWidth = 375;
    const scrollbarSize = 20;
    let columnCount = 0;
    let rowCount = 0;
    let columnWidth = 0;
    let current_width = 0;
    const [resizing, Setresizing] = useState(false);
    const [sorting, Setsorting] = useState(false);
    const { moreItemsLoading, loadMore, hasNextPage } = props;
    let { items } = props;

    const stop_render = (width = 1) => {
        if (sorting || moreItemsLoading || columnCount === 0 || rowCount === 0 || columnWidth === 0 || width === 0 || resizing) {
            return true;
        }
        return false;
    }


    const isItemLoaded = ({ index }) => !hasNextPage || index < items.length;
    const itemCount = hasNextPage ? items.length + 1 : items.length;
    const getMinwidth = (width) => width < 1280 ? minWidth : minWidthlg;
    const calculateColumnCount = (width) => {
        let column_count = Math.floor((width - scrollbarSize) / getMinwidth(width));
        if (column_count !== columnCount) {
            columnCount = column_count;
        }
    }

    const cellwidth = (width) => {
        let cell_width =(width !== 0 && columnCount !== 0)? Math.floor((width - scrollbarSize) / columnCount):0;
        if (cell_width < getMinwidth(width)) {
            cell_width = getMinwidth(width);
        } else if (cell_width > maxWidth && width >= 768) {
            cell_width = maxWidth;
        }

        if (cell_width !== columnWidth) {
            columnWidth = cell_width;
        }
    }

    const calculateRowCount = () => {
        let row_count = 1;
        row_count = (columnCount > 0) ? Math.floor(items.length / columnCount) : 1;
        row_count = (row_count < 1) ? 1 : row_count;
        if (row_count !== rowCount) {
            rowCount = row_count;
        }
    }

    const _onResize = ({ width }) => {
        if (width > 0 && columnCount === 0) {
            calculateColumnCount(width);
        }
    }

    const is_resizing = (width) => {
        if (current_width === 0) {
            current_width = width;
        } else if (width !== current_width) {
            current_width = width;
            if (!resizing) {
                Setresizing(true);
                setTimeout(() => {
                    Setresizing(false);
                }, 300);
            }
        }

    }

    const _renderAutoSizer = ({ height, onRowsRendered }) => {
        return (
            <AutoSizer
                disableHeight
                height={height}
                onResize={_onResize}>
                {({ width }) => {
                    calculateColumnCount(width);
                    cellwidth(width);
                    calculateRowCount();
                    is_resizing(width);
                    if (stop_render(width)) {
                        return ''
                    } else return <SortableList
                        columnWidth={columnWidth}
                        columnCount={columnCount}
                        rowCount={rowCount}
                        Setsorting={Setsorting}
                        width={width}
                        height={height}
                        onRowsRendered={onRowsRendered}
                        {...props}
                    />
                }}
            </AutoSizer>
        );
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
                            {moreItemsLoading || sorting ? <LinearProgress /> : <div></div>}
                            <WindowScroller scrollElement={window} ref={registerChild}>
                                {({ height }) => (_renderAutoSizer({ height, onRowsRendered }))}
                            </WindowScroller>
                        </React.Fragment>
                    )
                }
            }
        </InfiniteLoader>
    );
}
export default InfiniteList;