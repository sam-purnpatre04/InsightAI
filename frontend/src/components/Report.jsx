import "./Report.css";

function Report({ report }) {
  if (!report) return null;

  return (
    <div className="report-container">

      <h2 className="report-title">
        📄 Analysis Report
      </h2>

      <div className="report-grid">

        <div className="report-card">
          <h3>📊 Dataset Overview</h3>

          <p><strong>Rows:</strong> {report.dataset_overview.rows}</p>

          <p><strong>Columns:</strong> {report.dataset_overview.columns}</p>

          <p><strong>Memory:</strong> {report.dataset_overview.memory_usage_kb} KB</p>
        </div>

        <div className="report-card">
          <h3>🧹 Data Quality</h3>

          <p>
            <strong>Duplicate Rows:</strong>{" "}
            {report.data_quality.duplicate_rows}
          </p>

          <p>
            <strong>Cleaned Rows:</strong>{" "}
            {report.data_quality.cleaned_rows}
          </p>

          <p>
            <strong>Duplicates Removed:</strong>{" "}
            {report.data_quality.duplicates_removed}
          </p>
        </div>

      </div>

      <div className="summary-box">

        <h3>📝 Executive Summary</h3>

        <ul>

          {report.report_summary.map((item, index) => (

            <li key={index}>{item}</li>

          ))}

        </ul>

      </div>

    </div>
  );
}

export default Report;