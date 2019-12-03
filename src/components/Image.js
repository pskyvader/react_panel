import React from 'react';

const static_folder = 'images'
function Image(props) {
    if (typeof (props.image) == 'object') {
        var image = props.image;
        if (image.length === 1) {
            var static_image = [static_folder, image[0]].join("/");
        } else {
            return Image_multiple(props.image, props.title);
        }
    } else {
        static_image = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+ip1sAAAAASUVORK5CYII=';
    }
    return (
        <img className="" src={static_image} alt={props.title} />
    );
}

function Image_multiple(images, title) {
    return (
        images.forEach(i => {
            var static_image = [static_folder, i].join("/");
            <img className="" src={static_image} alt={title} />
        }
        )
    );
}


export default Image;