
import { useQuery } from '@apollo/react-hooks';

function Resolve(props) {
    const table = props.table;
    const { data, loading, fetchMore } = useQuery(props.query, {variables:props.vars, notifyOnNetworkStatusChange: true });


    if (loading && (!data || !data[table])){
        console.log('vacia',data);
    return { loading, items: [] };
    }else{
        console.log('no vacia',data,loading);

    }
        

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

                console.log(newquery , previousResult);
                

                return newEdges.length ? newquery : previousResult;
            },
        });
    };

    console.log(data);

    return {
        items: data[table].edges.map(({ node }) => node),
        hasNextPage: data[table].pageInfo.hasNextPage,
        loading,
        loadMore,
    };
}

export default Resolve;