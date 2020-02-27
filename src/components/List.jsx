import React, { Fragment } from 'react';
import { Link } from "react-router-dom";


import { ListItem, ListItemIcon, ListItemText, Collapse } from '@material-ui/core';
import { ExpandLess, ExpandMore } from '@material-ui/icons';

import * as mui from '@material-ui/icons';
import {
    makeStyles
} from '@material-ui/core/styles';
import { useRouteMatch } from "react-router-dom";


const useStyles = makeStyles(theme => ({
    nested: {
        paddingLeft: theme.spacing(9),
    },
    ActiveLink: {
        backgroundColor: theme.palette.secondary.light,
        color: theme.palette.secondary.contrastText
    }
}));


export class NestedList extends React.Component {
    constructor(props) {
        super(props);
        this.element = props.element;
        this.state = { open: false };
        this.icon = mui[this.element['icono']];
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
                <Collapse in={this.state.open} timeout="auto" unmountOnExit>
                    {this.element.hijo.map(hijo => (
                        <ChildButton key={this.element.module + '-' + this.element.orden + '-' + hijo.tipo} element={this.element} hijo={hijo} unique={false}  {...this.props} />
                    ))
                    }
                </Collapse>
            </Fragment>
        );
    }

}



export const ChildButton = ({ element, hijo, url, unique }) => {
    let to = `${url}/${element.module}`;
    if (!unique || hijo.tipo!==0) {
        to += `/${hijo.tipo}`;
    }
    const icon = { 'icon': mui[element.icono] };

    return <ActiveLink label={hijo.titulo} to={to} unique={unique} icon={icon} activeOnlyWhenExact={false} />
}


function ActiveLink({ label, to, unique,icon, activeOnlyWhenExact }) {
    let match = useRouteMatch({
      path: to,
      exact: activeOnlyWhenExact
    });
    const classes = useStyles();
    let active=(match ? classes.ActiveLink : "");
  
    return (
        <ListItem className={!unique ? classes.nested +active : active} button component={Link} to={to}>
            {(unique) ? <ListItemIcon><icon.icon /></ListItemIcon> : ""}
            <ListItemText primary={label} />
        </ListItem>
    );

  }
  



