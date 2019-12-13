import React from 'react';

const static_folder = 'images'
function Image(props) {
    if (typeof (props.image) == 'object') {
        var image = props.image;
        if (image.length === 0) {
            image = Object.values(image[0])[0];
            var static_image = [static_folder, image].join("/");
        } else {
            return Image_multiple(image, props.title);
        }
    } else {
        static_image = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+ip1sAAAAASUVORK5CYII=';
    }
    return (single_image(static_image, props.title));
}

function Image_multiple(images, title) {
    var image_list = [];
    images.forEach(i => {
        var image = Object.values(i)[0];
        var static_image = [static_folder, image].join("/");
        image_list.push(single_image(static_image, title));
    });
    return image_list;
}

function single_image(static_image, title) {
    return <img className="" src={static_image} alt={title} />
}


export default Image;