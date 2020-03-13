import { useQuery } from '@apollo/react-hooks';
import ErrorLink from './ErrorLink';

function Resolve(props) {
    const table = props.table;
    const { data, loading, fetchMore,error } = useQuery(props.query, { variables: props.vars, notifyOnNetworkStatusChange: true });
    if (error && ErrorLink(error)!=null) return {error:ErrorLink(error)};

    if (loading && (!data || !data[table])) return { loading, items: [] };
    var items = data[table].edges.map(({ node }) => node);


    const loadMore = (callback) => {
        props.vars['after'] = data[table].pageInfo.endCursor;
        props.vars['first'] = items.length * 2;
        props.vars['first'] = (props.vars['first'] < 10) ? 10 : (props.vars['first'] > 1000 ? 1000 : props.vars['first']);
        return fetchMore({
            query: props.query,
            notifyOnNetworkStatusChange: true,
            variables: props.vars,
            updateQuery: (previousResult, { fetchMoreResult }) => {
                const newEdges = fetchMoreResult[table].edges;
                const pageInfo = fetchMoreResult[table].pageInfo;

                var newquery = {}
                newquery[table] = {
                    __typename: previousResult[table].__typename,
                    edges: [...previousResult[table].edges, ...newEdges],
                    pageInfo,
                };

                return newEdges.length ? newquery : previousResult;
            },
        }).then(function(val){
            if (typeof callback==='function'){
                callback(val);
            }
        });
    };

    return {
        items: items,
        hasNextPage: data[table].pageInfo.hasNextPage,
        loading,
        loadMore,
    };
}

export default Resolve;