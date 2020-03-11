import React from 'react';
import CardHeader from '@material-ui/core/CardHeader';
import Avatar from '@material-ui/core/Avatar';
import IconButton from '@material-ui/core/IconButton';
import MoreVertIcon from '@material-ui/icons/MoreVert';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import CardMedia from '@material-ui/core/CardMedia';
import CheckBoxIcon from '@material-ui/icons/CheckBox';
import CancelIcon from '@material-ui/icons/Cancel';
import Box from '@material-ui/core/Box';



export const active = (key, value, classes) => (
    <Button
        color={(value)?"primary" :"secondary"}
        className={classes.button}
        startIcon={(value)?<CheckBoxIcon /> :<CancelIcon/>}
      >
        {key}
      </Button>

)

export const image = (key, value, classes) => (
    <CardMedia className={classes.media} image={value} title={key} />
)

export const text = (key, value, classes) => (
    <Typography noWrap variant="body2" color="textSecondary" component="p">
        {key + ': ' + value}
    </Typography>
)
export const title = (key, value, classes) => (
    <CardHeader noWrap
        titleTypographyProps={{ noWrap: true }}
        className={classes.header}
        // avatar={<Avatar aria-label="recipe" className={classes.avatar}> R </Avatar>}
        // action={<IconButton aria-label="settings"> <MoreVertIcon /> </IconButton>}
        title={key + ': ' + value}
    />
)
