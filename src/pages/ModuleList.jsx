import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import ModuleCard from '../components/ModuleCard';
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
    let array = [1, 1, 1, 1, 1,1,1,1,1,1,1,1];
    return (
        <Container maxWidth="xl" fixed>
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