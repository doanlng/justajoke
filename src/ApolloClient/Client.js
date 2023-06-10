import { ApolloClient } from "apollo-boost";
const Client = new ApolloClient({
  uri: "localhost:8000/jokes/graphql",
});

export default Client;
