import React from 'react';
const PersonCard = props => {
    const data = [
        {
            firstName: "Doe",
            lastName: "Jane",
            age: 45,
            hairColor: "Black"
        },
        {
            firstName: "Smith",
            lastName: "John",
            age: 88,
            hairColor: "Brown"
        },
        {
            firstName: "Fillmore",
            lastName: "Milliard",
            age: 50,
            hairColor: "Brown"
        },

        {
            firstName: "Smith",
            lastName: "Maria",
            age: 62,
            hairColor: "Brown"
        },

    ]

    return (
        <div>
            {data.map((person) => {
                return (
                    <div>
                    <h1>{person.firstName}, {person.lastName}</h1>
                    <p>Age: {person.age}</p>
                    <p>Hair Color: {person.hairColor}</p>
                    </div>
                )
            })}
        </div>
    );

}

export default PersonCard;

