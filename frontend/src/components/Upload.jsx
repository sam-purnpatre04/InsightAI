import { useState } from "react";
import { uploadDataset } from "../services/api";
import "./Upload.css";

function Upload({ setData }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a CSV file.");
      return;
    }

    try {
      setLoading(true);

      const result = await uploadDataset(file);

      setData(result);
    } catch (error) {
      console.error(error);
      alert("Upload failed.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="upload-container">
      <h2 className="upload-title">📂 Upload Your Dataset</h2>

      <p className="upload-subtitle">
        Upload a CSV dataset and let InsightAI generate
        automatic reports, charts and business insights.
      </p>

      <div className="file-box">
        <h3>Choose a CSV File</h3>

        <input
          className="file-input"
          type="file"
          accept=".csv"
          onChange={(e) => setFile(e.target.files[0])}
        />

        {file && (
          <p className="file-name">
            📄 {file.name}
          </p>
        )}
      </div>

      <button
        className="upload-btn"
        onClick={handleUpload}
        disabled={loading}
      >
        {loading ? "Analyzing Dataset..." : "Analyze Dataset"}
      </button>

      {loading && (
        <p className="loading">
          ⏳ Please wait while AI analyzes your dataset...
        </p>
      )}
    </div>
  );
}

export default Upload;