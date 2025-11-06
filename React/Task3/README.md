# React Task 3 – People Directory

This folder contains a React 18 + Vite project that displays a hard-coded list of notable people in
technology. The list appears in a different random order on each page load, and a button allows you
to sort the entries alphabetically by last name.

## Prerequisites

- [Node.js](https://nodejs.org/) 18 or later (LTS recommended)
- npm (bundled with Node.js)

> 💡 If you are using VS Code, the official **ESLint** and **Prettier** extensions are optional but
> helpful when editing the source files.

## Getting Started

1. Open VS Code at the repository root and navigate to the `React/Task3` folder.
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm run dev
   ```
   The dev server runs locally and does not require an internet connection after the dependencies are
   installed the first time. Vite will print a local URL (for example, `http://localhost:5173`) that
   you can open in your browser.

## Building for Offline Use

1. Build the project to generate a production bundle:
   ```bash
   npm run build
   ```
   The compiled assets will be emitted to the `dist/` directory. Everything in that folder is
   self-contained, so it can be copied to any machine or served without internet access.

2. Preview the production build locally (optional):
   ```bash
   npm run preview
   ```
   This starts a local static server that serves the `dist/` directory. It requires no external
   network access once dependencies are installed.

3. To manually inspect the offline build without running the preview server, you can use any static
   file server available on your system. For example, with Python installed:
   ```bash
   cd dist
   python -m http.server 8000
   ```
   Then open `http://localhost:8000` in your browser. You may also open `dist/index.html` directly in
   a browser tab; however, running a lightweight local server avoids cross-origin restrictions in
   some browsers.

## Project Structure

```
React/Task3/
├── index.html          # Vite entry point
├── package.json        # npm scripts and dependencies
├── src/
│   ├── App.jsx         # Main React component with the people directory UI
│   ├── App.css         # Styles for the page and list
│   └── main.jsx        # React entry script
├── vite.config.js      # Vite + React plugin configuration
└── README.md           # This guide
```

Feel free to expand the list with more attributes (such as job titles or biographies) to experiment
with rendering richer content.
