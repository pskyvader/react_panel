import React, { Fragment } from 'react';
import { CssBaseline, withStyles, } from '@material-ui/core';
import Header from './components/Header';
import Home from './pages/Home';
import { ApolloProvider } from '@apollo/react-hooks';
import ApolloClient from 'apollo-boost';
import {
    Route,
    Switch,
    useLocation
} from "react-router-dom";

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
                <Switch>
                    <Route exact path="/">
                        <Home />
                    </Route>
                    <Route path="/home">
                        <Home />
                    </Route>
                    <Route path="*">
                        <NoMatch />
                    </Route>
                </Switch>
            </main>
        </Fragment>
    </ApolloProvider>
);


function NoMatch() {
    let location = useLocation();

    return (
        <div>
            <h3>
                No match for <code>{location.pathname}</code>
            </h3>
        </div>
    );
}

export default withStyles(styles)(App);