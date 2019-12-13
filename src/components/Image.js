import React from 'react';

const static_folder = 'images'
function Image(props) {
    if (typeof (props.image) == 'object') {
        var image = props.image;
        if (image.length === 1) {
            console.log(image[0],Object.values(image[0]));
            var static_image = [static_folder, image[0]].join("/");
        } else {
            return Image_multiple(image, props.title);
        }
    } else {
        static_image = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+ip1sAAAAASUVORK5CYII=';
    }
    return (
        <img className="" src={static_image} alt={props.title} />
    );
}

function Image_multiple(images, title) {
    var image_list = [];
    images.forEach(i => {
        var static_image = [static_folder, i].join("/");
        image_list.push(<img className="" src={static_image} alt={title} />);
    });

    return image_list;
}


export default Image;