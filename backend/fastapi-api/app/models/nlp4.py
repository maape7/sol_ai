import re
import joblib  # To load the trained ML model
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# === Load Pre-trained ML Model (You need to train this separately) ===
vectorizer = joblib.load("tfidf_vectorizer.pkl")
scam_model = joblib.load("scam_classifier.pkl")

def is_onchain_activity_anomalous(project_metrics):
    """Check if on-chain activity is suspicious based on multiple metrics."""
    return (project_metrics["transactions_last_30_days"] < 10 or
            project_metrics["top_wallet_percentage"] > 50 or
            project_metrics["secondary_sales_count"] == 0)

def is_domain_suspicious(external_url):
    """Check if a domain is suspicious based on various heuristics."""
    suspicious_tlds = ['.xyz', '.top', '.online', '.tk', '.ml', '.gq']
    scam_keywords = ['giveaway', 'free', 'claim', 'mint', 'bonus', 'official', 'earn']

    domain = re.sub(r"https?://(www\.)?", "", external_url).split('/')[0]
    
    tld_flag = any(domain.endswith(tld) for tld in suspicious_tlds)
    scam_word_flag = any(word in domain.lower() for word in scam_keywords)

    return tld_flag or scam_word_flag

def analyze_project_description(description):
    """AI-powered scam detection using an ML model instead of rule-based keywords."""
    
    # Convert text to TF-IDF features
    text_features = vectorizer.transform([description])
    
    # Get scam probability from ML model
    scam_probability = scam_model.predict_proba(text_features)[0][1]  # Get probability for scam class
    
    return int(scam_probability * 10)  # Convert to a heuristic score (0-10)

def heuristic_score(nft_metadata, project_metrics, description):
    """Calculate a heuristic score based on AI and rule-based methods."""
    
    score = 0

    if is_domain_suspicious(nft_metadata['external_url']):
        score += 3 

    if is_onchain_activity_anomalous(project_metrics):
        score += 2  

    score += analyze_project_description(description)  # AI-powered NLP score
    
    return score

# === Example Test Cases ===
nft_metadata = {"external_url": "https://official-giveaway.xyz"}
project_metrics = {
    "transactions_last_30_days": 5,
    "top_wallet_percentage": 60,
    "secondary_sales_count": 0
}
description = "This is a guaranteed risk-free official giveaway! Act now."

# Run heuristic scoring function multiple times for testing
print(heuristic_score(nft_metadata, project_metrics, description))
print(heuristic_score(nft_metadata, project_metrics, description))
print(heuristic_score(nft_metadata, project_metrics, description))
print(heuristic_score(nft_metadata, project_metrics, description))
