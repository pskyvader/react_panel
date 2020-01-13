
import { useQuery } from '@apollo/react-hooks';

function Resolve(props) {
    const table = props.table;
    var vars=props.vars;
    const { data, loading, fetchMore } = useQuery(props.query, {variables:vars, notifyOnNetworkStatusChange: true });


    if (loading && (!data || !data[table])) return { loading, items: [] };
    var items=data[table].edges.map(({ node }) => node);

    
    const loadMore = () => {
        vars['after'] = data[table].pageInfo.endCursor;
        vars['first'] = items.length*10;
        return fetchMore({
            query: props.query,
            notifyOnNetworkStatusChange: true,
            variables: vars,
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
        items: items,
        hasNextPage: data[table].pageInfo.hasNextPage,
        loading,
        loadMore,
    };
}

export default Resolve;