import React, { Component } from 'react'
export default class Putting_it_Together extends Component {

constructor(props){
        super(props);
        this.state = {
        person: this.props.person
}
}

increment(){
        console.log(this.state.person.age);
        this.setState({
        person:{
        ...this.state.person,
        age : this.state.person.age + 1
}
})
}
render() {
const {firstName,lastName,age,haircolor} = this.state.person;
        return (
        <div>
        <h1>{firstName},{lastName}</h1>
        <p>age:{age}</p>
        <p>Hair Color:{haircolor}</p>
        <button onClick={()=>this.increment()}>Birthday Button for {firstName}</button>
        </div>
)
}
}