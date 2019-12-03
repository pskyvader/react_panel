import React from 'react';

const static_folder='images'
function Image(props) {
    if (typeof(props.image)=='object'){
        var image=props.image;
        if (image.length==1){
            var static_image=[static_folder,image[0]].join("/");
        }
    }else{
        static_image='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+ip1sAAAAASUVORK5CYII=';
    }
    return (
        <img className="" src={static_image} alt={props.title} />
    );
}
export default Image;