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
    let fields=['id'];
    if (config !== null && config!==false) {
        console.log(config);
        const module_data = config.hijo[0];
        const fields_filter = module_data.permisos.mostrar.filter(x => (x['tipo'] === 'active' || x['tipo'] === 'text'));
        fields = fields_filter.map(x => x['field']);
    }
    



    const vars = { first: 10, after: '' }
    if (tipo>0){
        vars['tipo']=tipo;
    }

    const table_query = 'all' + module.charAt(0).toUpperCase() + module.slice(1);
    const GET_LIST = gql(`
    query get_list($first:Int!,$after:String){
        $table(first:$first,after:$after,$tipo){
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
    `.replace('$table', table_query).replace('$fields', fields).replace('$tipo',(tipo>0)?'tipo:'+tipo:'') );

    const { items, loading, loadMore, hasNextPage, error } = Resolve({ query: GET_LIST, table: table_query, vars: vars });

    if (error){
        return error;
    }
    
    if (config === null) {
        return "Loading...";
    } else if (!config) {
        return "Module " + module + " not allowed for this user";
    }
    console.log(items);


    // let items = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1];
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
                        <ModuleCard {...element} />
                    </Grid>
                )
            })}
        </Grid>
    )
};

export default ModuleList;