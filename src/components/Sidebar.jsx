import React, { Fragment } from 'react';
import Local_storage from './Local_storage';
import { useQuery } from '@apollo/react-hooks';
import { gql } from 'apollo-boost';
import ErrorLink from './ErrorLink';
import { Link, useRouteMatch } from "react-router-dom";

import { CircularProgress, ListItem, ListItemIcon, ListItemText, Divider, List, IconButton, Hidden, Drawer } from '@material-ui/core';
import { ChevronLeft as ChevronLeftIcon, ChevronRight as ChevronRightIcon, MoveToInbox as InboxIcon, Mail as MailIcon } from '@material-ui/icons';




const child_button = (element, hijo, url) => (
    <ListItem button component={Link} to={`${url}/${element.module}`} key={element.module + element.orden + hijo.tipo}>
        

        <ListItemText primary={hijo.titulo} />
    </ListItem>
)

const sideList = (classes, handleDrawer, theme, final_list, path, url) => (
    <div className={classes.list} role="presentation" >
        <div className={classes.drawerHeader}>
            <IconButton onClick={handleDrawer}>
                {theme.direction === 'ltr' ? <ChevronLeftIcon /> : <ChevronRightIcon />}
            </IconButton>
        </div>
        <Divider />
        {final_list.map((sublist, index) => (
            <Fragment key={'sidebar_list' + index}>
                <List>
                    {sublist.forEach((element) => {
                        if (element.module === 'separador') {
                            return (
                                <ListItem key={element.module + element.orden}>
                                    <ListItemText primary={element.titulo} />
                                </ListItem>
                            )
                        } else {
                            if (element.hijo.length === 1) {
                                return child_button(element, element.hijo, url);
                            }else{
                                
                            }
                        }
                    }
                    )}
                </List>
                <Divider />
            </Fragment>
        ))}

    </div>

)



const SidebarMenu = (props, list) => {
    const handleDrawer = props.handleDrawer;
    const toggleDrawer = props.toggleDrawer;
    const open = props.open;
    const classes = props.classes;
    const theme = props.theme;
    let { path, url } = useRouteMatch();
    if (url === '/') url = '';

    const super_list = [];
    let new_list = [];
    list.forEach(element => {
        if (element['module'] === 'separador') {
            super_list.push(new_list);
            new_list = [];
        }
        new_list.push(element);
    });
    if (new_list.length > 0) {
        super_list.push(new_list);
    }

    return (
        <Fragment>
            <Hidden smDown>
                <Drawer className={classes.drawer} variant="persistent" open={open} classes={{ paper: classes.drawerPaper, }}>
                    {sideList(classes, handleDrawer, theme, super_list, path, url)}
                </Drawer>
            </Hidden>

            <Hidden mdUp>
                <Drawer variant="temporary" open={open} classes={{ paper: classes.drawerPaper, }} onClose={toggleDrawer(false)}>
                    {sideList(classes, handleDrawer, theme, super_list, path, url)}
                </Drawer>
            </Hidden>
        </Fragment>
    );
}



function Sidebar_cache(props, cache, url_cache) {
    const GET_MODULES = gql`
    query get_all_module ($idadministrador:Int!){
        allModule(idadministrador:$idadministrador){
            icono
            module
            titulo
            orden
            estado
            aside
            tipos
            hijo{
                tipo
                titulo
                orden
                aside
            }
        }
    }`;

    const variables = { variables: { idadministrador: props.idadministrador }, };
    const { loading, error, data } = useQuery(GET_MODULES, variables);
    if (loading) {
        return <CircularProgress />
    }
    if (error) return ErrorLink(error);
    cache['allModule'] = data.allModule;
    Local_storage.set(url_cache, cache);
    return SidebarMenu(props, cache['allModule']);
}


function Sidebar(props) {
    const url_cache = 'get_all_module_id_' + props.idadministrador;
    var cache = Local_storage.get(url_cache, { 'allModule': [] });
    if (cache['allModule'].length > 0) {
        return SidebarMenu(props, cache['allModule'])
    } else {
        return Sidebar_cache(props, cache, url_cache);
    }
}

export default Sidebar;