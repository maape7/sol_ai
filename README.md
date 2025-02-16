# Solana NFT Scam Detection (AI Powered)

## Table of Contents
- [Overview](#overview)
  - [Problem](#problem)
  - [Our Project & Solution](#our-project--solution)
  - [Key Features](#key-features)
- [Impact Assessment](#impact-assessment)
  - [Protection Against Solana NFT Scams](#1-protection-against-solana-nft-scams)
  - [Increased Trust in Solana NFT Marketplaces](#2-increased-trust-in-solana-nft-marketplaces)
  - [Scalability & Adoption](#3-scalability--adoption)
  - [Future-Proof Security](#4-future-proof-security)
- [Scalable Roadmap](#scalable-roadmap)
  - [Seamless Integration](#1-seamless-integration)
  - [Expanding Data Sources](#2-expanding-data-sources)
  - [Advanced AI Models](#3-advanced-ai-models)
- [Technical Documentation](#technical-documentation)
  - [Example](#an-example)
  - [Architecture Design of MVP](#architecture-design-of-mvp)
- [AI Model Overview: Solana NFT Scam Detection (MVP)](#ai-model-overview-solana-nft-scam-detection-mvp)
  - [AI Model](#-ai-model)
  - [Heuristic-Based Detection](#-heuristic-based-detection)
  - [How It Works](#-how-it-works)
- [How It Works (MVP)](#how-it-works-mvp)
- [Example Code Snippets](#example-code-snippets)
  - [Python AI Model](#python-ai-model)
  - [Solana Metadata Fetching (TypeScript)](#solana-metadata-fetching-typescript)
- [Technology Stack](#technology-stack)
  - [Frontend](#frontend)
  - [Backend](#backend)
    - [Express.js](#expressjs)
    - [FastAPI](#fastapi)
  - [AI and Machine Learning](#ai-and-machine-learning)
  - [Installation & Setup](#installation--setup)
    - [Clone the Repository](#1-clone-the-repository)
    - [Install Dependencies](#2-install-dependencies)
      - [For Frontend (React.js)](#for-frontend-reactjs)
      - [For Backend Express.js](#for-backend-expressjs)
      - [For Backend FastAPI](#for-backend-fastapi)
    - [Run the Services](#3-run-the-services)
      - [Start Express.js API](#start-expressjs-api)
      - [Start FastAPI Server](#start-fastapi-server)
  - [Challenges & Solutions](#challenges--solutions)
  - [Contributors](#contributors)


## Overview

### Problem
NFT scams are prevalent on the **Solana blockchain**, with malicious actors using **deceptive metadata, fake domains, and phishing tactics** to trick users. (Causes millions of dollar in losses)

Identifying fraudulent NFTs in real time is challenging, as manual verification is time-consuming and unreliable.

### Our Project & Solution
This AI-powered system detects scam NFTs by analyzing their **metadata** and associated **domain (website)**. It integrates an **SGDClassifier-based machine learning model** with blockchain data from **Solana RPC** to provide a **real-time scam risk score**. 

### Key Features:
- **Real-Time Scam Detection**: Instantly evaluates NFTs to alert users of potential Scam.
- **Multi-Layered Analysis**: Assesses metadata, domain legitimacy, and other risk factors.
- **Scalable & Efficient**: Designed for easy integration and expansion across NFT marketplaces.

By leveraging **AI and Solana RPC**, our system helps users **stay aware of scams** and make informed decisions before engaging with a **Solana NFT**.

---

## **Impact Assessment**
### **1. Protection Against Solana NFT Scams**
- **Real-time scam detection** significantly reduces the risk of users purchasing fraudulent NFTs.
- Helps protect **Solana users and investors** from losing funds due to deceptive projects.
  
### **2. Increased Trust in Solana NFT Marketplaces**
- By integrating scam detection into **wallets and marketplaces**, users gain confidence in NFT transactions.
- **Enhanced due diligence** helps projects build credibility.

### **3. Scalability & Adoption**
- The **modular API design** allows for **fast integration** with existing platforms.
- Can be **adopted by exchanges, wallets, and NFT launchpads**, making the entire Solana ecosystem safer.

### **4. Future-Proof Security**
- As AI models improve, the system evolves to **detect newer scam tactics**.
- **Community-driven scam reporting** ensures **continuous updates** and better Scam detection.

---
## **Scalable Roadmap**

The scalability of this project is **Very Easy** due to its seamless integration with **wallets like Phantom and Backpack**. Additionally, it can be developed as a **standalone API**, enabling **immediate adoption**. More information is mentioned below. 


### **1. Seamless Integration**
- Develop the system as a **plug-and-play API** or **wallet extension**.
- Ensure compatibility with **Phantom**, **Backpack**, and other Solana-based wallets.
- Provide **real-time scam alerts** directly within wallet interfaces.

### **2. Expanding Data Sources**
- Improve scam detection by **incorporating user-reported scam inputs** (community-driven risk assessment).
- Utilize **on-chain and off-chain data** to refine detection models.
- Implement **automated web scraping** and **API integrations** to collect comprehensive data from Solana NFT marketplaces, including scam reports, legitimate listings, and associated risk factors. This ensures that AI models are trained with high-quality, diverse data, leading to more accurate and efficient scam detection.

### **3. Advanced AI Models**
- Upgrade from the current **SGDClassifier** to more **powerful deep learning models**.
- Implement **rug pull detection**, analyzing transactional behavior and liquidity withdrawals.
- Enhance domain verification by **cross-checking site credibility** and detecting phishing attempts.

---
# Technical Documentation
---
## An example

![Example GIF](https://github.com/maape7/sol_ai_sup/blob/main/design/git_nft_example.gif?raw=true)

---

## Architecture Design of MVP

![NFT Architecture](https://raw.githubusercontent.com/maape7/sol_ai/refs/heads/main/design/nft_design.png)

---

## AI Model Overview: Solana NFT Scam Detection (MVP) 

This project utilizes a **hybrid approach** combining **heuristic rules** and **machine learning (ML)** to detect potential NFT scams on the Solana blockchain.  

## 🔹 AI Model  
- **Algorithm:** Stochastic Gradient Descent (SGD) Classifier  
- **Feature Extraction:** TF-IDF (Term Frequency-Inverse Document Frequency)  
- **Training Data:** 100 labeled samples (50 scams, 50 legitimate) - Small dataset, further refinement planned.  
- **Training Framework:** Scikit-learn  

## 🔹 Heuristic-Based Detection  
The system also applies **rule-based scoring** to assess suspicious patterns, such as:  
- 🚩 **Domain Analysis** (e.g., `.xyz`, `.top`, keywords like "giveaway")  
- 🚩 **Project Description Analysis** (e.g., "risk-free", "double your money")  

## 🔹 How It Works  
1. **Heuristic Analysis:** Assigns a risk score based on predefined scam patterns.  
2. **ML Classification:** The trained **SGDClassifier** predicts if a project is fraudulent.  
3. **Final Score:** A combined score determines the scam likelihood.  

---

## How It Works (MVP)
1. **User inputs an NFT mint address** → React frontend sends a request to Express.js API.
2. **Express.js API fetches NFT Details** from Solana via Web3.js. and sends to Fast API(Contains AI Model)
3. **NFT Details is processed by AI model** → Scam score is predicted using a trained SGD classifier and other rule based algorithms.
4. **Scam score is returned to the user** → Displayed in a simple UI as a score out of 100.

## Example Code Snippets

### **Python AI Model**
```python
import re
import joblib
from sklearn.metrics import classification_report

# Load the trained model and vectorizer
model = joblib.load("solana_nft_scam_model.pkl")
vectorizer = joblib.load("solana_vectorizer.pkl")

 # 🔹 Step 2: ML Model Prediction
X_test_tfidf = vectorizer.transform([description])  # Vectorize input
prediction = model.predict(X_test_tfidf)[0]  # Get model prediction (1 = Scam, 0 = Not Scam)

if prediction == 1:
    print("scam")
        score_data["score"] += 25  # ✅ Boost score if ML model flags it as a scam
    else:
        print("No scam")

```

### **Solana Metadata Fetching (TypeScript)**
```Typescript
export async function getNFTMetadata(mintAddress: string) {
  // Initialize the connection to the Solana cluster
  
  try{

  
  const connection = new Connection("https://api.mainnet-beta.solana.com", "confirmed");



  // Initialize Metaplex with the connection
  const metaplex = new Metaplex(connection);

  // Convert the mint address to a PublicKey
  const mint = new PublicKey(mintAddress);

  // Fetch the NFT metadata
  const nft = await metaplex.nfts().findByMint({ mintAddress: mint });


  // Log the NFT metadata
  const nftData = ({
    name: nft.name,  // ✅ NFT project name (Correct)
    symbol: nft.symbol,  // ✅ Token symbol (Correct)
    description: nft.json?.description,  // ✅ NFT description (Correct)
    image: nft.json?.image,  // ✅ Image URL (Correct)
    external_url: nft.json?.external_url,  // ✅ Project's external URL (Correct)
    seller_fee_basis_points: nft.sellerFeeBasisPoints,  // ✅ Royalties percentage (Correct)
    creators: nft.creators?.map(creator => creator.address.toBase58()),  // ✅ Creator addresses (Correct)
    update_authority: nft.updateAuthorityAddress.toBase58(),  // ✅ Who controls updates? (Correct)
    mint_address: nft.address.toBase58(),  // ✅ Mint address (Fixed Error: nft.address instead of nft.mintAddress)
    metadata_uri: nft.uri,  // ✅ Metadata URI (Correct)
});

   return nftData;

  }catch (error) {
    console.error("Error fetching NFT metadata:", error);
    return null;
}

}
```
---

## Technology Stack

### **Frontend:**
- **React.js** – For the user interface, allowing users to input an Solana NFT mint address and retrieve scam scores.

### **Backend:**
### Express.js
- Handles API endpoints that:
  - Receive the mint address from the frontend.
  - Fetch NFT details, including metadata, description, and associated domain, from Solana.
  - Pass the retrieved data to the FastAPI backend for further analysis.

### FastAPI
- Processes the NFT details using an **SGDClassifier-based AI model** and rule-based algorithms.
- Analyzes the NFT's metadata and domain details.
- Assigns a scam risk score on the basis of rules and classification done by AI model.
- WHOIS checks are performed separately but contribute to the overall risk assessment.


### **AI and Machine Learning:**
- **Python (NumPy, Pandas, Scikit-Learn)** – AI model for scam detection based on  NFT Details.
- **TF-IDF Vectorization** – Text feature extraction for analyzing NFT descriptions.
- **SGD Classifier** – A machine learning model trained to detect scam patterns.
- **Joblib** – Model serialization for efficient storage and retrieval.

## Installation & Setup

### **1. Clone the Repository:**
```sh
 git clone <repository_url>
 cd <project_directory>
```

### **2. Install Dependencies:**
#### **For Frontend (React.js)**
```sh
 cd client
 npm install
 npm start
```

#### **For Backend Express.js**
```sh
 cd backend/express-api
 npm install  # For Express.js API
```

#### **For Backend FastAPI**
```sh
 cd backend/fastapi-api
 python -m venv venv
 source venv/bin/activate  # On Windows use: venv\Scripts\activate
 pip install -r requirements.txt  # For FastAPI & AI model
```


### **3. Run the Services:**
#### **Start Express.js API:**
```sh
# Start the Express.js server with Nodemon (for hot-reloading)
npx nodemon --ext ts src/server.ts
```
#### **Start FastAPI Server:**
```sh
# Start the FastAPI server with Uvicorn
uvicorn app.main:app --reload
```
---

## Challenges & Solutions

- **Data Availability**: Initially, obtaining high-quality datasets of scam and legitimate URLs was difficult.  
  - **Solution**: Integrated **Rule Based** to analyze NFT domain legitimacy and leveraged **SGDClassifier** for scam classification after facing issues with earlier models like LightGBM. This helped improve scam detection accuracy. And bring up MVP Faster.

- **Model Accuracy**: Early attempts at URL classification lacked reliability due to insufficient training data.  
  - **Solution**: Transitioned to **SGDClassifier**, which performed better with limited data, and continuously refined the dataset for improved results.  

- **Blockchain Data Retrieval**: While NFT metadata was relatively easy to fetch, ensuring efficient and fast processing was crucial.  
  - **Solution**: Designed a well-structured **backend architecture** using **Express.js** and **FastAPI**, ensuring seamless communication between services. By structuring the API workflow efficiently, I built a scalable system that can function as a standalone API for broader integration.  

As the dataset grows, the system will become even more robust, making Solana NFT Scam detection **more precise and scalable**. 🚀  


