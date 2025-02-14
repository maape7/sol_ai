import React, { useState } from "react";
import { registerdoc } from "../services/Apis";
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
const Home = () => {
  const [mintAddress, setMintAddress] = useState("");
  const [score, setScore] = useState(null);
  const [metadata, setMetadata] = useState(null)
  const [isLoading, setIsLoading] = useState(false);

  // const handleSubmit = async () => {
  //   // Simulate API request (Replace with actual API call)
  //   const fakeScore = Math.floor(Math.random() * 10) + 1;
  //   setScore(fakeScore);
  // };

  const handleSubmit = async (e) => {
    setIsLoading(true);
    e.preventDefault();

    if (mintAddress === "") {
        toast.error("Mint address is required!");
        return;
    }

    const data = { mintAddress };
    const config = {
        "Content-Type": "application/json"
    };

    try {
        const response = await registerdoc(data, config);

        if (response.status === 201) {
            setIsLoading(false);
            toast.success("NFT metadata & Scam analysis fetched successfully!");
            console.log("NFT Metadata:", response.data.metadata);
            console.log("Fraud Analysis Result:", response.data.fraudAnalysis.processed);

            setMetadata(response.data.metadata);
            setScore(response.data.fraudAnalysis.processed);
        } else {
          setIsLoading(false);
            toast.error("Unexpected server response. Please try again.");
        }
    } catch (error) {
        setIsLoading(false);
        console.error("Error fetching NFT data:", error);
        toast.error("Server error or NFT not fetched from Solana.");
    }
};


  return (
<div className="min-h-screen bg-gradient-to-br from-gray-900 to-black text-white p-8">
  <div className="max-w-6xl mx-auto space-y-8">
    {/* Header Section */}
    <div className="bg-gray-800 p-6 rounded-xl border border-gray-700 shadow-2xl">
      <h1 className="text-4xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-500 text-center mb-2">
        Solana NFT Scam Detector (AI Powered)
      </h1>
      <p className="text-gray-400 text-center text-sm">
        Analyze NFT projects for potential scam risks and scam indicators
      </p>
    </div>

    {/* Input Section */}
    <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
      <div className="lg:col-span-2 bg-gray-800 p-6 rounded-xl border border-gray-700 shadow-xl">
        <div className="space-y-6">
          <div className="space-y-2">
            <label className="block text-sm font-semibold text-gray-300 mb-2">
              Solana NFT Mint Address
            </label>
            <div className="flex gap-4">
              <input
                type="text"
                placeholder="Enter Solana NFT Mint Address..."
                value={mintAddress}
                onChange={(e) => setMintAddress(e.target.value)}
                className="w-full px-4 py-3 border border-gray-600 bg-gray-700 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-blue-400 transition-all duration-300"
                disabled={isLoading} // Disable input during loading
              />
              <button
                onClick={handleSubmit}
                disabled={isLoading}
                className={`px-8 py-3 bg-blue-500 hover:bg-blue-600 transition-all text-white font-semibold rounded-lg shadow-md transform hover:scale-105 whitespace-nowrap ${
                  isLoading ? 'opacity-75 cursor-not-allowed' : ''
                }`}
              >
                {isLoading ? 'Analyzing...' : 'Analyze'}
              </button>
            </div>
          </div>

          {/* Loading State */}
          {isLoading && (
            <div className="mt-6 p-6 bg-gray-700 rounded-xl border border-gray-600 flex flex-col items-center justify-center space-y-3">
              <svg
                className="animate-spin h-8 w-8 text-blue-400"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
              >
                <circle
                  className="opacity-25"
                  cx="12"
                  cy="12"
                  r="10"
                  stroke="currentColor"
                  strokeWidth="4"
                ></circle>
                <path
                  className="opacity-75"
                  fill="currentColor"
                  d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                ></path>
              </svg>
              <p className="text-gray-300 text-sm">Analyzing NFT mint address...</p>
            </div>
          )}

          {/* Results Section */}
          {!isLoading && metadata && score !== null && (
            <div className="space-y-6">
              {/* NFT Metadata Grid */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="bg-gray-700 p-4 rounded-lg border border-gray-600">
                  <h3 className="text-sm font-semibold text-gray-300 mb-2">Mint Address</h3>
                  <p className="text-blue-300 text-sm break-all">{mintAddress}</p>
                </div>
                
                <div className="bg-gray-700 p-4 rounded-lg border border-gray-600">
                  <h3 className="text-sm font-semibold text-gray-300 mb-2">External URL</h3>
                  {metadata.external_url ? (
                    <a
                      href={metadata.external_url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-white hover:underline text-sm block truncate"
                    >
                      {metadata.external_url}
                    </a>
                  ) : (
                    <span className="text-red-400 text-sm">No external URL detected</span>
                  )}
                </div>
                
                <div className="md:col-span-2 bg-gray-700 p-4 rounded-lg border border-gray-600">
                  <h3 className="text-sm font-semibold text-gray-300 mb-2">Description</h3>
                  <p className="text-yellow-300 text-sm">
                    {metadata.description || "No description available"}
                  </p>
                </div>
              </div>
            </div>
          )}
        </div>
      </div>

      {/* Score Card */}
      {!isLoading && metadata && score !== null && (
        <div className="bg-gray-800 p-6 rounded-xl border border-gray-700 shadow-xl h-fit sticky top-8">
          <div className="space-y-4">
            <h2 className="text-xl font-semibold text-center mb-4">Security Overview</h2>
            <div className={`p-6 rounded-xl transition-all duration-300 ${
              score > 50 ? "bg-red-900/30 border-red-700" : "bg-green-900/30 border-green-700"
            } border`}>
              <p className="text-center text-sm text-gray-300 mb-2">Scam Risk Score</p>
              <p className={`text-center text-5xl font-bold ${
                score > 50 ? "text-red-400" : "text-green-400"
              } animate-pulse`}>
                {score}
                <span className="text-2xl text-gray-400">/100</span>
              </p>
            </div>
            <div className="bg-gray-700 p-4 rounded-lg">
              <h3 className="text-sm font-semibold text-gray-300 mb-2">Recommendation</h3>
              <p className="text-sm text-gray-400">
                {score > 50 
                  ? "Exercise extreme caution - multiple risk factors detected"
                  : "No critical issues found - standard precautions recommended"}
              </p>
            </div>
          </div>
        </div>
      )}
    </div>
  </div>
</div>
  

  );



};

export default Home;
