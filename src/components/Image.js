import React, { Component } from 'react';

function Image(props) {
    image=props.image;
    title=props.title;
    return (
        <img className="" src={image} alt={title} />
    );
}
export default Image;