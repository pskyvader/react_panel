import React from 'react';

const static_folder = 'images'
function Image(props) {
    if (typeof (props.image) == 'object') {
        var image = props.image;
        if (image.length === 0) {
            return single_image(image[0], props.title);
        } else {
            return Image_multiple(image, props.title);
        }
    } else {
        return (single_image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+ip1sAAAAASUVORK5CYII=', props.title));
    }
}

function Image_multiple(images, title) {
    var image_list = [];
    images.forEach(i => {
        image_list.push(single_image(i, title));
    });
    images.forEach(i => {
        image_list.push(single_image(i, title));
    });
    return image_list;
}

function single_image(image, title) {
    image = Object.values(image)[0];
    var static_image = [static_folder, image].join("/");
    return <img className="" src={static_image} alt={title} />
}


export default Image;