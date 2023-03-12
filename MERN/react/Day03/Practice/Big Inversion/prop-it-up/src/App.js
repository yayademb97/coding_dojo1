import './App.css';
import PersonCard from './components/PersonCard';
import UserForm from './components/UseForm';


function App() {
  const data = [
    {
        firstName: "Doe",
        lastName: "Jane",
        age: 45,
        hairColor: "Black"
    },
    {
        firstName: "Smith",
        lastName: "John",
        age: 88,
        hairColor: "Brown"
    },
    {
        firstName: "Fillmore",
        lastName: "Milliard",
        age: 50,
        hairColor: "Brown"
    },

    {
        firstName: "Smith",
        lastName: "Maria",
        age: 62,
        hairColor: "Brown"
    },

]
let c='yaya'
const adresses = [
  {
    town: "New York",
    state: "NY",
    country: "USA"
  },
  {
    town: "Philadelphia",
    state: "Boston",
    country: "USA"
  },
  {
    town: "Tunis",
    state: "Ariana",
    country: "Tunisia"
  },
  {
    town: "Madrid",
    state: "Maryland",
    country: "Spain"
  },
]
  return (
    <div className="App">
      
      {/* {adresses.map((address, index) =>{
        return (<PersonCard  key={index} address={address}/>)
      })} */}
  <UserForm />
    </div>
  );
}

export default App;
