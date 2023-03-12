import React, { useState } from 'react';


const MoreForm = (props) => {
    const [firstname, setFirstname] = useState("");
    const [firstnameError, setFirstnameError] = useState("");
    const [lastname, setLastname] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confirmpassword, setConfirmPassword] = useState("");

    const createUser = (e) => {
        e.preventDefault();
        const newUser = { firstname, lastname, email, password, confirmpassword };
        console.log("Welcome", newUser);
        };
        

    
    return (
        <div>
        <form onSubmit={createUser}>
            <div>
                <label>First Name: </label>
                <input type="text" onChange={(e) => setFirstname(e.target.value)} value={firstname} />
                <p>{(firstname.length<2)?"First Name must be at least 2 characters.":"Good"}</p>
            </div>
            <div>
                <label>Last Name: </label>
                <input type="text" onChange={(e) => setLastname(e.target.value)} value={lastname} />
                <p>{(lastname.length<2)?"Last Name must be at least 2 characters.":"Good"}</p>
            </div>
            <div>
                <label>Email: </label>
                <input type="text" onChange={(e) => setEmail(e.target.value)} value={email} />
                <p>{(email.length<5)?"Email must be at least 5 characters long.":"Good"}</p>
            </div>
            <div>
                <label>Password: </label>
                <input type="text" onChange={(e) => setPassword(e.target.value)} value={password} />
                <p>{(password.length<8)?"Password must be at least 8 characters long.":"Good"}</p>

            </div>
            <div>
                <label>Confirm Password: </label>
                <input type="text" onChange={(e) => setConfirmPassword(e.target.value)} value={confirmpassword} />
                <p>{(confirmpassword!=password)?"Confirm Password must correspond to the same password!!!":"Good"}</p>
            </div>
            <p>Your Form Data</p>
            {/* <input type="submit" value="Create User" /> */}
        </form>
        </div>

    );
};

export default MoreForm;