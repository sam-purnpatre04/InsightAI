function Report({ report }) {
  if (!report) return null;

  return (
    <div
      style={{
        background: "#fff",
        marginTop: "30px",
        padding: "25px",
        borderRadius: "12px",
        boxShadow: "0 4px 12px rgba(0,0,0,0.08)",
      }}
    >
      <h2>📄 AI Report Summary</h2>

      {report.report_summary.map((item, index) => (
        <p key={index}>• {item}</p>
      ))}
    </div>
  );
}

export default Report;