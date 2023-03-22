import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Search = (props) => {
    const [search, setSearch] = useState("");
    const [id, setId] = useState()
    const nav = useNavigate()

    const handleSubmit = (e) => {
        e.preventDefault();
        nav(`/${search}/${id}`)
    }
    return (
        <div>
            <div>
                <form onSubmit={(e) => { handleSubmit(e) }}>
                    <label> Searching for: </label>
                    <select onChange={(e) => {
                        setSearch(e.target.value)
                    }}>
                        <option value="people">people</option>
                        <option value="planets">planets</option>
                    </select>
                    <label> ID: </label>
                    <input type="number" min="1" onChange={(e) => {
                        setId(e.target.value)
                    }} />
                    <button>Search</button>
                </form>

            </div>
        </div>
    )
}

export default Search