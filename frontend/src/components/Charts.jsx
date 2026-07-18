import "./Charts.css";

function Charts({ charts }) {
  if (!charts || charts.length === 0) return null;

  return (
    <div className="charts-container">

      <h2 className="charts-title">
        📈 Generated Charts
      </h2>

      <div className="charts-grid">

        {charts.map((chart, index) => (

          <div className="chart-card" key={index}>

            <h3>
              {chart
                .replace(".png", "")
                .replaceAll("_", " ")
                .replace(/\b\w/g, (c) => c.toUpperCase())}
            </h3>

            <img
              src={`http://127.0.0.1:8000/reports/${chart}`}
              alt={chart}
              className="chart-image"
            />

          </div>

        ))}

      </div>

    </div>
  );
}

export default Charts;