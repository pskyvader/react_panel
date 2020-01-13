import React from 'react';
import {
    Typography,
} from '@material-ui/core';
import List2 from '../components/List2';

export default () => (
    <React.Fragment>
        <Typography variant="h3">Welcome Home!</Typography>
        <List2 table="Igaccounts" fields={['idigaccounts' ,'fullName' ,'username' ,'profilePicUrl' ,'followerCount' ,'followingCount' ,'fecha' ,'following' ,'follower' ,'favorito' ,'hashtag']}></List2>
    </React.Fragment>
);