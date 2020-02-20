import React,{Fragment} from 'react';
import ModuleCard from '../components/ModuleCard';
import {
    Typography,Grid,Container
} from '@material-ui/core';
import {
    useParams
  } from "react-router-dom";

export default () => {
    let { module,tipo } = useParams();
    console.log(useParams());
    let array=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1];
    return (
            <Container maxWidth="xl" fixed>
    <Typography variant="h3">Module {module} {tipo? `tipo ${tipo}`:'' } </Typography>
    <Grid
  container
  direction="row"
  justify="flex-start"
  alignItems="flex-start" spacing={3}
>
    {array.map((element,index) => {
        return (
            <Grid item xs={12} sm={6} md={4} lg={3} xl={2}>
                <ModuleCard key={index}/>
                </Grid>
        )    })}
        </Grid>
        </Container>
    )
};