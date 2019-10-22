import React from 'react';

function Image(props) {
    image=props.image;
    return (
        <img className="" src={image} alt={props.title} />
    );
}
export default Image;