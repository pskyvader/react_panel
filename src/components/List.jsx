import React, { Fragment } from 'react';
import { Link, useRouteMatch } from "react-router-dom";


import { CircularProgress, ListItem, ListItemIcon, ListItemText, ListSubheader, Collapse, Divider, List, IconButton, Hidden, Drawer } from '@material-ui/core';
import { ChevronLeft as ChevronLeftIcon, ChevronRight as ChevronRightIcon, ExpandLess, ExpandMore } from '@material-ui/icons';

import allIconsMap from "./IconList";

class NestedList extends React.Component {
    constructor(props) {
        super(props);
        this.element = props.element;
        this.url = props.url;
        this.classes = props.classes;
        this.state = { open: false };
        this.icon = allIconsMap[this.element['icono']];
        // console.log('icono',this.icon);
    }
    handleClick = () => {
        this.setOpen(!this.state.open);
    };

    setOpen = (o) => {
        this.setState({
            open: o
        });
    }

    render() {
        return (
            <Fragment key={this.element.module + '-' + this.element.orden}>
                <ListItem button onClick={this.handleClick}>
                    <ListItemIcon>
                        <this.icon.Icon />
                    </ListItemIcon>
                    <ListItemText primary={this.element.titulo} />
                    {this.state.open ? <ExpandLess /> : <ExpandMore />}
                </ListItem>
                <Collapse in={this.state.open} timeout="auto" unmountOnExit>
                    {this.element.hijo.map(hijo => (
                        child_button(this.element, hijo, this.url, false, this.classes, this.icon)
                    ))
                    }
                </Collapse>
            </Fragment>
        );
    }

}



const child_button = (element, hijo, url, unique, classes, icon) => (
    <ListItem className={!unique ? classes.nested : ''} button component={Link} to={`${url}/${element.module}`} key={element.module + '-' + element.orden + '-' + hijo.tipo}>
        {/* {console.log(allIconsMap[element['icono']],element['icono'],element['titulo'])} */}
        {unique ? <ListItemIcon><icon.Icon /></ListItemIcon> : ""}
        <ListItemText primary={hijo.titulo} />
    </ListItem>
)