import React from 'react'
const Display = (props) => {


        return (
            <div>
            <div>
                <p>First Name: {props.data.firstname}</p>
            </div>
            <div>
                <p>Last Name: {props.data.lastname}</p>
            </div>
            <div>
                <p>Email: {props.data.email}</p>
            </div>
            <div>
                <p>Password: {props.data.password}</p>
            </div>
            <div>
                <p>Confirm Password: {props.data.confirmpassword}</p>
            </div>
            </div>
            
        )
    
}

    export default Display;