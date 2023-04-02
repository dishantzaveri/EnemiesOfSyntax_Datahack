import "./App.css";
import { Routes } from "react-router-dom";
import { Route } from "react-router-dom";
import Article from "./components/article/Article";
import Brand from "./components/brand/Brand";
import CTA from "./components/cta/CTA";
import Feature from "./components/feature/Feature";
import Navbar from "./components/navbar/Navbar";
import Car from "./CAR/Car";
import Blog from "./container/blog/Blog";
import Features from "./container/features/Features";
import Footer from "./container/footer/Footer";
import Header from "./container/header/Header";
import Possibility from "./container/possibility/Possibility";
import What from "./container/what/What";
import alanBtn from "@alan-ai/alan-sdk-web";
import { useEffect } from "react";

function App() {
  useEffect(() => {
    alanBtn({
      key: "ecc5936429f8831a0a3f3bd73ff973822e956eca572e1d8b807a3e2338fdd0dc/stage",
    });
  }, []);
  return (
    <>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/blog" element={<Blog />} />
      </Routes>
    </>
  );
}

function Home() {
  return (
    <div className="App">
      <div className="gradient__bg">
        {/* <Route path="/" element={<Navbar />} /> */}
        <Header />
      </div>
      <What />
      <Features />
      <CTA />
      <Footer />
    </div>
  );
}
export default App;
