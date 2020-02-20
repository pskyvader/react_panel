import React from 'react';
import ModuleCard from '../components/ModuleCard';
import {
    Typography,
} from '@material-ui/core';
import {
    useParams
  } from "react-router-dom";

export default () => {
    let { module } = useParams();
    return (
<div>
    <Typography variant="h3">Module {module}</Typography>
        <ModuleCard/>
    </div>
    )
};