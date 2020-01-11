
import { useQuery } from '@apollo/react-hooks';

function Resolve(props) {
    const table = props.table;
    const { data, loading, fetchMore } = useQuery(props.query, props.variables);

    if (loading && !data[table]) return { loading, table: [] };

    const loadMore = () => {
        props.vars['variables']['after'] = data[table].pageInfo.endCursor
        return fetchMore({
            query: props.query,
            notifyOnNetworkStatusChange: true,
            variables: props.vars['variables'],
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
        persons: data[table].edges.map(({ node }) => node),
        hasNextPage: data[table].pageInfo.hasNextPage,
        loading,
        loadMore,
    };
}

export default Resolve;