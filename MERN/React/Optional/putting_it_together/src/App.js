import React from 'react';
import PuttingItTogether from "./components/Putting_it_Together";
import './App.css';

const data = [
  {
    firstName: 'Doe',
    lastName: 'Jane',
    age: 50,
    hairColor: 'Black'
  },
  {
    firstName: 'Smith',
    lastName: 'John',
    age: 88,
    hairColor: 'Brown'
  }

];

function App() {
  return (
    <div className="App">
      {data.map((person, idx) => {
        return <PuttingItTogether person={person} key={idx} />;
      })}
    </div>
  );
}

export default App;