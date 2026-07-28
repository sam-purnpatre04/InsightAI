import "./Outliers.css";

function Outliers({ outliers }) {

  if (!outliers || Object.keys(outliers).length === 0) {
    return (
      <div className="outlier-empty">
        <div className="outlier-empty-icon">✅</div>

        <h3>No Outlier Analysis Available</h3>

        <p>
          No numerical columns were available for outlier detection.
        </p>
      </div>
    );
  }

  const getSeverity = (percentage) => {

    if (percentage >= 5) {
      return {
        label: "High",
        className: "severity-high"
      };
    }

    if (percentage >= 2) {
      return {
        label: "Moderate",
        className: "severity-medium"
      };
    }

    return {
      label: "Low",
      className: "severity-low"
    };
  };

  return (
    <div className="outliers-container">

      <div className="outliers-header">

        <span className="outlier-badge">
          STATISTICAL ANALYSIS
        </span>

        <h2>🚨 Outlier Detection</h2>

        <p>
          InsightAI uses the IQR method to identify unusual
          observations in numerical columns.
        </p>

      </div>

      <div className="outliers-grid">

        {Object.entries(outliers).map(
          ([column, stats]) => {

            const severity = getSeverity(
              stats.outlier_percentage
            );

            return (

              <div
                className="outlier-card"
                key={column}
              >

                <div className="outlier-card-header">

                  <h3>
                    {column}
                  </h3>

                  <span
                    className={`severity ${severity.className}`}
                  >
                    {severity.label}
                  </span>

                </div>

                <div className="outlier-main">

                  <div>

                    <span className="outlier-number">
                      {stats.outlier_count}
                    </span>

                    <span className="outlier-label">
                      Outliers Detected
                    </span>

                  </div>

                  <div className="outlier-percentage">

                    {stats.outlier_percentage}%

                  </div>

                </div>

                <div className="outlier-details">

                  <div>
                    <span>Q1</span>
                    <strong>{stats.q1}</strong>
                  </div>

                  <div>
                    <span>Q3</span>
                    <strong>{stats.q3}</strong>
                  </div>

                  <div>
                    <span>IQR</span>
                    <strong>{stats.iqr}</strong>
                  </div>

                </div>

                <div className="outlier-bounds">

                  <p>
                    Lower Bound:
                    <strong>
                      {stats.lower_bound}
                    </strong>
                  </p>

                  <p>
                    Upper Bound:
                    <strong>
                      {stats.upper_bound}
                    </strong>
                  </p>

                </div>

              </div>

            );
          }
        )}

      </div>

    </div>
  );
}

export default Outliers;