import React, { Component } from 'react';

function Image(props) {
    return (
        <img className="" src={props.image} alt={props.title} />
    );
}
export default Image;