
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

project_metrics = 8

description = "guaranteed risk-free"

print(heuristic_score(nft_metadata, project_metrics, description))