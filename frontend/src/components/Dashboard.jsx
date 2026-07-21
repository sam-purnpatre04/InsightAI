import "./Dashboard.css";

import SummaryCards from "./SummaryCards";
import Insights from "./Insights";
import Charts from "./Charts";
import Report from "./Report";

function Dashboard({ data }) {
  if (!data) return null;

  return (
    <div className="dashboard-container">

      <div className="dashboard-header">

        <div>
          <h1 className="dashboard-title">
            📊 InsightAI Dashboard
          </h1>

          <p className="dashboard-subtitle">
            AI Powered Business Intelligence & Data Analytics
          </p>
        </div>

        <div className="dashboard-badge">
          Dataset Loaded
        </div>

      </div>

      <section className="section">

        <h2>📈 Dataset Summary</h2>

        <SummaryCards
          profile={data.dataset_profile}
          cleaning={data.cleaning_summary}
        />

      </section>

      <section className="section">

        <h2>💡 Business Insights</h2>

        <Insights
          insights={data.business_insights}
        />

      </section>

      <section className="section">

        <h2>📊 Data Visualizations</h2>

        <Charts
          charts={data.generated_charts}
        />

      </section>

      <section className="section">

        <h2>📄 Executive Report</h2>

        <Report
          report={data.report}
        />

      </section>

    </div>
  );
}

export default Dashboard;