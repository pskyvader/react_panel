import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import ModuleCard from '../components/ModuleCard';
import {
    Typography,Grid,Container
} from '@material-ui/core';
import {
    useParams
  } from "react-router-dom";



  const useStyles = makeStyles(theme => ({
    root: {
      flexGrow: 1,
    },
    paper: {
      height: 140,
      width: 100,
    },
    control: {
      padding: theme.spacing(2),
    },
  }));

export default () => {
    let { module,tipo } = useParams();
    let array=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1];
    return (
            <Container maxWidth="xl" fixed>
    <Typography variant="h3">Module {module} {tipo? `tipo ${tipo}`:'' } </Typography>
    <Grid
  container
  direction="row"
  justify="space-between"
  alignItems="flex-start" spacing={3}
>
    {array.map((element,index) => {
        return (
            <Grid item xs={12} sm>
                <ModuleCard key={index}/>
                </Grid>
        )    })}
        </Grid>
        </Container>
    )
};