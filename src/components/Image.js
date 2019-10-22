import React from 'react';

function Image(props) {
    console.log(props.image);
    console.log(props.title);
    return (
        <img className="" src={props.image} alt={props.title} />
    );
}
export default Image;