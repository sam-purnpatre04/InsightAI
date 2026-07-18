import "./Dashboard.css";

import SummaryCards from "./SummaryCards";
import Insights from "./Insights";
import Charts from "./Charts";
import Report from "./Report";

function Dashboard({ data }) {
  if (!data) return null;

  return (
    <div className="dashboard-container">

      <h1 className="dashboard-title">
        📊 InsightAI Dashboard
      </h1>

      <SummaryCards
        profile={data.dataset_profile}
        cleaning={data.cleaning_summary}
      />

      <Insights insights={data.business_insights} />

      <Charts charts={data.generated_charts} />

      <Report report={data.report} />

    </div>
  );
}

export default Dashboard;