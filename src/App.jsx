import React from 'react';
import Header from './components/Header';
import Home from './pages/Home';
import { ApolloProvider } from '@apollo/react-hooks';
import ApolloClient from 'apollo-boost';
import { Route, Switch } from "react-router-dom";

const client = new ApolloClient({
    uri: process.env.REACT_APP_API_URL,
});




const App = () => (
    <ApolloProvider client={client}>
        <Header>
            <Switch>
                <Route exact path="/">
                    <Home />
                </Route>
                <Route path="/home">
                    <Home />
                </Route>
                <Route path="*">
                    404 not found
                    </Route>
            </Switch>
        </Header>
    </ApolloProvider>
);
export default App;