import html2canvas from "html2canvas";
import jsPDF from "jspdf";
import "./Report.css";

function Report({ report }) {
  if (!report) return null;

  const downloadPDF = async () => {
    const reportElement = document.getElementById("pdf-report");

    if (!reportElement) return;

    try {
      const canvas = await html2canvas(reportElement, {
        scale: 2,
        useCORS: true,
        backgroundColor: "#f8fafc",
      });

      const imgData = canvas.toDataURL("image/png");

      const pdf = new jsPDF("p", "mm", "a4");

      const pdfWidth = pdf.internal.pageSize.getWidth();
      const pdfHeight = pdf.internal.pageSize.getHeight();

      const imgWidth = pdfWidth;
      const imgHeight =
        (canvas.height * imgWidth) / canvas.width;

      let heightLeft = imgHeight;
      let position = 0;

      pdf.addImage(
        imgData,
        "PNG",
        0,
        position,
        imgWidth,
        imgHeight
      );

      heightLeft -= pdfHeight;

      while (heightLeft > 0) {
        position = heightLeft - imgHeight;

        pdf.addPage();

        pdf.addImage(
          imgData,
          "PNG",
          0,
          position,
          imgWidth,
          imgHeight
        );

        heightLeft -= pdfHeight;
      }

      pdf.save("InsightAI_Analysis_Report.pdf");

    } catch (error) {
      console.error("PDF generation failed:", error);
      alert("Unable to generate PDF.");
    }
  };

  return (
    <div className="report-container">

      <div className="report-header">

        <div>
          <h2 className="report-title">
            📄 Analysis Report
          </h2>

          <p className="report-subtitle">
            Executive summary of your dataset analysis
          </p>
        </div>

        <button
          className="pdf-btn"
          onClick={downloadPDF}
        >
          📥 Download PDF Report
        </button>

      </div>

      <div id="pdf-report">

        <div className="report-grid">

          <div className="report-card">

            <h3>📊 Dataset Overview</h3>

            <p>
              <strong>Rows:</strong>{" "}
              {report.dataset_overview.rows}
            </p>

            <p>
              <strong>Columns:</strong>{" "}
              {report.dataset_overview.columns}
            </p>

            <p>
              <strong>Memory:</strong>{" "}
              {report.dataset_overview.memory_usage_kb} KB
            </p>

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

              <li key={index}>
                {item}
              </li>

            ))}

          </ul>

        </div>

      </div>

    </div>
  );
}

export default Report;