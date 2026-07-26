import { useState } from "react";
import "./Charts.css";

function Charts({ charts }) {

  const [selectedChart, setSelectedChart] = useState(null);

  if (!charts || charts.length === 0) return null;

  const getChartType = (chart) => {

    if (chart.includes("histogram")) return "Histogram";
    if (chart.includes("boxplot")) return "Box Plot";
    if (chart.includes("scatter")) return "Scatter Plot";
    if (chart.includes("heatmap")) return "Heatmap";
    if (chart.includes("line")) return "Line Chart";
    if (chart.includes("trend")) return "Trend";
    if (chart.includes("pie")) return "Pie Chart";
    if (chart.includes("bar")) return "Bar Chart";

    return "Chart";
  };

  return (

    <section className="charts-container">

      <div className="charts-header">

        <span className="section-badge">
          DATA VISUALIZATION
        </span>

        <h2>AI Generated Charts</h2>

        <p>
          InsightAI automatically creates professional
          visualizations to help understand your dataset faster.
        </p>

      </div>

      <div className="charts-grid">

        {charts.map((chart, index) => (

          <div className="chart-card" key={index}>

            <div className="chart-top">

              <span className="chart-type">
                {getChartType(chart)}
              </span>

            </div>

            <img
              src={`http://127.0.0.1:8000/reports/${chart}`}
              alt={chart}
              className="chart-image"
            />

            <h3>

              {chart
                .replace(".png", "")
                .replaceAll("_", " ")
                .replace(/\b\w/g, c => c.toUpperCase())}

            </h3>

            <button
              className="download-btn"
              onClick={() => setSelectedChart(chart)}
            >
              View Full Size
            </button>

          </div>

        ))}

      </div>

      {selectedChart && (

        <div
          className="image-modal"
          onClick={() => setSelectedChart(null)}
        >

          <div
            className="image-modal-content"
            onClick={(e) => e.stopPropagation()}
          >

            <button
              className="close-btn"
              onClick={() => setSelectedChart(null)}
            >
              ✕
            </button>

            <img
              src={`http://127.0.0.1:8000/reports/${selectedChart}`}
              alt={selectedChart}
              className="modal-image"
            />

          </div>

        </div>

      )}

    </section>

  );

}

export default Charts;