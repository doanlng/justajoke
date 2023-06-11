import "./App.css";
import { useState } from "react";
import Button from "./Components/Button";
import Joke from "./Components/Joke";
import Popup from "./Components/Popup";
function App() {
  const [j, renderJoke] = useState(false);

  const showJoke = () => {
    renderJoke(true);
  };

  return (
    <div className="App">
      <header className="App-header">
        <div className="grid-item"></div>
        <div className="grid-item"></div>
        <div className="grid-item"></div>
        <div className="grid-item"></div>
        <div className="grid-item">
          {j && <Joke />}
          <span className="b" onClick={showJoke}>
            <Button />
          </span>{" "}
        </div>
        <div className="grid-item"></div>
        <div className="grid-item"></div>
        <div className="grid-item"></div>
        <div className="grid-item">
          <Popup className="popup" />
        </div>
      </header>
    </div>
  );
}

export default App;
