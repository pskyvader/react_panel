import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import ModuleCard from '../components/ModuleCard';
import ModuleConfiguration from '../components/ModuleConfiguration';
import {
    Typography, Grid, Container
} from '@material-ui/core';



const useStyles = makeStyles(theme => ({
    grid: {
        display: 'flex',
        justifyContent: 'center',
        [theme.breakpoints.up('md')]: {
            justifyContent: 'flex-start',
        },

    },
}));

function ModuleList(props) {
    const {module,tipo,config}=props;
    const classes = useStyles();
    return "asdf";
    console.log(config);
    if (config==null){
        return "";
    }

    let array = [1, 1, 1, 1, 1,1,1,1,1,1,1,1];
    return (
        <Container maxWidth="xl" fixed>
            <Typography variant="h3" gutterBottom >Module {module} {tipo ? `tipo ${tipo}` : ''} </Typography>
            <ModuleConfiguration module={module} tipo={tipo} idadministrador="1">
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
            </ModuleConfiguration>
        </Container>
    )
};

export default ModuleList;