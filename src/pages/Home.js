import React from 'react';
import {
    Typography,
} from '@material-ui/core';
import List from '../components/List';
import Form from '../components/Form';

export default () => (
    <React.Fragment>
        <Typography variant="h3">Welcome Home!</Typography>
        <List table="Igaccounts" fields={['idigaccounts' ,'fullName' ,'username' ,'profilePicUrl' ,'followerCount' ,'followingCount' ,'fecha' ,'following' ,'follower' ,'favorito' ,'hashtag']}></List>
        <Form></Form>
    </React.Fragment>
);