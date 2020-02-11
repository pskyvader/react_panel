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
        <Box component="div" display="flex" p={1} m={1} bgcolor="background.paper" justifyContent="center">
            <Form></Form>
        </Box>

        <Box component="div" display="flex" p={1} m={1} bgcolor="background.paper">
            <List table="Igaccounts" fields={['idigaccounts', 'fullName', 'username', 'profilePicUrl', 'followerCount', 'followingCount', 'fecha', 'following', 'follower', 'favorito', 'hashtag']}></List>

        </Box>


    </React.Fragment>
);