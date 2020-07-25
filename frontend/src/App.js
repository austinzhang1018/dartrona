import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';

function App() {
  const submitQuestion = async (data) => {
    console.log(data);
    const url = 'localhost:8000/api-qa' // 'https://dartrona.herokuapp.com/'
    const response = await axios.post(url, {question})
  }

  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("Your answer will appear here after asking a question.")

  return (
    <div className="App">
      <input type="text" name="question" onChange={(event) => {
        setQuestion(event.target.value)
      }}></input>
      <button onClick={async () => {
        setAnswer(await submitQuestion(question).data)
      }}>submit</button>
      <p>{answer}</p>
    </div>
  );
}

export default App;
