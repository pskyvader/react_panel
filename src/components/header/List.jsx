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
        color: theme.palette.primary.dark, 
        '& span': { 
            fontWeight: theme.typography.fontWeightMedium 
        } 
    }
}));


export function NestedList(props) {
    const {element,url}=props;
    const icon = { 'icon': mui[element.icono] };
    const to = `${url}/${element.module}`;
    let match = useRouteMatch({ path: to, exact: false });
    const [open, setOpen] = React.useState((match?true:false));
  
    const handleClick = () => {
      setOpen(!open);
    };
    return (
        <Fragment>
            <ListItem button onClick={handleClick}>
                <ListItemIcon>
                    <icon.icon />
                </ListItemIcon>
                <ListItemText primary={element.titulo} />
                {open ? <ExpandLess /> : <ExpandMore />}
            </ListItem>
            <Collapse in={open} timeout="auto" unmountOnExit>
                {element.hijo.map(hijo => (
                    <ChildButton key={element.module + '-' + element.orden + '-' + hijo.tipo} element={element} hijo={hijo} unique={false}  {...props} />
                ))
                }
            </Collapse>
        </Fragment>
    );
}



export const ChildButton = ({ element, hijo, url, unique }) => {
    let to = `${url}/${element.module}`;
    if (!unique || hijo.tipo !== 0) {
        to += `/${hijo.tipo}`;
    }
    const icon = { 'icon': mui[element.icono] };

    return <ActiveLink label={hijo.titulo} to={to} unique={unique} icon={icon} activeOnlyWhenExact={false} />
}

function ActiveLink({ label, to, unique, icon, activeOnlyWhenExact }) {

    let match = useRouteMatch({
        path: to,
        exact: activeOnlyWhenExact
    });
    const classes = useStyles();
    let active = (match ? classes.ActiveLink : "");

    return (
        <ListItem className={!unique ? classes.nested+' ' + active : active} button component={Link} to={to}>
            {(unique) ? <ListItemIcon><icon.icon className={active} /></ListItemIcon> : ""}
            <ListItemText primary={label} />
        </ListItem>
    );
}
