import React from 'react';

const static_folder='public/images'
function Image(props) {
    var final_image=props.image;
    console.log(final_image,final_image[0]);
    var static_image=static_folder+final_image['folder']+final_image.parent+final_image.subfolder+final_image.url;
    return (
        <img className="" src={static_image} alt={props.title} />
    );
}
export default Image;