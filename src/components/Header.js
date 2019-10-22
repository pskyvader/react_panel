import React from 'react';
import {
    AppBar,
    Toolbar,
    Typography,
    withStyles
} from '@material-ui/core';
import Logo from './Logo';

// import Login from './Login';

const styles = {
    flex: {
        flex: 1,
    },
};
const Header = ({ classes }) => (
    <AppBar position="static">
        <Logo />
        <Toolbar>
            <Typography variant="title" color="inherit">
                Panel v3.0
      </Typography>
            <div className={classes.flex} />
            {/* <Login /> */}
        </Toolbar>
    </AppBar>
);

export default withStyles(styles)(Header);