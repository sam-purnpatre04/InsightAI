import html2canvas from "html2canvas";
import jsPDF from "jspdf";
import "./Report.css";

function Report({ report, data }) {

  if (!report || !data) return null;

  const downloadPDF = async () => {

    const reportElement = document.getElementById("pdf-report");

    if (!reportElement) return;

    try {

      const button = document.querySelector(".pdf-btn");

      if (button) {
        button.disabled = true;
        button.innerText = "Generating PDF...";
      }

      const canvas = await html2canvas(reportElement, {
        scale: 2,
        useCORS: true,
        backgroundColor: "#f8fafc",
        logging: false
      });

      const imgData = canvas.toDataURL("image/png");

      const pdf = new jsPDF(
        "p",
        "mm",
        "a4"
      );

      const pdfWidth =
        pdf.internal.pageSize.getWidth();

      const pdfHeight =
        pdf.internal.pageSize.getHeight();

      const margin = 8;

      const contentWidth =
        pdfWidth - margin * 2;

      const imgHeight =
        (canvas.height * contentWidth) /
        canvas.width;

      let heightLeft = imgHeight;

      let position = margin;

      /* -----------------------------------------
         FIRST PAGE
      ----------------------------------------- */

      pdf.addImage(
        imgData,
        "PNG",
        margin,
        position,
        contentWidth,
        imgHeight
      );

      heightLeft -=
        pdfHeight - margin * 2;


      /* -----------------------------------------
         ADDITIONAL PAGES
      ----------------------------------------- */

      while (heightLeft > 0) {

        position =
          heightLeft -
          imgHeight +
          margin;

        pdf.addPage();

        pdf.addImage(
          imgData,
          "PNG",
          margin,
          position,
          contentWidth,
          imgHeight
        );

        heightLeft -=
          pdfHeight - margin * 2;

      }


      /* -----------------------------------------
         SAVE
      ----------------------------------------- */

      pdf.save(
        "InsightAI_Complete_Analysis_Report.pdf"
      );


      if (button) {

        button.disabled = false;

        button.innerText =
          "📥 Download Complete PDF";

      }

    } catch (error) {

      console.error(
        "PDF generation failed:",
        error
      );

      alert(
        "Unable to generate PDF."
      );

      const button =
        document.querySelector(".pdf-btn");

      if (button) {

        button.disabled = false;

        button.innerText =
          "📥 Download Complete PDF";

      }

    }

  };


  return (

    <div className="report-container">


      {/* ==========================================
          REPORT HEADER
      ========================================== */}

      <div className="report-header">

        <div>

          <span className="report-badge">
            ANALYTICAL REPORT
          </span>

          <h2 className="report-title">
            📄 InsightAI Analysis Report
          </h2>

          <p className="report-subtitle">
            Complete business intelligence analysis
            generated from your dataset.
          </p>

        </div>


        <button
          className="pdf-btn"
          onClick={downloadPDF}
        >

          📥 Download Complete PDF

        </button>

      </div>


      {/* ==========================================
          EVERYTHING INSIDE THIS DIV
          WILL GO INTO THE PDF
      ========================================== */}

      <div id="pdf-report">


        {/* ==========================================
            BRAND HEADER
        ========================================== */}

        <div className="pdf-brand">

          <h1>
            InsightAI
          </h1>

          <p>
            AI Powered Business Intelligence
            & Data Analytics
          </p>

        </div>


        {/* ==========================================
            DATASET OVERVIEW
        ========================================== */}

        <div className="report-section">

          <h2>
            📊 Dataset Overview
          </h2>

          <div className="report-grid">

            <div className="report-card">

              <h3>Total Rows</h3>

              <p className="big-value">
                {data.dataset_profile?.rows ?? "-"}
              </p>

            </div>


            <div className="report-card">

              <h3>Total Columns</h3>

              <p className="big-value">
                {data.dataset_profile?.columns ?? "-"}
              </p>

            </div>


            <div className="report-card">

              <h3>Memory Usage</h3>

              <p className="big-value">

                {data.dataset_profile?.memory_usage_kb ?? "-"}
                {" "}KB

              </p>

            </div>

          </div>

        </div>


        {/* ==========================================
            DATA QUALITY
        ========================================== */}

        <div className="report-section">

          <h2>
            🧹 Data Quality
          </h2>

          <div className="report-grid">

            <div className="report-card">

              <h3>Duplicate Rows</h3>

              <p className="big-value">

                {report.data_quality?.duplicate_rows ?? 0}

              </p>

            </div>


            <div className="report-card">

              <h3>Duplicates Removed</h3>

              <p className="big-value">

                {report.data_quality?.duplicates_removed ?? 0}

              </p>

            </div>


            <div className="report-card">

              <h3>Cleaned Rows</h3>

              <p className="big-value">

                {report.data_quality?.cleaned_rows ?? "-"}

              </p>

            </div>

          </div>

        </div>


        {/* ==========================================
            BUSINESS INSIGHTS
        ========================================== */}

        <div className="report-section">

          <h2>
            💡 Business Insights
          </h2>

          <div className="pdf-insights">

            {data.business_insights?.map(
              (item, index) => (

                <div
                  className="pdf-insight"
                  key={index}
                >

                  <div className="pdf-insight-icon">
                    💡
                  </div>

                  <div>

                    <h3>
                      {item.title}
                    </h3>

                    <p>
                      {item.description}
                    </p>

                  </div>

                </div>

              )
            )}

          </div>

        </div>


        {/* ==========================================
            OUTLIERS
        ========================================== */}

        <div className="report-section">

          <h2>
            🔍 Outlier Analysis
          </h2>

          {data.eda?.outlier_summary &&
           Object.keys(
             data.eda.outlier_summary
           ).length > 0 ? (

            <div className="outlier-table">

              <div className="outlier-row outlier-header">

                <span>Column</span>

                <span>Outliers</span>

                <span>Percentage</span>

              </div>


              {Object.entries(
                data.eda.outlier_summary
              ).map(
                ([column, info]) => (

                  <div
                    className="outlier-row"
                    key={column}
                  >

                    <span>
                      {column}
                    </span>

                    <span>
                      {info.count ??
                       info.outliers ??
                       0}
                    </span>

                    <span>

                      {info.percentage !== undefined
                        ? `${info.percentage}%`
                        : "-"}

                    </span>

                  </div>

                )
              )}

            </div>

          ) : (

            <div className="empty-analysis">

              No outlier information
              available for this dataset.

            </div>

          )}

        </div>


        {/* ==========================================
            EXECUTIVE SUMMARY
        ========================================== */}

        <div className="report-section">

          <h2>
            📝 Executive Summary
          </h2>

          <div className="summary-box">

            <ul>

              {report.report_summary?.map(
                (item, index) => (

                  <li key={index}>
                    {item}
                  </li>

                )
              )}

            </ul>

          </div>

        </div>


        {/* ==========================================
            VISUAL ANALYSIS
        ========================================== */}

        <div className="report-section">

          <h2>
            📈 Visual Analysis
          </h2>

          <p className="section-description">

            Visualizations generated automatically
            from the uploaded dataset.

          </p>


          <div className="pdf-charts">

            {data.generated_charts?.map(
              (chart, index) => (

                <div
                  className="pdf-chart"
                  key={index}
                >

                  <h3>

                    {chart
                      .replace(".png", "")
                      .replaceAll("_", " ")
                      .replace(
                        /\b\w/g,
                        c => c.toUpperCase()
                      )}

                  </h3>

                  <img
                    src={`http://127.0.0.1:8000/reports/${chart}`}
                    alt={chart}
                    crossOrigin="anonymous"
                  />

                </div>

              )
            )}

          </div>

        </div>


        {/* ==========================================
            FOOTER
        ========================================== */}

        <div className="pdf-footer">

          <p>
            Generated by InsightAI
          </p>

          <p>
            AI Powered Business Intelligence
            & Data Analytics Platform
          </p>

        </div>


      </div>

    </div>

  );

}

export default Report;