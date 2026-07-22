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

        <span className="upload-badge">
          DATA IMPORT
        </span>

        <h2>Upload Your Dataset</h2>

        <p>
          Upload any CSV dataset and InsightAI will automatically clean,
          analyze, visualize and generate AI-powered business insights.
        </p>

      </div>

      <div className="upload-card">

        <label className="file-box">

          <div className="cloud-circle">
              ☁️
          </div>

          <h3>Drag & Drop your CSV here</h3>

          <p>
            or click to browse from your computer
          </p>

          <input
            type="file"
            accept=".csv"
            hidden
            onChange={(e)=>setFile(e.target.files[0])}
          />

        </label>

        {file && (

          <div className="selected-file">

            <div className="csv-icon">
                📄
            </div>

            <div className="file-info">

                <h4>{file.name}</h4>

                <span>
                    CSV File • {(file.size/1024).toFixed(2)} KB
                </span>

            </div>

            <div className="success-icon">

                ✓

            </div>

          </div>

        )}

        <button

            className="upload-btn"

            disabled={loading}

            onClick={handleUpload}

        >

            {loading ? "Analyzing Dataset..." : "Analyze Dataset"}

        </button>

        {loading && (

            <div className="loading">

                <div className="loader"></div>

                <span>
                    AI is analyzing your dataset...
                </span>

            </div>

        )}

      </div>

    </section>

  );

}

export default Upload;