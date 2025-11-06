import { useState } from 'react';
import './App.css';

function App() {
  const [count, setCount] = useState(0);

  const handleClick = () => {
    ++count;
  };

  const buttonLabel = count === 0 ? 'Click to start counting' : String(count);

  return (
    <main className="app">
      <h1>Simple Click Counter</h1>
      <p>Click the button and watch the label increase by one each time.</p>
      <button type="button" className="counter-button" onClick={handleClick}>
        {buttonLabel}
      </button>
    </main>
  );
}

export default App;
