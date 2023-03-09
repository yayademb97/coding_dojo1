import React, { Component } from 'react'

class PersonCard extends Component {

    constructor(props) {
        super(props);
        this.state = {
            age: this.props.age
        }
    }
    logout = () => { this.setState({ age: this.state.age + 1 }); };
    render() {
        const { firstName, lastName, age, haircolor } = this.props;
        return (
            <div>
                <h1> {firstName}, {lastName}</h1>
                <p>Age: {this.state.age}</p>

                
                <p>Hair Color: {haircolor}</p>
                <button onClick={this.logout}>Birthday Button</button>
            </div>
        );
    }
}

export default PersonCard;
