import React, { useRef } from 'react';
import { Typography, Container } from '@material-ui/core';
import { useParams } from "react-router-dom";
import { makeStyles } from '@material-ui/core/styles';

import ModuleConfiguration from '../components/ModuleConfiguration';

const useStyles = makeStyles(theme => (
    {
        root: {
            [theme.breakpoints.down('sm')]: {
                paddingLeft: 0,
                paddingRight: 0
            },
        },
        typography:{
            [theme.breakpoints.down('sm')]: {
                padding: theme.spacing(0, 3)
            },
        }
    }
));

export default (props) => {
    const classes = useStyles();
    const TypographyRef = useRef();
    let { module, tipo } = useParams();
    if (typeof (tipo) == 'undefined') {
        tipo = 0;
    }
    return (
        <Container maxWidth="xl" className={classes.root}>
            <Typography ref={TypographyRef} variant="h4" gutterBottom  className={classes.typography} >Module {module} {tipo ? `tipo ${tipo}` : ''} </Typography>
            <ModuleConfiguration module={module} tipo={tipo} idadministrador="1" TypographyRef={TypographyRef} {...props} />
        </Container>
    )
};