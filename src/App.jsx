import React from 'react';
import Header from './components/Header';
import Home from './pages/Home';
import { ApolloProvider } from '@apollo/react-hooks';
import ApolloClient from 'apollo-boost';
import { Route, Switch } from "react-router-dom";

const client = new ApolloClient({
    uri: process.env.REACT_APP_API_URL,
});


function repeticiones(turno=1,posibilidades=18){
    var count=0;
    var turno_final=0;
    do {
        turno_final=Math.round(Math.random()*posibilidades);
        count++;
    } while (turno_final!==turno);
    return count;
}

var totales=[];
for (let index = 0; index < 5; index++) {
    totales.push(repeticiones(1,18));
}

var suma=0;
totales.forEach(element => {
    suma+=element;
});

var final=suma/totales.length;
console.log(final);




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