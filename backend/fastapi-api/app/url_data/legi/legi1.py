import os
import pandas as pd
import requests

def fetch_nft_data():
    # Example: Fetch data from Magic Eden API (Replace with actual API endpoint and parameters)
    api_url = "https://api-mainnet.magiceden.dev/v2/collections"  # Example URL
    response = requests.get(api_url)
    
    if response.status_code == 200:
        nft_data = response.json()

        
        # Process and structure data
        data = pd.DataFrame({
            'URL': nft_data.url,  # Example URL (Modify as needed)
            'Type': ["Legitimate"]
        })
        
        print("data ->", data)
        save_and_update_dataframe_to_excel(data, filename='nft_data.xlsx')
    else:
        print("Failed to fetch data from API")

def save_and_update_dataframe_to_excel(data, filename='nft_data.xlsx'):
    if os.path.exists(filename):
        # Read existing data
        existing_data = pd.read_excel(filename)
        
        # Ensure no duplicate rows based on 'URL'
        updated_data = pd.concat([existing_data, data]).drop_duplicates(subset='URL', keep='last')
    else:
        updated_data = data
    
    # Save the updated data back to the file
    updated_data.to_excel(filename, index=False)
    print(f"Data saved successfully to {filename}")

# Run the function
fetch_nft_data()
