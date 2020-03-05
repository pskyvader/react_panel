import React, { useRef } from 'react';
import clsx from 'clsx';
import CssBaseline from '@material-ui/core/CssBaseline';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import { makeStyles } from '@material-ui/core/styles';

import Logo from '../Logo';
import Sidebar from './Sidebar';
import LocalStorage from '../LocalStorage';

const drawerWidth = 240;

const useStyles = makeStyles(theme => ({
    root: {
        display: 'flex',
    },
    appBar: {
        zIndex: theme.zIndex.drawer + 1,
    },
    content: {
        flexGrow: 1,
        padding: theme.spacing(3),
        transition: theme.transitions.create('margin', {
            easing: theme.transitions.easing.sharp,
            duration: theme.transitions.duration.leavingScreen,
        }),
        [theme.breakpoints.up('md')]: {
            marginLeft: -drawerWidth,
        },
        [theme.breakpoints.down('sm')]: {
            padding: theme.spacing(3,0)
        },

    },
    contentShift: {
        transition: theme.transitions.create('margin', {
            easing: theme.transitions.easing.easeOut,
            duration: theme.transitions.duration.enteringScreen,
        }),
        [theme.breakpoints.up('md')]: {
            marginLeft: 0,
        },
    },
    drawerHeader: {
        display: 'flex',
        alignItems: 'center',
        padding: theme.spacing(0, 1),
        ...theme.mixins.toolbar,
        justifyContent: 'flex-end',
    },
    menuButton: {
        marginRight: theme.spacing(2),
    }
}));


export default function Header(props) {
    var sidebar_open = LocalStorage.get('sidebar_open', false);
    const classes = useStyles();
    const [open, setOpen] = React.useState(sidebar_open);
    const mainRef = useRef();
    const drawerHeaderRef = useRef();
    const handleDrawer = () => {
        setOpen(!open);
        LocalStorage.set('sidebar_open', !open);
    }
    const toggleDrawer = (open) => event => {
        if (event.type === 'keydown' && (event.key === 'Tab' || event.key === 'Shift')) {
            return;
        }
        setOpen(open);
        LocalStorage.set('sidebar_open', open);
    };

    return (
        <div className={classes.root}>
            <CssBaseline />

            <AppBar position="fixed" className={classes.appBar} >
                <Toolbar>
                    <IconButton color="inherit" aria-label="open drawer" onClick={handleDrawer} edge="start" className={classes.menuButton} >
                        <MenuIcon />
                    </IconButton>
                    <div className={classes.menuButton} >
                        <Logo id='1' width="40" height="40" />
                    </div>
                    <Typography variant="h6" noWrap> Persistent drawer </Typography>
                </Toolbar>
            </AppBar>

            <Sidebar handleDrawer={handleDrawer} open={open} toggleDrawer={toggleDrawer} idadministrador="1" />

            <main ref={mainRef} className={clsx(classes.content, { [classes.contentShift]: open, })} >
                <div ref={drawerHeaderRef} className={classes.drawerHeader} />
                {props.children({ mainRef: mainRef, drawerHeaderRef: drawerHeaderRef })}
            </main>
        </div>
    );
}
