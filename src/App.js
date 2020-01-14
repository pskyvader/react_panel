import React, { Fragment } from 'react';
import { CssBaseline, withStyles, } from '@material-ui/core';
import Header from './components/Header';
import Home from './pages/Home';
import { ApolloProvider } from '@apollo/react-hooks';
import ApolloClient from 'apollo-boost';
import { onError } from "apollo-link-error";
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



const ErrorLink = onError(({ graphQLErrors, networkError }) => {
  var error_message;
  if (graphQLErrors)
    graphQLErrors.map(({ message, extensions },i) => {
    error_message= (<span key={i}>Message: {message}, Location: {extensions.code}</span>);
    });
  if (networkError) {
    error_message=`[Network error]: ${networkError}`;
  }
  return (
    <pre>{error_message} </pre>
  )
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