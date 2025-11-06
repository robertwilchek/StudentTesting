import { useMemo, useState } from 'react';
import './App.css';

const PEOPLE = [
  { firstName: 'Ada', lastName: 'Lovelace' },
  { firstName: 'Alan', lastName: 'Turing' },
  { firstName: 'Grace', lastName: 'Hopper' },
  { firstName: 'Edsger', lastName: 'Dijkstra' },
  { firstName: 'Katherine', lastName: 'Johnson' },
  { firstName: 'Donald', lastName: 'Knuth' },
];

const shuffle = (list) => {
  const copy = [...list];
  for (let index = copy.length - 1; index > 0; index -= 1) {
    const randomIndex = Math.floor(Math.random() * (index + 1));
    [copy[index], copy[randomIndex]] = [copy[randomIndex], copy[index]];
  }
  return copy;
};

function App() {
  const randomizedPeople = useMemo(() => shuffle(PEOPLE), []);
  const [people, setPeople] = useState(randomizedPeople);

  const handleSort = () => {

    setPeople(sorted);
  };

  return (
    <main className="app">
      <section className="content">
        <header>
          <h1>Task 3: People Directory</h1>
          <p>
            Below is a curated list of pioneers in computing. Refresh the page to see them in a
            different order, or sort them alphabetically by last name using the button.
          </p>
        </header>

        <button type="button" className="sort-button" onClick={handleSort}>
          Sort by last name
        </button>

        <table className="people-table">
          <thead>
            <tr>
              <th scope="col">Last name</th>
              <th scope="col">First name</th>
            </tr>
          </thead>
          <tbody>
            {people.map((person) => (
              <tr key={`${person.lastName}-${person.firstName}`}>
                <td>{person.lastName}</td>
                <td>{person.firstName}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </section>
    </main>
  );
}

export default App;
