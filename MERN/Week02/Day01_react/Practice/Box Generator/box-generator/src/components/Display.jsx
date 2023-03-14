import React from 'react'

const Display = (props) => {
    return (
        <fieldset>
            <legend>Display.jsx</legend>
            <div style={{ display: "flex", flexWrap: "wrap" }}>
                {props.colors.map((onecolor, index) => {
                    return (
                        <div style={{ width: "100px", height: "100px", backgroundColor: onecolor.color }} key={index}    ></div>)

                })}

            </div>

        </fieldset>
    )
}

export default Display;