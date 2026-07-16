import "./App.css";

function App() {
  return (
    <div className="app">

      <header className="header">
        <h1>📊 InsightAI</h1>
        <p>AI Powered Business Intelligence Platform</p>
      </header>

      <section className="upload-card">

        <h2>Upload Dataset</h2>

        <input type="file" accept=".csv,.xlsx" />

        <button>Analyze Dataset</button>

      </section>

      <section className="dashboard">

        <div className="card">
          <h3>Dataset Profile</h3>
          <p>Rows</p>
          <p>Columns</p>
          <p>Missing Values</p>
        </div>

        <div className="card">
          <h3>Cleaning Summary</h3>
          <p>Data cleaning results will appear here.</p>
        </div>

        <div className="card">
          <h3>Exploratory Data Analysis</h3>
          <p>Statistical analysis will appear here.</p>
        </div>

        <div className="card">
          <h3>Business Insights</h3>
          <p>AI generated insights will appear here.</p>
        </div>

        <div className="card">
          <h3>Charts</h3>
          <p>Visualizations will appear here.</p>
        </div>

        <div className="card">
          <h3>Final Report</h3>
          <p>Professional report summary will appear here.</p>
        </div>

      </section>

    </div>
  );
}

export default App;