
import { useQuery } from '@apollo/react-hooks';

function Resolve(props) {
    const table = props.table;
    const { data, loading, fetchMore } = useQuery(props.query, {variables:props.vars, notifyOnNetworkStatusChange: true });


    if (loading && (!data || !data[table])) return { loading, items: [] };
    
    const loadMore = () => {
        props.vars['after'] = data[table].pageInfo.endCursor
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
        });
    };
    return {
        items: data[table].edges.map(({ node }) => node),
        hasNextPage: data[table].pageInfo.hasNextPage,
        loading,
        loadMore,
    };
}

export default Resolve;