import './App.css';
import React, { useState, useEffect } from 'react'

function App() {


  
    const [people, setPeople] = useState([]);



    //   ! useEffect triggers when the component has FINISHED rendering

    useEffect(() => {
      fetchPokemon()
    }, [])

    const fetchPokemon = () => {
      fetch("https://pokeapi.co/api/v2/pokemon?limit=807")
        .then(response => {
          return response.json();
        }).then(response => {
          console.log(response);
          setPeople(response.results)
        }).catch(err => {
          console.log("⛔🚫", err);
        });
    }
    // fetchPokemon()

    return (
      <div className="App">
        <h1>Pokemon API 🦸‍♀️🦸🦸‍♂️</h1>
        <button onClick={() => { fetchPokemon()}}>Fetch Pokemon</button>
        <hr />
        <h2>Pokemon Name</h2>
        <u1>
          <li>
            {people.length > 0 && people.map((pokemon, index) => {
              return (<div key={index}>{pokemon.name}</div>)
            })}
          </li>
        </u1>
      </div>
    )
  }


export default App;
