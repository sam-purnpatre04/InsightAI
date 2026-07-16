function Insights({ insights }) {
  if (!insights || insights.length === 0) {
    return null;
  }

  return (
    <div
      style={{
        background: "#ffffff",
        padding: "20px",
        borderRadius: "10px",
        boxShadow: "0 2px 8px rgba(0,0,0,0.1)",
        marginBottom: "30px",
      }}
    >
      <h2>Business Insights</h2>

      <ul>
        {insights.map((insight, index) => (
          <li
            key={index}
            style={{
              marginBottom: "10px",
              fontSize: "16px",
            }}
          >
            {insight}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Insights;