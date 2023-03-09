import './App.css';
import PersonCard from './components/PersonCard';

function App() {


  
  return (
    <div className="App">
      <PersonCard firstName= {"Doe"} lastName= {"Jane"} age = {45} haircolor= "Black"/>
      <PersonCard firstName= "Smith" lastName= "John" age = {88} haircolor= "Brown"/>
      <PersonCard firstName= "Fillmore" lastName= "Milliard" age = {50} haircolor= "Brown"/>
      <PersonCard firstName= "Smith" lastName= "Maria" age = {62} haircolor= "Brown"/>

    </div>
  );
}

export default App;
