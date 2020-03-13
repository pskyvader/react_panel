import React, { useState } from 'react';
import { AutoSizer, Grid, WindowScroller, InfiniteLoader } from 'react-virtualized';
import ModuleCard from './ModuleCard';
import LinearProgress from '@material-ui/core/LinearProgress';
import { sortableContainer, sortableElement } from 'react-sortable-hoc';
import arrayMove from 'array-move';
import { makeStyles } from '@material-ui/core/styles';

import IconButton from '@material-ui/core/IconButton';
import { sortableHandle } from 'react-sortable-hoc';
import OpenWithIcon from '@material-ui/icons/OpenWith';

const useStyles = makeStyles(theme => ({
    root: {
        boxShadow: theme.shadows[12],
        transition: theme.transitions.create('', {
            duration: theme.transitions.duration.short,
        })
    },
    movebutton:{
        position:'absolute',
        right:theme.spacing(3),
        top:theme.spacing(3),
        zIndex:1,
    },
    moveicon:{
        fontSize:'1.75rem'
    }
}));





const InfiniteList = (props) => {
    const classes = useStyles();
    const minWidth = 275;
    const minWidthlg = 320;
    const maxWidth = 375;
    const scrollbarSize = 20;
    const [columnCount, SetcolumnCount] = useState(0);
    const [rowCount, SetrowCount] = useState(0);
    const [columnWidth, SetcolumnWidth] = useState(0);
    const [rowHeight, SetrowHeight] = useState(100);
    const [scroll_row, Setscroll_row] = useState(0);

    const { moreItemsLoading, loadMore, hasNextPage, enableDrag,config_mostrar } = props;
    let { items } = props;
    let list = null;
    let currentNode = null;

    
    const DragHandle = sortableHandle(() =>
        <IconButton aria-label="Move" className={classes.movebutton} >  
        <OpenWithIcon  className={classes.moveicon}/>
        </IconButton>
    );


    
    const onScroll = ({ clientHeight, scrollHeight, scrollTop }) => {
        if (scrollHeight > clientHeight && scrollTop >= (scrollHeight - clientHeight) * 0.7 && !moreItemsLoading && hasNextPage) {
            loadMore(function(val){
                let current_row=Math.round(rowCount-((scrollHeight-scrollTop)/rowHeight));
                if (current_row!==scroll_row){
                    Setscroll_row(current_row);
                }
            });
        }
    };

    const isItemLoaded = ({ index }) => !hasNextPage || index < items.length;
    const itemCount = hasNextPage ? items.length + 1 : items.length;
    const getMinwidth = (width) => width < 1280 ? minWidth : minWidthlg;
    const calculateColumnCount = (width) => {
        let column_count = Math.floor((width - scrollbarSize) / getMinwidth(width));
        if (column_count !== columnCount) {
            SetcolumnCount(column_count);
        }
    }

    const cellwidth = (width) => {
        let cell_width = 0;
        if (width !== 0 && columnCount !== 0) {
            cell_width = Math.floor((width - scrollbarSize) / columnCount);
        }
        if (cell_width < getMinwidth(width)) {
            cell_width = getMinwidth(width);
        } else if (cell_width > maxWidth && width >= 768) {
            cell_width = maxWidth;
        }

        if (cell_width !== columnWidth) {
            SetcolumnWidth(cell_width);
        }
    }

    const calculateRowCount = () => {
        let row_count = 1;
        row_count = (columnCount > 0) ? Math.floor(items.length / columnCount) : 1;
        row_count = (row_count < 1) ? 1 : row_count;
        if (row_count !== rowCount) {
            SetrowCount(row_count);
        }
    }


    const SortableItem = sortableElement(({ cell, style }) => {
        return (
            <div style={style} tabIndex={0}>
                <DragHandle />
                <ModuleCard element={cell} config_mostrar={config_mostrar} Height={rowHeight} setHeight={SetrowHeight} />
            </div>
        );
    });

    const _cellRenderer = ({ columnIndex, key, rowIndex, style }) => {
        const startIndex = rowIndex * columnCount + columnIndex;
        const zindex = rowCount * columnCount - startIndex;
        const cell = items[startIndex];
        if (cell === undefined) { return null; }
        // return <div key={key} style={{ ...style, zIndex: zindex }}>asdfasdf</div>
        return <SortableItem disabled={!enableDrag} index={startIndex} cell={cell} key={key} style={{ ...style, zIndex: zindex}} />;
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
        const { width, height, onRowsRendered, getRef } = props;
        calculateColumnCount(width);
        cellwidth(width);
        calculateRowCount();

        const gridHeight = getHeight(height);
        return (
            <Grid
                ref={getRef}
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
                scrollToRow={scroll_row}
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

    const registerListRef = (listInstance) => {
        if (list !== null) {
            if (list.state.scrollTop !== 0) {
                let current_row=Math.round(rowCount-(((rowHeight*rowCount)-list.state.scrollTop)/rowHeight));
                Setscroll_row(current_row);
            }
        }

        list = listInstance;
    };
    const SortableVirtualList = sortableContainer(RenderGrid);
    const _onResize = ({ width }) => { calculateColumnCount(width); cellwidth(width); }


    const onSortEnd = ({ oldIndex, newIndex }) => {
        if (currentNode !== null) {
            currentNode.className = currentNode.classtmp;
            currentNode = null;
        }
        if (oldIndex === newIndex) { return; }
        items = arrayMove(items, oldIndex, newIndex);

        let tmpitems=[];
        let minposition=0;
        for (let index = Math.min(oldIndex,newIndex)-1; index <  Math.max(oldIndex,newIndex)+1; index++) {
            if (index<0){
                minposition=0;
            }else{
                minposition=(minposition===0 || items[index]['orden']<minposition)?items[index]['orden']:minposition;
                tmpitems.push(items[index]);
            }
        }
        console.log(tmpitems,minposition);


        if (list !== null) {
            // list.recomputeGridSize();
            list.forceUpdate();
        }
    };
    const updateBeforeSortStart = ({ node }) => {
        currentNode = node.children[1];
        currentNode.classtmp = currentNode.className;
        currentNode.className += " " + classes.root;
    }

    const _renderAutoSizer = ({ height, onRowsRendered }) => {
        return (
            <AutoSizer
                disableHeight
                height={height}
                onResize={_onResize}>
                {({ width }) => {
                    return <SortableVirtualList
                        getRef={registerListRef}
                        items={items}
                        onSortEnd={onSortEnd}
                        width={width}
                        height={height}
                        onRowsRendered={onRowsRendered}
                        axis="xy"
                        pressDelay={0}
                        updateBeforeSortStart={updateBeforeSortStart}
                        useDragHandle={true}
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
                            {moreItemsLoading ? <LinearProgress /> : <div></div>}
                            <WindowScroller scrollElement={window} ref={registerChild}>
                                {({ height }) => (_renderAutoSizer({ height, onRowsRendered }))}
                            </WindowScroller>
                        </React.Fragment>
                    )
                }
            }
        </InfiniteLoader>
    )

}
export default InfiniteList;