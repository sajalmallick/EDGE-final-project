import { useState } from 'react';
import axios from 'axios';

export default function Query() {
  const [input, setInput] = useState("");
  const [result, setResult] = useState("");

  const handleQuery = async () => {
    const res = await axios.get(`http://127.0.0.1:8000/ask?q=${input}`);
    setResult(res.data.prediction);
  };

  return (
    <div>
      <h1>Ask a Question</h1>
      <input
        type="text"
        placeholder='e.g. [5.1, 3.5, 1.4, 0.2]'
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />
      <button onClick={handleQuery}>Submit</button>
      <p>Prediction: {result}</p>
    </div>
  );
}
