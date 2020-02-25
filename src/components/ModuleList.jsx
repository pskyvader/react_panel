import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import ModuleCard from '../components/ModuleCard';
import { Grid } from '@material-ui/core';



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
    const { module, tipo, config } = props;
    const classes = useStyles();
    if (config === null) {
        return "Loading...";
    } else if (!config) {
        return "Module " + module + " not allowed for this user";
    }

    let array = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1];
    return (
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
    )
};

export default ModuleList;