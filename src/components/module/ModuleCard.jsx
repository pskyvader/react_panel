import React, { useRef } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import clsx from 'clsx';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import CardActions from '@material-ui/core/CardActions';
import Collapse from '@material-ui/core/Collapse';
import IconButton from '@material-ui/core/IconButton';
import Typography from '@material-ui/core/Typography';
import { red } from '@material-ui/core/colors';
import FavoriteIcon from '@material-ui/icons/Favorite';
import ShareIcon from '@material-ui/icons/Share';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import CardActionArea from '@material-ui/core/CardActionArea';

import * as types from './CardTypes';

const useStyles = makeStyles(theme => ({
    root: {
        margin: theme.spacing(2),
        transition:'none'
    },
    button: {
        margin: theme.spacing(1),
    },
    media: {
        height: 0,
        paddingTop: '56.25%', // 16:9
    },
    expand: {
        transform: 'rotate(0deg)',
        marginLeft: 'auto',
        transition: theme.transitions.create('transform', {
            duration: theme.transitions.duration.shortest,
        }),
    },
    expandOpen: {
        transform: 'rotate(180deg)',
    },
    avatar: {
        backgroundColor: red[500],
    },
    header: {
        padding: theme.spacing(2, 0),
        display: 'block'
    },
    actions: {
        display: 'block'
    }
}));




const action_list = ['link', 'active', 'action', 'delete'];




export default function RecipeReviewCard(props) {
    const { element, config_mostrar } = props;
    const classes = useStyles();
    const [expanded, setExpanded] = React.useState(false);
    const { Height, setHeight } = props;
    const CardRef = useRef();



    config_mostrar.map(x => {
        let value = element[x['field']];
        if (value !== undefined) {
            x['value'] = value;
        }
        delete x.__typename;
        return x;
    });
    const element_actions = config_mostrar.filter(x => (action_list.includes(x['tipo'])));
    const element_fields = config_mostrar.filter(x => (!action_list.includes(x['tipo'])));




    const handleExpandClick = () => {
        setExpanded(!expanded);
    };

    const set_height = (timeout=false) => {
        if (CardRef.current !== undefined && CardRef.current !== null) {
            const nodeStyle1 = window.getComputedStyle(CardRef.current);
            let margin = nodeStyle1.getPropertyValue('margin-bottom');
            const heightCard = CardRef.current.offsetHeight + parseFloat(margin) * 2;
            if (Height !== heightCard && heightCard <= 600) {
                setHeight(heightCard);
            }
        } else if (Height === 100 && !timeout) {
            setTimeout(set_height, 0,true);
        }
    }



    const setElement = (element, position) => {
        if (element['tipo'] === 'text' && position === 0) {
            element['tipo'] = 'title';
        }
        const current_element = types[element['tipo']];
        if (current_element === undefined) {
            return element['tipo'];
        }
        return current_element(element['titulo'], element['value'], classes);
    }





    const return_element = (
        <Card className={classes.root} ref={CardRef}>
            <CardActionArea focusRipple>
                <CardContent >
                    {element_fields.map((x, i) => setElement(x, i))}
                </CardContent>
            </CardActionArea>


            <CardActions disableSpacing className={classes.actions}>
                {element_actions.map((x, i) => setElement(x, i))}
                <IconButton aria-label="add to favorites"> <FavoriteIcon /> </IconButton>
                <IconButton aria-label="share"> <ShareIcon /> </IconButton>
                <IconButton className={clsx(classes.expand, { [classes.expandOpen]: expanded, })} onClick={handleExpandClick} aria-expanded={expanded} aria-label="show more" >
                    <ExpandMoreIcon />
                </IconButton>
            </CardActions>
            <Collapse in={expanded} timeout="auto" unmountOnExit>
                <CardContent>
                    <Typography paragraph>Method:</Typography>

                </CardContent>
            </Collapse>
        </Card>
    );
    if(Height!==null){
        set_height();
    }
    return return_element;
}