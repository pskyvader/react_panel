import React from 'react';
import CardHeader from '@material-ui/core/CardHeader';
import Avatar from '@material-ui/core/Avatar';
import IconButton from '@material-ui/core/IconButton';
import MoreVertIcon from '@material-ui/icons/MoreVert';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';
import CardMedia from '@material-ui/core/CardMedia';

export const text = (key,value, classes) => (
        <Typography variant="body2" color="textSecondary" component="p">
            {key+': '+value}
        </Typography>
)
export const title = (key,value, classes) => (
    <CardHeader
    className={classes.header}
        // avatar={<Avatar aria-label="recipe" className={classes.avatar}> R </Avatar>}
        // action={<IconButton aria-label="settings"> <MoreVertIcon /> </IconButton>}
        title={key+': '+value}
    />
)

export const image = (key,value, classes) => (
    <CardMedia className={classes.media} image={value} title={key}/>
)