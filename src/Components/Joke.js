import React, { useState } from "react";
import "./joke.css";
export default function Joke(props) {
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
        Why do birds fly South for the Winter?
      </p>
      {showPunchline && (
        <p>
          <span className="punchline">Because it's too far to walk!</span>
        </p>
      )}
    </div>
  );
}
