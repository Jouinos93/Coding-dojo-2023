import React from 'react'

function PersonCard(props) {

    const {firstName,lastName,age,haircolor} = props.person;
    return (
    <div>
        <h1>{firstName}, {lastName}</h1>
        <p>age:{age}</p>
        <p>Hair Color:{haircolor}</p>
    </div>
)

}

export default PersonCard