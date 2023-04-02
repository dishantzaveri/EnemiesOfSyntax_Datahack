import React from "react";
import "./cta.css";
import { Link } from "react-router-dom";

const CTA = () => (
  <div className="gpt3__cta">
    <div className="gpt3__cta-content">
      <p>Start your journey right now!</p>
      <h3>Sell your car stress-free - We've got you covered</h3>
    </div>
    <div className="gpt3__cta-btn">
      <button type="button">
        <p>
          <Link to="/blog">Get started</Link>
        </p>
      </button>
    </div>
  </div>
);

export default CTA;
