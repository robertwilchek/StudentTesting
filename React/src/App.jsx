import './App.css';

function App() {
  const infoItems = [
    'This React sample is built with Vite and React 18.',
    'All assets are bundled locally, so no external CDNs are required.',
    'After building once, the output in the dist/ folder can be viewed without an internet connection.',
  ];

  return (
    <main className="app-container">
      <header>
        <h1>Hello, React!</h1>
        <p className="tagline">A self-contained example you can run entirely offline.</p>
      </header>

      <section>
        <h2>Project Highlights</h2>
        <ul>
          {infoItems.map((item) => (
            <li key={item}>{item}</li>
          ))}
        </ul>
      </section>

      <section className="instructions">
        <h2>Next Steps</h2>
        <p>
          Edit <code>src/App.jsx</code> and save to see automatic refreshes while the dev server is
          running. Build the project to generate an offline-friendly bundle under <code>dist/</code>.
        </p>
      </section>
    </main>
  );
}

export default App;
