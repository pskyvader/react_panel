import React from 'react';

const static_folder='public/images'
function Image(props) {
    var image=props.image;
    var static_image=static_folder+image['folder']+image.parent+image.subfolder+image.url;
    return (
        <img className="" src={static_image} alt={props.title} />
    );
}
export default Image;