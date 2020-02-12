import React from 'react';
import clsx from 'clsx';
import Drawer from '@material-ui/core/Drawer';
import CssBaseline from '@material-ui/core/CssBaseline';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';


import Hidden from '@material-ui/core/Hidden';


import Logo from './Logo';
import useStyles from './Styles';
import Sidebar from './Sidebar';





export default function Header(props) {
    const classes = useStyles();
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
                    <Logo id='1' width="40" height="40" className={classes.menuButton} />
                    <Typography variant="h6" noWrap> Persistent drawer </Typography>
                </Toolbar>
            </AppBar>
            
            <Hidden smDown>
                <Drawer className={classes.drawer} variant="persistent" open={open} classes={{ paper: classes.drawerPaper, }}>
                    <Sidebar classes={classes} handleDrawer={handleDrawer}/>
                </Drawer>
            </Hidden>

            <Hidden mdUp>
                <Drawer variant="temporary" open={open} classes={{ paper: classes.drawerPaper, }} onClose={toggleDrawer(false)}>
                    <Sidebar classes={classes} handleDrawer={handleDrawer}/>
                </Drawer>
            </Hidden>

            <main className={clsx(classes.content, { [classes.contentShift]: open, })} >
                <div className={classes.drawerHeader} />
                {props.children}
            </main>
        </div>
    );
}
