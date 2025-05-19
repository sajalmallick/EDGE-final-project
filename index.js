import { useState } from 'react';
import axios from 'axios';

export default function Home() {
  const [message, setMessage] = useState("");

  const handleUpload = async (e) => {
    e.preventDefault();
    const file = e.target.file.files[0];
    const formData = new FormData();
    formData.append("file", file);

    const res = await axios.post("http://127.0.0.1:8000/learn", formData);
    setMessage(res.data.message);
  };

  return (
    <div>
      <h1>Upload CSV File to Train Model</h1>
      <form onSubmit={handleUpload}>
        <input type="file" name="file" accept=".csv" />
        <button type="submit">Upload and Train</button>
      </form>
      <p>{message}</p>
    </div>
  );
}
