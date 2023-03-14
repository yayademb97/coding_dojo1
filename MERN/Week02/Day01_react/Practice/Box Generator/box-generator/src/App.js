import './App.css';
import { useState } from 'react'
import BoxStyleForm from './components/BoxStyleForm';
import Display from './components/Display';

function App() {
  const [colors, setcolors] = useState([])
  return (
    <fieldset>
      <legend>App.js</legend>
      {/* {JSON.stringify(color)} */}
      <div className="App">
        <BoxStyleForm colors={colors} setcolors={setcolors} />

        <Display colors={colors} />
        {/* {JSON.stringify(props.color)} */}

      </div>
    </fieldset>
  );
}

export default App;
