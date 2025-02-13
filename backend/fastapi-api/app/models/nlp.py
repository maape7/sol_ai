# for reference 

def analyze_project_description(description):
    # Use NLP to check for scam-like language
    scam_keywords = ['guaranteed', 'risk-free', 'official giveaway', 'limited mint']
    score = 0
    for keyword in scam_keywords:
        if keyword in description.lower():
            score += 1
    # A simple threshold-based flag for demonstration
    return score >= 2  # Flag if two or more scam keywords are present

# Using a BERT Model (Hugging Face)


from transformers import pipeline

# Load a pre-trained text classification model
scam_detector = pipeline("text-classification", model="bhadresh-savani/bert-base-uncased-finetuned-scam")

def analyze_project_description(description):
    result = scam_detector(description)
    return result[0]['label'] == "scam"  # If model labels it as 'scam', flag it

# Example test
desc = "Guaranteed returns on your investment in crypto!"
if analyze_project_description(desc):
    print("⚠️ Scam-like language detected!")
else:
    print("✅ Looks safe!")


#######################

# Load FinBERT model 

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from torch.nn.functional import softmax

# Load FinBERT (fast, sentiment-based fraud detection)
MODEL_NAME = "yiyanghkust/finbert-tone"  
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

def analyze_project_description(description):
    inputs = tokenizer(description, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    probabilities = softmax(outputs.logits, dim=1)
    scam_score = probabilities[0][1].item()  # Higher = more scam-like

    return scam_score > 0.5  # Flags as scam if above threshold

# Example usage
description = "Guaranteed profits! Limited-time NFT offer! Join now and get free rewards!"
is_scam = analyze_project_description(description)
print(f"Scam Detected: {is_scam}")

