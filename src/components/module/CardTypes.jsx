import React from 'react';
import CardHeader from '@material-ui/core/CardHeader';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import CardMedia from '@material-ui/core/CardMedia';
import CheckBoxIcon from '@material-ui/icons/CheckBox';
import CancelIcon from '@material-ui/icons/Cancel';



export const active = (key, value, classes) => (
    <Button 
    key={key}
        size="small"
        variant="outlined"
        color={(value) ? "primary" : "secondary"}
        className={classes.button}
        startIcon={(value) ? <CheckBoxIcon /> : <CancelIcon />}
    >
        {key}
    </Button>
)


export const link = (key, value, classes) => (
    <Button key={key} href={value}>
        {key}
    </Button>
)

export const image = (key, value, classes) => (
    <CardMedia key={key} className={classes.media} image={value} title={key} />
)

export const text = (key, value, classes) => (
    <Typography key={key} noWrap variant="body2" color="textSecondary" component="p">
        {key + ': ' + value}
    </Typography>
)
export const title = (key, value, classes) => (
    <CardHeader
        key={key}
        titleTypographyProps={{ noWrap: true }}
        className={classes.header}
        // avatar={<Avatar aria-label="recipe" className={classes.avatar}> R </Avatar>}
        // action={<IconButton aria-label="settings"> <MoreVertIcon /> </IconButton>}
        title={key + ': ' + value}
    />
)
