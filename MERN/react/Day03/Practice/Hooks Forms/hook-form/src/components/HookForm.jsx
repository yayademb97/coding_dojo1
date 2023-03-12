import React, { useState } from 'react';
import Display from './Display';

const HookForm = (props) => {
    const [firstname, setFirstname] = useState("");
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
            </div>
            <div>
                <label>Last Name: </label>
                <input type="text" onChange={(e) => setLastname(e.target.value)} value={lastname} />
            </div>
            <div>
                <label>Email: </label>
                <input type="text" onChange={(e) => setEmail(e.target.value)} value={email} />
            </div>
            <div>
                <label>Password: </label>
                <input type="text" onChange={(e) => setPassword(e.target.value)} value={password} />
            </div>
            <div>
                <label>Confirm Password: </label>
                <input type="text" onChange={(e) => setConfirmPassword(e.target.value)} value={confirmpassword} />
            </div>
            <p>Your Form Data</p>
            <input type="submit" value="Create User" />
        </form>
        <div>
            <Display  data={{firstname,lastname, email, password, confirmpassword }} />
        </div>
        </div>

    );
};

export default HookForm;