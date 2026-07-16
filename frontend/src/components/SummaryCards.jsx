import "./SummaryCards.css";

function SummaryCards({ data }) {
  if (!data) return null;

  const profile = data.dataset_profile;
  const cleaning = data.cleaning_summary;

  return (
    <div className="summary-grid">

      <div className="card">
        <h3>Total Rows</h3>
        <p>{profile.rows}</p>
      </div>

      <div className="card">
        <h3>Total Columns</h3>
        <p>{profile.columns}</p>
      </div>

      <div className="card">
        <h3>Duplicate Rows</h3>
        <p>{profile.duplicate_rows}</p>
      </div>

      <div className="card">
        <h3>Memory Usage</h3>
        <p>{profile.memory_usage_kb} KB</p>
      </div>

      <div className="card">
        <h3>Cleaned Rows</h3>
        <p>{cleaning.cleaned_rows}</p>
      </div>

      <div className="card">
        <h3>Duplicates Removed</h3>
        <p>{cleaning.duplicates_removed}</p>
      </div>

    </div>
  );
}

export default SummaryCards;