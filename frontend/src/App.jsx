import { useState } from "react";
import "./App.css";

import Upload from "./components/Upload";
import Dashboard from "./components/Dashboard";

function App() {

  const [data, setData] = useState(null);

  return (

    <div className="app">

      <header className="header">
        <h1>📊 InsightAI</h1>
        <p>AI Powered Business Intelligence Platform</p>
      </header>

      <Upload setData={setData} />

      <div className="dashboard">

        {data && <Dashboard data={data} />}

      </div>

    </div>

  );
}

export default App;