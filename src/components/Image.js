import React, { Component } from 'react';

function Image(props) {
    console.log(props);
    return (
        <img className="" src={props.image} alt={props.title} />
    );
}
export default Image;