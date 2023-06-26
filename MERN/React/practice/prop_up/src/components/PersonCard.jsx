import React, { Component } from 'react'

export default class PersonCard extends Component {
render() {
    const {firstName,lastName,age,haircolor} = this.props.person;
    return (
    <div>
        <h1>{firstName}, {lastName}</h1>
        <p>age:{age}</p>
        <p>Hair Color:{haircolor}</p>
    </div>
    )
}
}