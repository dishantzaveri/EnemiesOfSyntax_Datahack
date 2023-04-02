import React from "react";
import "./header.css";
import Car from "../../CAR/Car";

const Header = () => (
  <div className="gpt3__header section__padding" id="home">
    <div className="gpt3__header-content">
      <h1 className="gradient__text">CarGPT</h1>
      <p>
        Say goodbye to the hassle of selling your car <br /> Start selling your
        car today and join the thousands of satisfied <br />
        sellers who have already found success on our platform.
      </p>
      <div
        className="gpt3__header-image"
        style={{ width: "570px", height: "570px" }}
      >
        <Car />
      </div>
    </div>
  </div>
);

export default Header;
