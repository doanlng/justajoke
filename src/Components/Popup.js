import React, { useState } from "react";
import "./popup.css";
export default function Popup() {
  const [isOpen, setIsOpen] = useState(false);

  const togglePopup = () => {
    setIsOpen(!isOpen);
  };

  return (
    <div className="popup">
      {isOpen && (
        <div class="popupContent">
          <div>
            <p>
              See, the humor in this joke is that people understand that birds
              migrate to the South for the winter for environmental purposes,
              likely to be in a warmer climate. However, when considering the
              question literally, it is obvious that flying would be
              significantly quicker than walking. Thus, your expectations have
              been subverted.
            </p>
          </div>
          <span onClick={togglePopup} className="explain">
            Close
          </span>
        </div>
      )}
      {!isOpen && (
        <span onClick={togglePopup} className="explain">
          I don't understand
        </span>
      )}
    </div>
  );
}
