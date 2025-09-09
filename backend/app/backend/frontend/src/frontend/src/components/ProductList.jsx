import React, {useEffect, useState} from "react";
export default function ProductList(){
  const [products,setProducts]=useState([]);
  useEffect(()=>{ fetch("http://localhost:8000/products").then(r=>r.json()).then(setProducts) },[]);
  return (
    <div>
      {products.map(p=>(
        <div key={p.id} style={{border:"1px solid #ddd", padding:10, margin:10}}>
          <h3>{p.name} — ${p.price}</h3>
          <p>{p.description}</p>
        </div>
      ))}
    </div>
  )
}
