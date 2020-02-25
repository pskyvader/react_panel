import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import ModuleCard from '../components/ModuleCard';
import { Grid } from '@material-ui/core';
import { gql } from 'apollo-boost';
import Resolve from './Resolve';



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
    const module_data = config.hijo[0];
    const fields_filter = module_data.permisos.mostrar.filter(x => (x['tipo'] === 'active' || x['tipo'] === 'text'));
    const fields = fields_filter.map(x => x['field']);



    const vars = { first: 10, after: '' }
    if (tipo>0){
        vars['tipo']=tipo;
    }

    const table_query = 'all' + module;
    const GET_LIST = gql(`
    query get_list($first:Int!,$after:String,$tipo:Int){
        $table(first:$first,after:$after,tipo:$tipo){
            pageInfo{
                endCursor
                hasNextPage
            }
            edges{
                node{
                    $fields
                }
            }
        }
    }
    `.replace('$table', table_query).replace('$fields', fields));

    const { items, loading, loadMore, hasNextPage, error } = Resolve({ query: GET_LIST, table: table_query, vars: vars });

    if (error){
        return error;
    }

    return (
        <Grid
            container
            direction="row"
            justify="flex-start"
            alignItems="flex-start" spacing={3}
        >
            {items.map((element, index) => {
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