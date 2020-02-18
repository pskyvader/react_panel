import React from 'react';
import {
    Typography,
} from '@material-ui/core';
import Table from '../components/Table';
import Form from '../components/Form';

export default () => (
    <React.Fragment>
        <Typography variant="h3">Welcome Home!</Typography>
            <Form/>

            <Table table="Igaccounts" fields={['idigaccounts', 'fullName', 'username', 'profilePicUrl', 'followerCount', 'followingCount', 'fecha', 'following', 'follower', 'favorito', 'hashtag']}/>



    </React.Fragment>
);