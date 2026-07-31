import { useState } from "react";
import "./Dashboard.css";

import SummaryCards from "./SummaryCards";
import Insights from "./Insights";
import Charts from "./Charts";
import Report from "./Report";
import Outliers from "./Outliers";

function Dashboard({ data }) {

  const [activeTab, setActiveTab] = useState("overview");

  if (!data) return null;

  return (

    <div className="dashboard-container">

      {/* =====================================================
          DASHBOARD HEADER
      ===================================================== */}

      <div className="dashboard-header">

        <div>

          <h1 className="dashboard-title">
            InsightAI Dashboard
          </h1>

          <p className="dashboard-subtitle">
            AI Powered Business Intelligence & Data Analytics
          </p>

        </div>

        <div className="dashboard-badge">
          <span className="status-dot"></span>
          Dataset Loaded
        </div>

      </div>


      {/* =====================================================
          DASHBOARD NAVIGATION
      ===================================================== */}

      <div className="dashboard-nav">

        <button
          className={activeTab === "overview" ? "nav-btn active" : "nav-btn"}
          onClick={() => setActiveTab("overview")}
        >
          📊 Overview
        </button>

        <button
          className={activeTab === "insights" ? "nav-btn active" : "nav-btn"}
          onClick={() => setActiveTab("insights")}
        >
          💡 Insights
        </button>

        <button
          className={activeTab === "outliers" ? "nav-btn active" : "nav-btn"}
          onClick={() => setActiveTab("outliers")}
        >
          🔍 Outliers
        </button>

        <button
          className={activeTab === "visualizations" ? "nav-btn active" : "nav-btn"}
          onClick={() => setActiveTab("visualizations")}
        >
          📈 Visualizations
        </button>

        <button
          className={activeTab === "report" ? "nav-btn active" : "nav-btn"}
          onClick={() => setActiveTab("report")}
        >
          📄 Report
        </button>

      </div>


      {/* =====================================================
          OVERVIEW
      ===================================================== */}

      {activeTab === "overview" && (

        <div className="dashboard-content">

          <section className="dashboard-section">

            <div className="section-heading">

              <div>
                <span className="section-label">
                  DATASET
                </span>

                <h2>
                  📊 Dataset Summary
                </h2>
              </div>

            </div>

            <SummaryCards
              profile={data.dataset_profile}
              cleaning={data.cleaning_summary}
            />

          </section>


          {/* Quick insights preview */}

          <section className="dashboard-section">

            <div className="section-heading">

              <div>
                <span className="section-label">
                  AI ANALYSIS
                </span>

                <h2>
                  💡 Business Insights
                </h2>
              </div>

              <button
                className="view-section-btn"
                onClick={() => setActiveTab("insights")}
              >
                View All →
              </button>

            </div>

            <Insights
              insights={data.business_insights?.slice(0, 4)}
            />

          </section>

        </div>

      )}


      {/* =====================================================
          INSIGHTS
      ===================================================== */}

      {activeTab === "insights" && (

        <div className="dashboard-content">

          <section className="dashboard-section">

            <div className="section-heading">

              <div>
                <span className="section-label">
                  AI ANALYSIS
                </span>

                <h2>
                  💡 Business Insights
                </h2>
              </div>

            </div>

            <Insights
              insights={data.business_insights}
            />

          </section>

        </div>

      )}


      {/* =====================================================
          OUTLIERS
      ===================================================== */}

      {activeTab === "outliers" && (

        <div className="dashboard-content">

          <section className="dashboard-section">

            <div className="section-heading">

              <div>
                <span className="section-label">
                  DATA QUALITY
                </span>

                <h2>
                  🔍 Outlier Detection
                </h2>
              </div>

            </div>

            <Outliers
              outliers={data.eda?.outlier_summary}
            />

          </section>

        </div>

      )}


      {/* =====================================================
          VISUALIZATIONS
      ===================================================== */}

      {activeTab === "visualizations" && (

        <div className="dashboard-content">

          <section className="dashboard-section">

            <div className="section-heading">

              <div>
                <span className="section-label">
                  DATA VISUALIZATION
                </span>

                <h2>
                  📈 Data Visualizations
                </h2>
              </div>

            </div>

            <Charts
              charts={data.generated_charts}
            />

          </section>

        </div>

      )}


      {/* =====================================================
          REPORT
      ===================================================== */}

      {activeTab === "report" && (

        <div className="dashboard-content">

          <section className="dashboard-section">

            <div className="section-heading">

              <div>
                <span className="section-label">
                  REPORT
                </span>

                <h2>
                  📄 Executive Report
                </h2>

              </div>

            </div>

            <Report
              report={data.report}
            />

          </section>

        </div>

      )}

    </div>

  );
}

export default Dashboard;