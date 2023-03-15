import './App.css';
import React, { useState, useEffect } from 'react';
import axios from 'axios';


function App() {
  const [people, setPeople] = useState([]);
  const [button, setButton]= useState(false);
  //* VANILLA JS fetch - Axios
  const fetchAxiosPokemon = (e) => {
    e.preventDefault();
    setButton(true);
  }

  useEffect(() => {
    axios.get("https://pokeapi.co/api/v2/pokemon?limit=807")
      .then((res) => {
        console.log(res.data); 
        setPeople(res.data.results)
      })
      .catch((err) => {
        console.log("❌❌", err);
      })
  }, [])
  return (
    <div className="App">
      <h1>Axios Pokemon API 🦸‍♀️🦸🦸‍♂️</h1>
      <button onClick={(e) => { fetchAxiosPokemon(e) }}>Fetch Axios Pokemon</button>
      <hr />
      <h2>Pokemon Name</h2>
      <ul>
        <li>
          {button === true? people.map((pokemon, index) => {
            return <div key={index}>{pokemon.name}</div>
          }): <p></p>}
        </li>
      </ul>
    </div>
  )
}

export default App;
