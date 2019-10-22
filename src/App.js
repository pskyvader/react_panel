import React, { Fragment } from 'react';
import { CssBaseline, withStyles, } from '@material-ui/core';
import Header from './components/Header';
import Home from './pages/Home';

const API = 'http://localhost:8080/admin/';

const styles = theme => ({
  main: {
    padding: 3 * theme.spacing.unit,
    [theme.breakpoints.down('xs')]: {
      padding: 2 * theme.spacing.unit,
    },
  },
});


const App = ({ classes }) => (
  <Fragment>
    <CssBaseline />
    <Header />
    <main className={classes.main}>
      <Home />
    </main>
  </Fragment>
);

export default withStyles(styles)(App);