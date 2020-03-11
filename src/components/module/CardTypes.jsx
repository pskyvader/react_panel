import React from 'react';
import CardHeader from '@material-ui/core/CardHeader';
import Avatar from '@material-ui/core/Avatar';
import IconButton from '@material-ui/core/IconButton';
import MoreVertIcon from '@material-ui/icons/MoreVert';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';

export const text = (value, classes) => (
    <CardContent>
        <Typography variant="body2" color="textSecondary" component="p">
            {value}
        </Typography>
    </CardContent>
)
export const title = (value, classes) => (
    <CardHeader
        avatar={<Avatar aria-label="recipe" className={classes.avatar}> R </Avatar>}
        action={<IconButton aria-label="settings"> <MoreVertIcon /> </IconButton>}
        title={value}
    />
)