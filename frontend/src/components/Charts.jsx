function Charts({ charts }) {
  if (!charts || charts.length === 0) return null;

  return (
    <div style={{ marginTop: "40px" }}>
      <h2>Generated Charts</h2>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit, minmax(300px,1fr))",
          gap: "20px",
        }}
      >
        {charts.map((chart, index) => (
          <div
            key={index}
            style={{
              border: "1px solid #ddd",
              borderRadius: "10px",
              padding: "15px",
              textAlign: "center",
            }}
          >
            <h4>{chart}</h4>

            <img
              src={`http://127.0.0.1:8000/reports/${chart}`}
              alt={chart}
              style={{
                width: "100%",
                borderRadius: "8px",
              }}
            />
          </div>
        ))}
      </div>
    </div>
  );
}

export default Charts;