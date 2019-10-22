import React from 'react';

const static_folder='public/images'
function Image(props) {
    var image=props.image;
    console.log(image);
    return (
        <img className="" src={static_folder+image.folder+image.parent+image.subfolder+image.url} alt={props.title} />
    );
}
export default Image;