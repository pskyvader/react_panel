import React, { Fragment } from 'react';
import LocalStorage from './LocalStorage';
import { useQuery } from '@apollo/react-hooks';
import { gql } from 'apollo-boost';
import ErrorLink from './ErrorLink';
import { useRouteMatch } from "react-router-dom";

import { CircularProgress, ListSubheader, Divider, List, IconButton, Hidden, Drawer } from '@material-ui/core';
import { ChevronLeft as ChevronLeftIcon, ChevronRight as ChevronRightIcon } from '@material-ui/icons';

import {NestedList,ChildButton} from "./List";


const SideList = (props) =>{
 const {classes, handleDrawer, theme, final_list}=props;
return (
    <div className={classes.list} role="presentation" >
        <div className={classes.drawerHeader}>
            <IconButton onClick={handleDrawer}>
                {theme.direction === 'ltr' ? <ChevronLeftIcon /> : <ChevronRightIcon />}
            </IconButton>
        </div>
        <Divider />
        {final_list.map((sublist, index) => (
            <Fragment key={'sidebar_list' + index}>
                <List subheader={
                    sublist[0].module === 'separador' ?
                        <ListSubheader component="div" key={"sidebar-separador-" + sublist[0].orden}> {sublist[0].titulo} </ListSubheader> :
                        ""}
                >

                    {sublist.map((element) => (
                        (element.module !== 'separador') ? (
                            (element.hijo.length === 1) ?
                            <ChildButton {...props} key={element.module + '-' + element.orden + '-' + element.hijo[0].tipo} element={element} hijo={element.hijo[0]} unique={true} /> :
                            <NestedList  {...props} key={element.module + '-' + element.orden} element={element}/> 
                        ): ""
                    )
                    )}

                </List>
                <Divider />
            </Fragment>
        ))}

    </div>

)
} 



const SidebarMenu = (props) => {
    const { toggleDrawer, open, classes, list} = props;
    let {url}=props;

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
                    <SideList  {...props} final_list={super_list} url={url}/>
                </Drawer>
            </Hidden>

            <Hidden mdUp>
                <Drawer variant="temporary" open={open} classes={{ paper: classes.drawerPaper, }} onClose={toggleDrawer(false)}>
                    <SideList {...props} final_list={super_list} url={url} />
                </Drawer>
            </Hidden>
        </Fragment>
    );
}



function SidebarCache(props) {
    const {cache, url_cache}=props;
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
    if (loading) return <CircularProgress />
    if (error) return ErrorLink(error);
    cache['allModule'] = data.allModule;
    LocalStorage.set(url_cache, cache);
    return <SidebarMenu {...props} list={cache['allModule']}/>
}


function Sidebar(props) {
    let { path, url } = useRouteMatch();
    const url_cache = 'get_all_module_id_' + props.idadministrador;
    var cache = LocalStorage.get(url_cache, { 'allModule': [] });
    if (cache['allModule'].length > 0) {
        return <SidebarMenu {...props} list={cache['allModule']} path={path} url={url}/>
    } else {
        return <SidebarCache {...props} cache={cache} url_cache={url_cache} path={path} url={url}/>
    }
}

export default Sidebar;