import re

# Define thresholds based on your domain knowledge or empirical data
expected_min_transactions = 10       # e.g., expect at least 10 transactions in the last 30 days
concentration_threshold = 0.5        # e.g., flag if one wallet holds more than 50% of tokens

def is_onchain_activity_anomalous(project_metrics):

    if project_metrics < 3:
        return True
    else:
        return False


    # project_metrics is a dict containing keys like 'transactions_last_30_days', 'top_wallet_percentage', etc.
    # if project_metrics['transactions_last_30_days'] < expected_min_transactions:
    #     return True
    # if project_metrics['top_wallet_percentage'] > concentration_threshold:
    #     return True
    # if project_metrics['secondary_sales_count'] == 0:
    #     return True
    # return False

def check_domain_pattern(domain):
    """
    Analyzes a domain name to check for patterns commonly seen in suspicious or autogenerated domains.
    
    Heuristics:
    - Excessively high ratio of numeric characters.
    - Repeated characters (e.g., 'aaaa' or '1111').
    - Excessive length (could indicate auto-generated names).
    - Unusual amount of hyphens.
    
    Returns True if any suspicious pattern is found, else False.
    """
    
    # Normalize the domain (remove www. if present)
    domain = domain.lower().replace("www.", "")
    
    # Heuristic 1: Check if the domain is excessively long.
    # (Threshold is arbitrary; adjust as necessary)
    if len(domain) > 30:
        return True

    # Heuristic 2: Check the ratio of numeric characters.
    digit_count = sum(1 for c in domain if c.isdigit())
    if len(domain) > 0 and (digit_count / len(domain)) > 0.3:
        # Flag if more than 30% of the domain are digits.
        return True

    # Heuristic 3: Look for repeated characters (4 or more in a row).
    if re.search(r'(.)\1{3,}', domain):
        return True

    # Heuristic 4: Check for an excessive number of hyphens.
    if domain.count('-') > 2:
        return True

    # Additional heuristics can be added here (e.g., random character patterns)
    
    return False

def is_domain_suspicious(external_url):

    #api's
    # domain = extract_domain(external_url)
    # age = lookup_domain_age(domain)
    # tld_flag = domain.endswith(tuple(['.xyz', '.top', '.online']))
    # pattern_flag = check_domain_pattern(domain)
          #api's
    #    if age < 180 or tld_flag or pattern_flag:
    #     return True
    # return False
    # Simple rule: flag if new domain or suspicious TLD or pattern mismatch
     # rules

    if "xyz" in external_url:
        return True
    else:
        return False







def analyze_project_description(description):

     # NLP model 

    # Use NLP to check for scam-like language
    scam_keywords = ['guaranteed', 'risk-free', 'official giveaway', 'limited mint']
    score = 0
    for keyword in scam_keywords:
        if keyword in description.lower():
            score += 1
    # A simple threshold-based flag for demonstration
    
        
    return score  # Flag if two or more scam keywords are present





def heuristic_score(nft_metadata, project_metrics, description):
    score = 0
    if is_domain_suspicious(nft_metadata['external_url']):
        score += 3  # Weight of 3 for domain issues
    if is_onchain_activity_anomalous(project_metrics):
        score += 2  # Weight of 2 for blockchain anomalies
    k = analyze_project_description(description)

    score += k 
        
    return score




nft_metadata = {
    "external_url":"aa.xyz"
}

project_metrics = 3

description = "guaranteed"

print(heuristic_score(nft_metadata, project_metrics, description))