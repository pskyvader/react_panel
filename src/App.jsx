import React from 'react';
import { ApolloProvider } from '@apollo/react-hooks';
import ApolloClient from 'apollo-boost';
import { Route, Switch } from "react-router-dom";

import Header from './components/Header';
import Home from './pages/Home';
import ModuleList from './pages/ModuleList';

const client = new ApolloClient({
    uri: process.env.REACT_APP_API_URL,
});


const App = () => (
    <ApolloProvider client={client}>
        <Header>
            {(props) => (
                <Switch>
                    <Route exact path="/">
                        <Home />
                    </Route>
                    <Route path="/home">
                        <Home />
                    </Route>
                    <Route path="/:module/:tipo?">
                        <ModuleList {...props}/>
                    </Route>
                    <Route path="*">
                        404 not found
                    </Route>
                </Switch>
            )}

        </Header>
    </ApolloProvider>
);
export default App;