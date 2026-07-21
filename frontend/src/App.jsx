import { useState } from "react";
import "./App.css";

import Upload from "./components/Upload";
import Dashboard from "./components/Dashboard";

function App() {
  const [data, setData] = useState(null);

  return (
    <div className="app">

      {/* Background Decorative Shapes */}
      <div className="bg-circle bg-circle-1"></div>
      <div className="bg-circle bg-circle-2"></div>

      {/* Hero Header */}
      <header className="hero">

        <div className="hero-content">

          <div className="logo">
            📊
          </div>

         <div className="hero-text">

  <h1>InsightAI</h1>

  <p>
    AI Powered Business Intelligence Platform
  </p>

</div>
        </div>

        <div className="hero-right">

          <span className="status-dot"></span>

          Ready

        </div>

      </header>

      {/* Upload Section */}

      <section className="upload-wrapper">

        <Upload setData={setData} />

      </section>

      {/* Dashboard */}

      {data && (

        <main className="dashboard-wrapper">

          <Dashboard data={data} />

        </main>

      )}

    </div>
  );
}

export default App;