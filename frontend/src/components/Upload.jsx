import { useState } from "react";
import { uploadDataset } from "../services/api";

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
    <div
      style={{
        marginBottom: "30px",
        textAlign: "center",
      }}
    >
      <input
        type="file"
        accept=".csv"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br />
      <br />

      <button onClick={handleUpload}>
        {loading ? "Analyzing..." : "Analyze Dataset"}
      </button>
    </div>
  );
}

export default Upload;