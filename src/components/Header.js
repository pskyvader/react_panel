import React from 'react';
import { AppBar, Toolbar, Typography, withStyles } from '@material-ui/core';
import Grid from '@material-ui/core/Grid';
import Logo from './Logo';

// import Login from './Login';

const styles = {
    flex: {
        flex: 1,
    },
};
const Header = ({ classes }) => (
    <AppBar position="static">
        <Toolbar>
            <Grid container spacing={3}>
                <Grid item xs height="40%">
                    <Logo id='1' width="100" height="40" />
                </Grid>
                <Grid item xs>
                    <Typography variant="h4" color="inherit"> Panel v3.0 </Typography>
                    <div className={classes.flex} />
                    {/* <Login /> */}
                </Grid>
            </Grid>
        </Toolbar>
    </AppBar>
);

export default withStyles(styles)(Header);