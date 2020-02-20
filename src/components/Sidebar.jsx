import React, { Fragment } from 'react';
import { useQuery } from '@apollo/react-hooks';
import { gql } from 'apollo-boost';
import { useRouteMatch } from "react-router-dom";
import { useTheme ,makeStyles} from '@material-ui/core/styles';
import { CircularProgress, ListSubheader, Divider, List, IconButton, Hidden, Drawer } from '@material-ui/core';
import { ChevronLeft as ChevronLeftIcon, ChevronRight as ChevronRightIcon } from '@material-ui/icons';

import { NestedList, ChildButton } from "./List";
import ErrorLink from './ErrorLink';
import LocalStorage from './LocalStorage';

const drawerWidth = 240;

const useStyles = makeStyles(theme => ({
    drawer: {
        width: drawerWidth,
        flexShrink: 0,
    },
    drawerPaper: {
        width: drawerWidth,
    },

    drawerHeader: {
        display: 'flex',
        alignItems: 'center',
        padding: theme.spacing(0, 1),
        ...theme.mixins.toolbar,
        justifyContent: 'flex-end',
    },
}));


const SideList = (props) => {
    const { handleDrawer, list } = props;
    const classes = useStyles();
    const theme = useTheme();
    return (
        <div className={classes.list} role="presentation" >
            <div className={classes.drawerHeader}>
                <IconButton onClick={handleDrawer}>
                    {theme.direction === 'ltr' ? <ChevronLeftIcon /> : <ChevronRightIcon />}
                </IconButton>
            </div>
            <Divider />
            {list.map((sublist, index) => (
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
                                    <NestedList  {...props} key={element.module + '-' + element.orden} element={element} />
                            ) : ""
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
    const { toggleDrawer, open, list } = props;
    const classes = useStyles();
    let { url } = props;

    if (url === '/') url = '';


    return (
        <Fragment>
            <Hidden smDown>
                <Drawer className={classes.drawer} variant="persistent" open={open} classes={{ paper: classes.drawerPaper, }}>
                    <SideList  {...props} list={list} url={url} />
                </Drawer>
            </Hidden>

            <Hidden mdUp>
                <Drawer variant="temporary" open={open} classes={{ paper: classes.drawerPaper, }} onClose={toggleDrawer(false)}>
                    <SideList {...props} list={list} url={url} />
                </Drawer>
            </Hidden>
        </Fragment>
    );
}



function SidebarCache(props) {
    const { url_cache } = props;
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

    const super_list = [];
    let new_list = [];
    data.allModule.forEach(element => {
        if (element['module'] === 'separador') {
            super_list.push(new_list);
            new_list = [];
        }
        new_list.push(element);
    });
    if (new_list.length > 0) {
        super_list.push(new_list);
    }
    LocalStorage.set(url_cache, super_list);

    return <SidebarMenu {...props} list={super_list} />
}


function Sidebar(props) {
    let { path, url } = useRouteMatch();
    const url_cache = 'get_all_module_id_' + props.idadministrador;
    var cache = LocalStorage.get(url_cache, []);
    if (cache.length > 0) {
        return <SidebarMenu {...props} list={cache} path={path} url={url} />
    } else {
        return <SidebarCache {...props} url_cache={url_cache} path={path} url={url} />
    }
}

export default Sidebar;