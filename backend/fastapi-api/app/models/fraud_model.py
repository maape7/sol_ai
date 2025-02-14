import re
import joblib
from sklearn.metrics import classification_report

# Load the trained model and vectorizer
model = joblib.load("solana_nft_scam_model.pkl")
vectorizer = joblib.load("solana_vectorizer.pkl")

# def is_onchain_activity_anomalous(project_metrics):
#     """Check if on-chain activity is suspicious based on multiple metrics."""
#     if (project_metrics["transactions_last_30_days"] < 10 or
#         project_metrics["top_wallet_percentage"] > 50 or
#         project_metrics["secondary_sales_count"] == 0):
#         return True
#     return False

score_data = {"score": 0}

def is_domain_suspicious(external_url):
    
    """Check if a domain is suspicious based on various heuristics."""
    
    suspicious_tlds = [
        '.xyz', '.top', '.online', '.tk', '.ml', '.gq', '.cc', '.cf', '.ga', '.ve',
        '.pw', '.bd', '.ke', '.ng', '.pk', '.ru', '.in', '.ph', '.click', '.bond']

    scam_keywords = [
        'giveaway', 'free', 'claim', 'mint', 'bonus', 'earn',
        'bigdaddyapeclub', 'bigdaddyape', 'apeclub', 'daddyape', 'daddyapeclub',
        'airdrop', 'exclusive', 'limited', 'urgent', 'winner', 'congratulations',
        'prize', 'redeem', 'instant', 'reward']

    
    # Extract domain name
    domain = re.sub(r"https?://(www\.)?", "", external_url).split('/')[0]
    
    
    # Check if TLD is suspicious
    if any(domain.endswith(tld) for tld in suspicious_tlds):
        score_data["score"] += 10  # Increase score if TLD is suspicious

    # Check for common scam words in domain name
    if any(word in domain.lower() for word in scam_keywords):
        score_data["score"] += 15  # Increase score for scam-related words



def analyze_project_description(description):
    """Analyze project description using scam-related keywords and ML model."""
    
    scam_keywords = {
    'guaranteed': 3, 'risk-free': 3, 'official giveaway': 4,
    'limited mint': 2, 'double your money': 5, 'act now': 3,
    'instant profit': 4, 'exclusive deal': 3, 'no loss': 4,
    'limited time offer': 3, 'click here': 2, 'urgent response': 3,
    '100% free': 4, 'secure investment': 3, 'high returns': 4}

    # Convert description to lowercase
    description = description.lower()

    # 🔹 Step 1: Keyword-based scoring
    for keyword, weight in scam_keywords.items():
        if keyword in description:
            score_data["score"] += weight  # ✅ Updating the global dictionary

    # 🔹 Step 2: ML Model Prediction
    X_test_tfidf = vectorizer.transform([description])  # Vectorize input
    prediction = model.predict(X_test_tfidf)[0]  # Get model prediction (1 = Scam, 0 = Not Scam)

    if prediction == 1:
        print("scam")
        score_data["score"] += 25  # ✅ Boost score if ML model flags it as a scam
    else:
        print("No scam")
    # 🔹 Step 3: Return Final Score & Prediction
    
    



def heuristic_score(external_url, description):
    
    score_data['score'] = 0
   
    """Calculate a heuristic score based on multiple scam indicators."""
    
    
    
    is_domain_suspicious(external_url)

    # if is_onchain_activity_anomalous(project_metrics):
    #     score += 2  # Blockchain anomalies

    analyze_project_description(description)  # Add NLP-based score
    print("score_data[score] -->",score_data["score"])
    return score_data["score"]


# === Test Cases ===
# nft_metadata = {"external_url": "https://official-giveaway.xyz"}
# project_metrics = {
#     "transactions_last_30_days": 5,
#     "top_wallet_percentage": 60,
#     "secondary_sales_count": 0
# }
# description = "This is a guaranteed risk-free official giveaway! Act now."

# # Run heuristic scoring function multiple times for testing
# heuristic_score(nft_metadata, project_metrics, description)

