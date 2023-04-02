import React from "react";
import Feature from "../../components/feature/Feature";
import "./features.css";

const featuresData = [
  {
    title: "Check your car's market price",
    text: "Get your car's current market price by just giving us few details about your car",
  },
  {
    title: "Compare",
    text: "Compare the price of your car with the current market rates",
  },
  {
    title: "Insurance ",
    text: "Detect the dents in your car and tell you the insurance rates",
  },
  {
    title: "FREE?",
    text: "Yes you heard it right. All of this for completely free of cost!",
  },
];

const Features = () => (
  <div className="gpt3__features section__padding" id="features">
    <div className="gpt3__features-heading">
      <h1 className="gradient__text">
        The Future is Now and You Just Need to Realize It. Step into Future
        Today. & Make it Happen.
      </h1>
      <p>All the functionalities we offer!</p>
    </div>
    <div className="gpt3__features-container">
      {featuresData.map((item, index) => (
        <Feature title={item.title} text={item.text} key={item.title + index} />
      ))}
    </div>
  </div>
);

export default Features;
