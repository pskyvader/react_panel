import React from 'react';
import ModuleConfiguration from '../components/ModuleConfiguration';
import { Typography, Container } from '@material-ui/core';
import { useParams } from "react-router-dom";
import { useRef } from 'react'


export default (props) => {
    const TypographyRef = useRef();
    let { module, tipo } = useParams();
    if (typeof (tipo) == 'undefined') {
        tipo = 0;
    }
    return (
        <Container maxWidth="xl">
            <Typography ref={TypographyRef}  variant="h4" gutterBottom >Module {module} {tipo ? `tipo ${tipo}` : ''} </Typography>
            <ModuleConfiguration module={module} tipo={tipo} idadministrador="1" TypographyRef={TypographyRef} {...props} />
        </Container>
    )
};