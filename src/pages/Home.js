import React from 'react';
import {
    Typography,
} from '@material-ui/core';
import List from '../components/List';
import Form from '../components/Form';
import Box from '@material-ui/core/Box';

export default () => (
    <React.Fragment>
        <Typography variant="h3">Welcome Home!</Typography>
            <Form></Form>

            <List table="Igaccounts" fields={['idigaccounts', 'fullName', 'username', 'profilePicUrl', 'followerCount', 'followingCount', 'fecha', 'following', 'follower', 'favorito', 'hashtag']}></List>



    </React.Fragment>
);