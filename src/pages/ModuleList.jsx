import React from 'react';
import ModuleConfiguration from '../components/ModuleConfiguration';
import { Typography, Container } from '@material-ui/core';
import { useParams } from "react-router-dom";

export default () => {
    let { module, tipo } = useParams();
    if (typeof (tipo) == 'undefined') {
        tipo = 0;
    }
    return (
        <Container maxWidth="xl" fixed>
            <Typography variant="h3" gutterBottom >Module {module} {tipo ? `tipo ${tipo}` : ''} </Typography>
            <ModuleConfiguration module={module} tipo={tipo} idadministrador="1" />
        </Container>
    )
};