import React, { Fragment } from 'react';
import { Link } from "react-router-dom";


import { ListItem, ListItemIcon, ListItemText, Collapse } from '@material-ui/core';
import {ExpandLess, ExpandMore } from '@material-ui/icons';

import allIconsMap from "./IconList";
import * as mui from '@material-ui/icons';

export class NestedList extends React.Component {
    constructor(props) {
        super(props);
        this.element = props.element;
        this.url = props.url;
        this.classes = props.classes;
        this.state = { open: false };
        this.icon = mui[this.element['icono']];
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
            <Fragment>
                <ListItem button onClick={this.handleClick}>
                    <ListItemIcon>
                        <this.icon />
                    </ListItemIcon>
                    <ListItemText primary={this.element.titulo} />
                    {this.state.open ? <ExpandLess /> : <ExpandMore />}
                </ListItem>
                <Collapse in={this.state.open} timeout="auto" unmountOnExit className={this.classes.nested}>
                    {this.element.hijo.map(hijo => (
                        <ChildButton key={this.element.module + '-' + this.element.orden + '-' + hijo.tipo} element={this.element} hijo={hijo} unique={false}  {...this.props}/>
                    ))
                    }
                </Collapse>
            </Fragment>
        );
    }

}



export const ChildButton = ({element, hijo, url, unique, classes}) =>{
    const to=`${url}/${element.module}`;
    const icon={'icon':mui[element.icono]};
    // console.log(allIconsMap[element['icono']],element['icono'],element['titulo'])
    return (
        <ListItem className={!unique ? classes.nested : ''} button component={Link} to={to}>
            {unique ? <ListItemIcon><icon.icon /></ListItemIcon> : ""}
            <ListItemText primary={hijo.titulo} />
        </ListItem>
    );
}



