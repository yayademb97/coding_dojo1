import './App.css';
import Search from './components/Search';
import People from './components/People';
import Planets from './components/Planets';
import { Route, Routes } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <Search/>
      <Routes>
        <Route path='/people/:peopleId' element={<People/>} />
        <Route path='/planets/:planetsId' element={<Planets/>} />

        
      </Routes>

    </div>
  );
}

export default App;
