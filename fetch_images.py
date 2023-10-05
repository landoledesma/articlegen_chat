import requests
from dotenv import load_dotenv
import os

load_dotenv("token.env")
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
PEXELS_API_KEY = os.getenv('PEXELS_API_KEY')

def fetch_photo(query):
    api_key = ""

    url = 'https://api.pexels.com/v1/search'
    headers = {
        'Authorization':PEXELS_API_KEY,
    }
    params = {
        'query':query,
        'per_page':1,
    }
    response = requests.get(url,headers=headers,params=params) 

    if response.status_code == 200:
        data = response.json()
        photos = data.get('photos',[])
        if photos:
            src_original_url = photos[0]['src']['original']
            return src_original_url
        else:
            print(f"Error: {response.status_code},{response.text}")
    return None

# Example usage of the function
query = 'kitties'
src_original_url = fetch_photo(query)
if src_original_url:
    print(f"Original URL for query '{query}': {src_original_url}")
else:
    print("No se pudo traer imagens lo siento ")