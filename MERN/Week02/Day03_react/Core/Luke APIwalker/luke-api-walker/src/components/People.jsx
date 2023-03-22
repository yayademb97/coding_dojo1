import React, {useState, useEffect} from 'react'
import { useParams } from 'react-router-dom'
import axios from 'axios'

const People = (props) => {
    const [newpeople, setNewPeople] = useState({});
    const {peopleId} = useParams()
    useEffect((e)=>{
        axios.get(`https://swapi.dev/api/people/${peopleId}/?format=json`)
        .then(res => {
            console.log(res);
            setNewPeople(res.data);
        })
        .catch(err => {
            console.log(err);
            setNewPeople({err: "⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔"})
        })
    },[peopleId]);
    return (
        <div>
            <h1>Planet: {newpeople.name}</h1>
            <p><h5>height:</h5>{newpeople.height}cm
            <br />
            <h5>Mass:</h5>{newpeople.mass}kg
            <br />
            <h5>Hair Color:</h5>{newpeople.hair_color}
            <br />
            <h5>Skin Color:</h5>{newpeople.skin_color}
            </p>
        </div>
    )
}

export default People