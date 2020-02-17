import React from 'react';
import clsx from 'clsx';
import CssBaseline from '@material-ui/core/CssBaseline';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import { useTheme } from '@material-ui/core/styles';

import Logo from './Logo';
import useStyles from './Styles';
import Sidebar from './Sidebar';


export default function Header(props) {
    const classes = useStyles();
    const theme = useTheme();
    const [open, setOpen] = React.useState(false);
    const handleDrawer = () => {
        setOpen(!open);
    }
    const toggleDrawer = (open) => event => {
        if (event.type === 'keydown' && (event.key === 'Tab' || event.key === 'Shift')) {
            return;
        }
        setOpen(open);
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
                    <Logo id='1' width="40" height="40"/></div>
                    <Typography variant="h6" noWrap> Persistent drawer </Typography>
                </Toolbar>
            </AppBar>
            
            <Sidebar handleDrawer={handleDrawer} open={open} toggleDrawer={toggleDrawer} idadministrador="1" theme={theme} classes={classes}/>

            <main className={clsx(classes.content, { [classes.contentShift]: open, })} >
                <div className={classes.drawerHeader} />
                {props.children}
            </main>
        </div>
    );
}
