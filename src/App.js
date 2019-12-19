import React, { Fragment } from 'react';
import { CssBaseline, withStyles, } from '@material-ui/core';
import Header from './components/Header';
import Home from './pages/Home';
import { ApolloProvider } from '@apollo/react-hooks';
import ApolloClient from 'apollo-boost';
const client = new ApolloClient({
  uri: process.env.REACT_APP_API_URL,
});


const styles = theme => ({
  main: {
    padding: theme.spacing(3),
    [theme.breakpoints.down('xs')]: {
      padding: theme.spacing(2),
    },
  },
});


const App = ({ classes }) => (
  <ApolloProvider client={client}>
    <Fragment>
      <CssBaseline />
      <Header />
      <main className={classes.main}>
        <Home />
      </main>
    </Fragment>
  </ApolloProvider>
);

export default withStyles(styles)(App);