import "./Insights.css";

function Insights({ insights }) {
  if (!insights || insights.length === 0) return null;

  return (
    <div className="insights-container">

      <h2 className="insights-title">
        💡 Business Insights
      </h2>

      <p className="insights-subtitle">
        AI-generated insights extracted from your dataset.
      </p>

      <div className="insights-grid">

        {insights.map((item, index) => (

          <div className="insight-card" key={index}>

            <div className="insight-icon">
              💡
            </div>

            <div className="insight-content">

              <div className="insight-heading">
                {item.title}
              </div>

              <p>
                {item.description}
              </p>

            </div>

          </div>

        ))}

      </div>

    </div>
  );
}

export default Insights;