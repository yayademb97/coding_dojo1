import React from 'react';
const PersonCard = props => {
    

    return (
        <div>
            
            {/* {props.data.map((person) => {
                return (
                    <div>
                    <h1>{person.firstName}, {person.lastName}</h1>
                    <p>Age: {person.age}</p>
                    <p>Hair Color: {person.hairColor}</p>
                    </div>
                    
                )
            })} */}
            <div>
            {props.address.town}

            </div>
        </div>
    );

}

export default PersonCard;

