import React from 'react';

const static_folder='images'
function Image(props) {
    if (typeof(props.image)=='object'){
        console.log(props.image);
        var image=props.image[0];
        var static_image=[static_folder,image.folder,image.parent,image.subfolder,image.url].join("/");
    }else{
        static_image='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+ip1sAAAAASUVORK5CYII=';
    }
    return (
        <img className="" src={static_image} alt={props.title} />
    );
}
export default Image;