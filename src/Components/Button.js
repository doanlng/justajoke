import React from "react";
import "./Button.css";
const lines = [
  "HA! CAN I HEAR ANOTHER?",
  "SIDE SPLITTING COMEDY, I MUST HAVE MORE!",
  "BRILLIANT! PLEASE! ANOTHER!",
  "I CAN'T STOP LAUGHING! MORE!",
  "AGAIN!",
  "MORE! MORE! MORE!(i gave a second chance to cupid)",
  "CONTINUE",
];
export default function Button(props) {
  const [selectedLine, setSelectedLine] = React.useState("TELL ME A JOKE");

  const switchLine = () => {
    const randomIndex = Math.floor(Math.random() * lines.length);
    const nextLine = lines[randomIndex];
    setSelectedLine(nextLine);
  };

  return (
    <div className="custom-button" onClick={switchLine}>
      {selectedLine && <p>{selectedLine}</p>}
    </div>
  );
}
