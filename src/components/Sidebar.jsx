import React from 'react';
import Local_storage from './Local_storage';
import { useQuery } from '@apollo/react-hooks';
import { gql } from 'apollo-boost';
import ErrorLink from './ErrorLink';


import CircularProgress from '@material-ui/core/CircularProgress';

import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import Divider from '@material-ui/core/Divider';
import List from '@material-ui/core/List';
import IconButton from '@material-ui/core/IconButton';
import { useTheme } from '@material-ui/core/styles';
import Hidden from '@material-ui/core/Hidden';
import Drawer from '@material-ui/core/Drawer';

import { ChevronLeft as ChevronLeftIcon, ChevronRight as ChevronRightIcon, MoveToInbox as InboxIcon, Mail as MailIcon } from '@material-ui/icons';

import useStyles from './Styles';
import { Fragment } from 'react';



const sideList = (classes, handleDrawer, theme,list) => (

    <div className={classes.list} role="presentation" >
        <div className={classes.drawerHeader}>
            <IconButton onClick={handleDrawer}>
                {theme.direction === 'ltr' ? <ChevronLeftIcon /> : <ChevronRightIcon />}
            </IconButton>
        </div>
        <Divider />
        {console.log(list)}
        

        <List>
            {['Inbox', 'Starred', 'Send email', 'Drafts'].map((text, index) => (
                <ListItem button key={text}>
                    <ListItemIcon>{index % 2 === 0 ? <InboxIcon /> : <MailIcon />}</ListItemIcon>
                    <ListItemText primary={text} />
                </ListItem>
            ))}
        </List>

        <Divider />
        <List>
            {['All mail', 'Trash', 'Spam'].map((text, index) => (
                <ListItem button key={text}>
                    <ListItemIcon>{index % 2 === 0 ? <InboxIcon /> : <MailIcon />}</ListItemIcon>
                    <ListItemText primary={text} />
                </ListItem>
            ))}
        </List>
    </div>

)



const SidebarMenu = (props, list) => {
    const handleDrawer = props.handleDrawer;
    const toggleDrawer = props.toggleDrawer;
    const open = props.open;
    const theme = useTheme();
    const classes = useStyles();

    return (
        <Fragment>
            <Hidden smDown>
                <Drawer className={classes.drawer} variant="persistent" open={open} classes={{ paper: classes.drawerPaper, }}>
                    {sideList(classes, handleDrawer, theme, list)}
                </Drawer>
            </Hidden>

            <Hidden mdUp>
                <Drawer variant="temporary" open={open} classes={{ paper: classes.drawerPaper, }} onClose={toggleDrawer(false)}>
                    {sideList(classes, handleDrawer, theme, list)}
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
    if (loading) return <CircularProgress />;
    if (error) return ErrorLink(error);
    cache['allModule'] = data.allModule;
    Local_storage.set(url_cache, cache);
    return SidebarMenu(props,cache['allModule']);
}


function Sidebar(props) {
    const url_cache = 'get_all_module_id_' + props.idadministrador;
    var cache = Local_storage.get(url_cache, { 'allModule': [] });
    if (cache['allModule'].length > 0) {
        return SidebarMenu(props,cache['allModule'])
    } else {
        return Sidebar_cache(props, cache, url_cache);
    }
}

export default Sidebar;