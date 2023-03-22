import React, { useEffect, useState } from 'react'
import axios from "axios"
import { useParams } from 'react-router-dom'

const Planets = (props) => {
    const { planetsId } = useParams()
    const [planets, setPlanets] = useState('')
    useEffect(() => {
        axios.get(`https://swapi.dev/api/planets/${planetsId}/?format=json`)
            .then(res => {
                setPlanets(res.data)
            })
            .catch(err => {
                console.log("check pleassse", err);
            })
    }, [planetsId])


    return (
        <div>
            <h3>{planets.name}</h3>
            <p><h5>Climate:</h5>{planets.climate}cm
                <br />
                <h5>Terrain:</h5>{planets.terrain}kg
                <br />
                <h5>Surface Water:</h5>{planets.surface_water}
                <br />
                <h5>Population</h5>{planets.population}
            </p>
        </div>
    )
}

export default Planets