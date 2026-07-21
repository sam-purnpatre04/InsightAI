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
    <section className="upload-container">

      <div className="upload-header">

        <h2>📂 Upload Dataset</h2>

        <p>
          Upload any CSV dataset and let InsightAI automatically clean,
          analyze, visualize and generate business insights.
        </p>

      </div>

      <div className="upload-card">

        <label className="file-box">

          <div className="upload-icon">
            ☁️
          </div>

          <h3>Choose CSV File</h3>

          <p>
            Click here to browse your dataset
          </p>

          <input
            type="file"
            accept=".csv"
            onChange={(e) => setFile(e.target.files[0])}
            hidden
          />

        </label>

        {file && (

          <div className="selected-file">

            <div>

              <h4>{file.name}</h4>

              <span>
                {(file.size / 1024).toFixed(2)} KB
              </span>

            </div>

            <div className="check">
              ✓
            </div>

          </div>

        )}

        <button
          className="upload-btn"
          onClick={handleUpload}
          disabled={loading}
        >
          {loading ? "Analyzing Dataset..." : "Analyze Dataset"}
        </button>

        {loading && (
          <div className="loading">

            <div className="loader"></div>

            <span>
              AI is processing your dataset...
            </span>

          </div>
        )}

      </div>

    </section>
  );
}

export default Upload;