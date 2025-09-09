import React from "react";
import { createRoot } from "react-dom/client";
import ProductList from "./components/ProductList";

function App(){ return <div style={{padding:20}}><h1>Mini Ecom</h1><ProductList/></div> }
createRoot(document.getElementById("root")).render(<App />);
