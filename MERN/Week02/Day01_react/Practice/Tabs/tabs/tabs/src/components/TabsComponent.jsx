import React, { useState } from 'react'

const Tabs = (props) => {
    const [tabs1, setTabs1] = useState("");
    const [tabs2, setTabs2] = useState("");
    const [tabs3, setTabs3] = useState("");


    const showTabs1 = (e) => {
        e.preventDefault();
        setTabs1("Tab 1 content showing is here")
        setTabs2()
        setTabs3()
    }

    const showTabs2 = (e) => {
        e.preventDefault();
        setTabs2("Tab 2 content showing is here")
        setTabs1()
        setTabs3()
    }
    const showTabs3 = (e) => {
        e.preventDefault();
        setTabs3("Tab 3 content showing is here")
        setTabs2()
        setTabs1()
    }
    return (
        <div>
            <div style={{display:"flex"}} >
                <button onClick={(e) => {showTabs1(e)}}>Tabs1</button>
                <button onClick={(e) => {showTabs2(e)}}>Tabs2</button>
                <button onClick={(e) => {showTabs3(e)}}>Tabs3</button>
            </div>

            <div >
        <p>{tabs1}</p>
        <p>{tabs2}</p>
        <p>{tabs3}</p>
        </div>
        </div>
    )
}

export default Tabs