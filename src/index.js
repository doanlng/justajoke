import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import Client from "./Requests/Client";
import { Provider } from "urql";

// Check connection status
Client.query(`{ __typename }`)
  .toPromise()
  .then(() => {
    console.log("Connection established");
  })
  .catch((error) => {
    console.error("Connection error:", error);
  });

const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(
  <Provider value={Client}>
    <React.StrictMode>
      <App />
    </React.StrictMode>
  </Provider>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
