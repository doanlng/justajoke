import React, { useState, useEffect } from "react";
import "./joke.css";
import Client from "../Requests/Client";

export default function Joke(props) {
  const [data, setData] = useState([]);

  useEffect(() => {
    const joke = async () => {
      try {
        const result = await Client.query(
          `
          query {
            randomJoke{
                name,
                punchline,
                dateSubmitted,
            }
          }
        `
        ).toPromise();
        setData(result.data.randomJoke);
      } catch (error) {
        console.log(error);
      }
    };

    joke();
  }, []);
  const [showPunchline, setShowPunchline] = useState(false);
  const [arrowSymbol, setArrowSymbol] = useState("&#x2192;");

  const togglePunchline = () => {
    setShowPunchline(!showPunchline);
    if (arrowSymbol === "&#x2192;") {
      setArrowSymbol("&#x2193;");
    } else {
      setArrowSymbol("&#x2192;");
    }
  };

  return (
    <div onClick={togglePunchline}>
      <p>
        <div className="arrow" onClick={togglePunchline}>
          <span dangerouslySetInnerHTML={{ __html: arrowSymbol }} />
        </div>
        {data.name !== undefined
          ? data.name
          : "This is not a joke, something is broken."}
      </p>
      {showPunchline && (
        <p>
          <span className="punchline">
            {" "}
            {data.punchline !== undefined
              ? data.punchline
              : "We have no time for a punchline, production is being."}
          </span>
        </p>
      )}
    </div>
  );
}
