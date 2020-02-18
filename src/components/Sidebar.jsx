import React, { Fragment } from 'react';
import Local_storage from './Local_storage';
import { useQuery } from '@apollo/react-hooks';
import { gql } from 'apollo-boost';
import ErrorLink from './ErrorLink';
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
    }
    componentDidMount() {
    }

    componentWillUnmount() {
    }

    handleClick = () => {
        this.setOpen(!this.state.open);
    };

    setOpen = (o) => {
        this.setState({
            open: o
        });
    }

    // console.log('icono',icon);
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
                <List subheader={
                    sublist[0].module === 'separador' ?
                        <ListSubheader component="div" key={"separador-" + sublist[0].orden}> {sublist[0].titulo} </ListSubheader> :
                        ""}
                >

                    {sublist.map((element) => (
                        (element.module !== 'separador') ? (element.hijo.length === 1) ?
                            child_button(element, element.hijo[0], url, true, classes, allIconsMap[element['icono']]) :
                            <NestedList key={'sidebar-list' + element['orden']} element={element} url={url} classes={classes} /> : ""
                    )
                    )}

                </List>
                <Divider />
            </Fragment>
        ))}

    </div>

)



const SidebarMenu = (props, list, path, url) => {
    const { handleDrawer, toggleDrawer, open, classes, theme } = props;

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



function Sidebar_cache(props, cache, url_cache, path, url) {
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

    // Local_storage.set(url_cache, cache);
    return SidebarMenu(props, cache['allModule'], path, url);
}


function Sidebar(props) {
    let { path, url } = useRouteMatch();
    const url_cache = 'get_all_module_id_' + props.idadministrador;
    var cache = Local_storage.get(url_cache, { 'allModule': [] });
    if (cache['allModule'].length > 0) {
        return SidebarMenu(props, cache['allModule'], path, url)
    } else {
        return Sidebar_cache(props, cache, url_cache, path, url);
    }
}

export default Sidebar;