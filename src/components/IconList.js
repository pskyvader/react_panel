import * as mui from '@material-ui/icons';

const allIconsMap = {};
Object.keys(mui)
    .sort()
    .forEach(key => {
        let tag;
        if (key.indexOf('Outlined') !== -1) {
            tag = 'Outlined';
        } else if (key.indexOf('TwoTone') !== -1) {
            tag = 'Two tone';
        } else if (key.indexOf('Rounded') !== -1) {
            tag = 'Rounded';
        } else if (key.indexOf('Sharp') !== -1) {
            tag = 'Sharp';
        } else {
            tag = 'Filled';
        }

        const icon = {
            key,
            tag,
            Icon: mui[key],
        };
        allIconsMap[key] = icon;
    });

export default allIconsMap;