import React, { useState } from "react";
import { registerdoc } from "../services/Apis";
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
const Home = () => {
  const [mintAddress, setMintAddress] = useState("");
  const [score, setScore] = useState(null);
  

  // const handleSubmit = async () => {
  //   // Simulate API request (Replace with actual API call)
  //   const fakeScore = Math.floor(Math.random() * 10) + 1;
  //   setScore(fakeScore);
  // };

  const handleSubmit = async (e) => {
          e.preventDefault();
  
  
          if (mintAddress === "") {
              toast.error("mintAddress is Required!");
          } else {
              const data = {mintAddress};
  
              const config = {
                  "Content-Type": "application/json"
              }
  
              const response = await registerdoc(data, config);
  
              if (response.status === 201) {
                  toast.success("Api fetched");
                  setScore(response.data.processed)
                  console.log(response)
              } else {
                  toast.error("somethine went wrong");
              }
          }
      }

  return (
    <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", height: "100vh", backgroundColor: "#f4f4f4", padding: "20px" }}>
      <h1 style={{ marginBottom: "20px", fontSize: "24px" }}>NFT Fraud Score Checker</h1>
      <input
        type="text"
        placeholder="Enter Mint Address"
        value={mintAddress}
        onChange={(e) => setMintAddress(e.target.value)}
        style={{ padding: "10px", width: "300px", marginBottom: "20px", borderRadius: "5px", border: "1px solid #ccc" }}
      />
      <button
        onClick={handleSubmit}
        style={{ padding: "10px 20px", backgroundColor: "#007bff", color: "white", border: "none", borderRadius: "5px", cursor: "pointer" }}
      >
        Check Score
      </button>
      {score !== null && (
        <div style={{ marginTop: "20px", padding: "20px", backgroundColor: "white", borderRadius: "10px", boxShadow: "0px 4px 10px rgba(0, 0, 0, 0.1)", textAlign: "center" }}>
          <h2>Fraud Score</h2>
          <p style={{ fontSize: "20px", fontWeight: "bold", color: score < 5 ? "red" : "green" }}>{score} / 100</p>
        </div>
      )}
    </div>
  );



};

export default Home;
