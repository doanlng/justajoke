import { createClient, cacheExchange, fetchExchange } from "@urql/core";

const Client = createClient({
  url: " http://localhost:8000/jokes/graphql",
  exchanges: [cacheExchange, fetchExchange],
});

export default Client;
