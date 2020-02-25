import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import ModuleCard from '../components/ModuleCard';
import ModuleConfiguration from '../components/ModuleConfiguration';
import {
    Typography, Grid, Container
} from '@material-ui/core';
import {
    useParams
} from "react-router-dom";



const useStyles = makeStyles(theme => ({
    grid: {
        display: 'flex',
        justifyContent: 'center',
        [theme.breakpoints.up('md')]: {
            justifyContent: 'flex-start',
        },

    },
}));

export default () => {
    const classes = useStyles();
    let { module, tipo } = useParams();
    if (typeof(tipo)=='undefined'){
        tipo=0;
    }
    const configuracion=ModuleConfiguration({module:module,tipo:tipo,idadministrador:1});
    console.log(configuracion);
    let array = [1, 1, 1, 1, 1,1,1,1,1,1,1,1];
    return (
        <Container maxWidth="xl" fixed>
            {(configuracion!=null)?configuracion:null}
            <Typography variant="h3" gutterBottom >Module {module} {tipo ? `tipo ${tipo}` : ''} </Typography>
            <Grid
                container
                direction="row"
                justify="flex-start"
                alignItems="flex-start" spacing={3}
            >
                {array.map((element, index) => {
                    return (
                        <Grid item xs={12} sm className={classes.grid} key={index}>
                            <ModuleCard />
                        </Grid>
                    )
                })}
            </Grid>
        </Container>
    )
};