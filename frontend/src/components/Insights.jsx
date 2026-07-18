import "./Insights.css";

function Insights({ insights }) {
  if (!insights || insights.length === 0) return null;

  return (
    <div className="insights-container">

      <h2 className="insights-title">
        💡 Business Insights
      </h2>

      <div className="insights-grid">

        {insights.map((item, index) => (
          <div className="insight-card" key={index}>
            <span className="insight-icon">💡</span>

            <p>{item}</p>
          </div>
        ))}

      </div>

    </div>
  );
}

export default Insights;