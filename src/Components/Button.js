import React from "react";
import "./Button.css";
import Client from "../Requests/Client";

export default function Button(props) {
  const [data, setData] = React.useState([]); // array of lines
  const fetchlines = async () => {
    try {
      const result = Client.query(
        `
        query {
          randomProceeds(numProceeds:5){
            text
          }
        }
      `
      )
        .toPromise()
        .then((result) => {
          setData(result.data.randomProceeds); //fill the array with the lines
          console.log(data);
        });
    } catch (error) {
      console.log(error);
    }
  };

  const [selectedLine, setSelectedLine] = React.useState("TELL ME A JOKE");
  const switchLine = () => {
    if (data.length === 0) {
      // if the array is empty, refill it
      fetchlines();
    }
    let line = data.pop();
    console.log(line);
    setSelectedLine(line.text); // set the line to the last element of the array
    console.log(data.length);
  };
  return (
    <div className="custom-button" onClick={switchLine}>
      {selectedLine && <p>{selectedLine}</p>}
    </div>
  );
}
