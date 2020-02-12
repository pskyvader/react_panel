import React from 'react';

const ErrorLink = ({ graphQLErrors, networkError }) => {
    var error_message = null;
    if (graphQLErrors) {
        error_message = <pre>Bad: {graphQLErrors.map(({ message, extensions }, i) => (
            <span key={i}>Message: {message}, Location: {extensions.code}</span>
        ))}
        </pre>
    }

    if (networkError) {
        error_message = <pre>[Network error]:{` ${networkError}`} </pre>;
    }

    return error_message;
};

export default ErrorLink;