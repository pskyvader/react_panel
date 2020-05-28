import React, { useState } from 'react';
import { AutoSizer, Grid, WindowScroller, InfiniteLoader } from 'react-virtualized';
import LinearProgress from '@material-ui/core/LinearProgress';
import { makeStyles } from '@material-ui/core/styles';
import IconButton from '@material-ui/core/IconButton';
import OpenWithIcon from '@material-ui/icons/OpenWith';
import { sortableContainer, sortableElement } from 'react-sortable-hoc';
import arrayMove from 'array-move';
import { sortableHandle } from 'react-sortable-hoc';

import ModuleCard from './ModuleCard';
import { CreateMutation, Mutation } from '../Mutation';


const useStyles = makeStyles(theme => ({
    root: {
        boxShadow: theme.shadows[12],
        transition: theme.transitions.create('', {
            duration: theme.transitions.duration.short,
        })
    },
    movebutton: {
        position: 'absolute',
        right: theme.spacing(3),
        top: theme.spacing(3),
        zIndex: 1,
    },
    moveicon: {
        fontSize: '1.75rem'
    }
}));


const SortableList=(props)=>{

    console.log("sortable");

    const classes = useStyles();
    let columnCount = 0;
    let rowCount = 0;
    let columnWidth = 0;
    
    const [rowHeight, SetrowHeight] = useState(100);
    const [scroll_row, Setscroll_row] = useState(0);
    

    const {Setsorting, moreItemsLoading, loadMore, hasNextPage, enableDrag, config_mostrar, module, query, variables,width,height,onRowsRendered } = props;
    let { items } = props;
    let list = null;
    let currentNode = null;

    const OrderMutation = CreateMutation({ table: module, fields: '$id:ID!,$orden:Int!', input: `{id${module}:$id,orden:$orden}` });
    let update_order = Mutation({ mutationquery: OrderMutation, query, variables, mutation: 'order', Setsorting });
    const DragHandle = sortableHandle(() =>
        <IconButton aria-label="Move" className={classes.movebutton} >
            <OpenWithIcon className={classes.moveicon} />
        </IconButton>
    );


    const onScroll = ({ clientHeight, scrollHeight, scrollTop }) => {
        if (scrollHeight > clientHeight && scrollTop >= (scrollHeight - clientHeight) * 0.7 && !moreItemsLoading && hasNextPage) {
            loadMore(function (val) {
                let current_row = Math.round(rowCount - ((scrollHeight - scrollTop) / rowHeight));
                if (current_row !== scroll_row) {
                    Setscroll_row(current_row);
                }
            });
        }
    };
    
    const SortableItem = sortableElement(({ cell, style }) => {
        const needheight = (style.top === 0 && style.left === 0);
        return (
            <div style={style} tabIndex={0}>
                <DragHandle />
                <ModuleCard element={cell} config_mostrar={config_mostrar} Height={needheight ? rowHeight : null} setHeight={needheight ? SetrowHeight : null} />
            </div>
        );
    });

    const _cellRenderer = ({ columnIndex, key, rowIndex, style }) => {
        const startIndex = rowIndex * columnCount + columnIndex;
        const zindex = rowCount * columnCount - startIndex;
        const cell = items[startIndex];
        if (cell === undefined) { return null; }
        return <SortableItem disabled={!enableDrag} index={startIndex} cell={cell} key={key} style={{ ...style, zIndex: zindex }} />;
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
        const gridHeight = getHeight(height);
        console.log("render grid");
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
                rowCount={rowHeight !== 100 ? rowCount : 1}
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
                let current_row = Math.round(rowCount - (((rowHeight * rowCount) - list.state.scrollTop) / rowHeight));
                Setscroll_row(current_row);
            }
        }

        list = listInstance;
    };
    const SortableVirtualList = sortableContainer(RenderGrid);
    


    const onSortEnd = ({ oldIndex, newIndex }) => {
        if (currentNode !== null) {
            currentNode.className = currentNode.classtmp;
            currentNode = null;
        }
        if (oldIndex === newIndex) { return; }
        items = arrayMove(items, oldIndex, newIndex);

        let tmpitems = [];
        let minposition = 0;
        for (let index = Math.min(oldIndex, newIndex) - 1; index < Math.max(oldIndex, newIndex) + 1; index++) {
            if (index < 0) {
                minposition = 0;
            } else {
                minposition = (minposition === 0 || items[index]['orden'] < minposition) ? items[index]['orden'] : minposition;
                tmpitems.push(index);
            }
        }
        let update_inputs = [];
        const idtable = 'id' + module;
        tmpitems.forEach(element => {
            items[element]['orden'] = minposition;
            let input = { 'orden': minposition, 'id': items[element][idtable] };
            update_inputs.push(input);
            minposition++;
        });
        update_inputs.forEach(element => {
            update_order({ variables: element });
        });

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
}

export default SortableList;