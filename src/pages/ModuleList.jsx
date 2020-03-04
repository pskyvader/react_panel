import React from 'react';
import ModuleConfiguration from '../components/ModuleConfiguration';
import { Typography, Container } from '@material-ui/core';
import { useParams } from "react-router-dom";
import { useRef } from 'react'


export default () => {
    const inputRef = useRef();
    let { module, tipo } = useParams();
    if (typeof (tipo) == 'undefined') {
        tipo = 0;
    }
    console.log(inputRef);
    return (
        <Container maxWidth="xl" fixed>
            <Typography ref={inputRef}  variant="h3" gutterBottom >Module {module} {tipo ? `tipo ${tipo}` : ''} </Typography>
            <ModuleConfiguration module={module} tipo={tipo} idadministrador="1" offsetTop={inputRef} />
        </Container>
    )
};