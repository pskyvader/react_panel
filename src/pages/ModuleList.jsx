import React from 'react';
import ModuleCard from '../components/ModuleCard';
import {
    Typography,
} from '@material-ui/core';
import {
    useParams
  } from "react-router-dom";

export default () => {
    let { module,tipo } = useParams();
    console.log(useParams());
    let array=new Array(10);
    return (
<div>
    <Typography variant="h3">Module {module} {tipo? `tipo ${tipo}`:'' } </Typography>
    {array.map(element => {
        return <ModuleCard/>
    })}
        
    </div>
    )
};