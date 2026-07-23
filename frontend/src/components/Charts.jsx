import "./Charts.css";

function Charts({ charts }) {

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

        <h2>
          AI Generated Charts
        </h2>

        <p>
          InsightAI automatically creates professional visualizations
          to help understand your dataset faster.
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
                .replace(".png","")
                .replaceAll("_"," ")
                .replace(/\b\w/g,c=>c.toUpperCase())}

            </h3>

            <a
              href={`http://127.0.0.1:8000/reports/${chart}`}
              target="_blank"
              rel="noreferrer"
              className="download-btn"
            >
              View Full Size
            </a>

          </div>

        ))}

      </div>

    </section>

  );

}

export default Charts;