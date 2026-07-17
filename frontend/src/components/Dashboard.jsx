import SummaryCards from "./SummaryCards";
import Insights from "./Insights";
import Charts from "./Charts";

function Dashboard({ data }) {
  if (!data) return null;

  return (
    <div style={{ marginTop: "30px" }}>

      <h1
        style={{
          textAlign: "center",
          marginBottom: "30px",
          color: "#2c3e50",
        }}
      >
        InsightAI Dashboard
      </h1>

      {/* Summary Cards */}
      <SummaryCards
        profile={data.dataset_profile}
        cleaning={data.cleaning_summary}
      />

      {/* Business Insights */}
      <Insights insights={data.business_insights} />

      {/* Charts */}
      <Charts charts={data.generated_charts} />

    </div>
  );
}

export default Dashboard;