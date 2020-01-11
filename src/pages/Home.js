import React from 'react';
import {
    Typography,
} from '@material-ui/core';
import List from '../components/List';

export default () => (
    <React.Fragment>
        <Typography variant="h3">Welcome Home!</Typography>
        <List table="igaccounts">Cuentas</List>
    </React.Fragment>
);