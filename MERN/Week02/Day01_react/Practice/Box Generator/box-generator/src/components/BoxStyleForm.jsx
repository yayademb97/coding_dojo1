import React, { useState } from 'react'

const BoxStyleForm = (props) => {
    const [color, setColor] = useState("#ffffff")


    const submitInput = (e) => {
        e.preventDefault()
        const newColor = { color }
        props.setcolors([...props.colors, newColor])
        // setInput("")
        e.target.reset()
    }

    return (
        <div>
            <fieldset>
                <legend>BoxForm.jsx</legend>
                Current input : {color}
                <form onSubmit={(e) => { submitInput(e) }}>
                    <div>
                        <label > Color : </label>
                        <input type="color" onChange={(e) => { setColor(e.target.value) }} value={color} />
                        <button> Add + </button>

                    </div>
                    <br />
                </form>
            </fieldset>
        </div>
    )
}

export default BoxStyleForm;
