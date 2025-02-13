import re

def is_onchain_activity_anomalous(project_metrics):
    """Check if on-chain activity is suspicious based on multiple metrics."""
    if (project_metrics["transactions_last_30_days"] < 10 or
        project_metrics["top_wallet_percentage"] > 50 or
        project_metrics["secondary_sales_count"] == 0):
        return True
    return False

def is_domain_suspicious(external_url):
    """Check if a domain is suspicious based on various heuristics."""
    
    suspicious_tlds = ['.xyz', '.top', '.online', '.tk', '.ml', '.gq']
    scam_keywords = ['giveaway', 'free', 'claim', 'mint', 'bonus', 'official', 'earn']
    
    # Extract domain name
    domain = re.sub(r"https?://(www\.)?", "", external_url).split('/')[0]
    
    # Check if TLD is suspicious
    tld_flag = any(domain.endswith(tld) for tld in suspicious_tlds)

    # Check for common scam words in domain name
    scam_word_flag = any(word in domain.lower() for word in scam_keywords)

    # Placeholder for WHOIS API to check domain age
    # domain_age = lookup_domain_age(domain)  # Uncomment if using API
    # age_flag = domain_age < 180  # Flag if domain is newer than 6 months
    
    return tld_flag or scam_word_flag  # or age_flag  # Uncomment age_flag if using WHOIS API


def analyze_project_description(description):
    """Analyze project description using scam-related keywords."""
    
    scam_keywords = {
        'guaranteed': 3, 'risk-free': 3, 'official giveaway': 4, 
        'limited mint': 2, 'double your money': 5, 'act now': 3, 
        'instant profit': 4, 'exclusive deal': 3, 'no loss': 4
    }
    
    score = 0
    description = description.lower()
    
    for keyword, weight in scam_keywords.items():
        if keyword in description:
            score += weight  # Weighted scoring for severity
    
    return score  # Higher score = more scam-like

def heuristic_score(nft_metadata, project_metrics, description):
    """Calculate a heuristic score based on multiple scam indicators."""
    
    score = 0
    
    if is_domain_suspicious(nft_metadata['external_url']):
        score += 3  # Domain issues carry high weight

    if is_onchain_activity_anomalous(project_metrics):
        score += 2  # Blockchain anomalies

    score += analyze_project_description(description)  # Add NLP-based score
    
    return score


# === Test Cases ===
nft_metadata = {"external_url": "https://official-giveaway.xyz"}
project_metrics = {
    "transactions_last_30_days": 5,
    "top_wallet_percentage": 60,
    "secondary_sales_count": 0
}
description = "This is a guaranteed risk-free official giveaway! Act now."

# Run heuristic scoring function multiple times for testing
heuristic_score(nft_metadata, project_metrics, description)

