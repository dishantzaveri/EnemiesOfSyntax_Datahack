import React from "react";
import Feature from "../../components/feature/Feature";
import "./what.css";

const What = () => (
  <div className="gpt3__whatgpt3 section__margin" id="wgpt3">
    <div className="gpt3__whatgpt3-feature">
      <Feature
        title="What is CarGPT?"
        text="Our platform allows you to showcase your car with high-quality images, detailed descriptions, and a variety of customizable options."
      />
    </div>
    <div className="gpt3__whatgpt3-heading">
      <h1 className="gradient__text">
        Sell your car with confidence - Let us handle the details
      </h1>
    </div>
    <div className="gpt3__whatgpt3-container">
      <Feature
        title="Experience"
        text="With our user-friendly interface and advanced features, you can easily list your car for sale and connect with potential buyers from all over the world"
      />
      <Feature
        title="Any kind of cars!"
        text="Whether you're looking to sell a used car, a classic car, or a luxury vehicle, our platform has everything you need to make the process simple, convenient, and profitable"
      />
      <Feature
        title="24x7 Support"
        text=" Our team of experts will also provide you with personalized support and guidance throughout the selling process, ensuring that you get the best possible value for your car."
      />
    </div>
  </div>
);

export default What;
