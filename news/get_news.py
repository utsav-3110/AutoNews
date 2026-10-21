import os
import sys
import time

import requests

API_KEY = os.environ.get("NEWS_API_KEY")
if not API_KEY:
    print("ERROR: NEWS_API_KEY environment variable is not set.", file=sys.stderr)
    sys.exit(1)

country_map = {
    "USA": "us",
    "INDIA": "in",
    "UK": "gb",
    "CANADA": "ca",
    "AUSTRALIA": "au",
    "GERMANY": "de",
    "FRANCE": "fr",
    "CHINA": "cn",
    "JAPAN": "jp",
}

language_map = {
    "ENGLISH": "en",
    "HINDI": "hi",
    "SPANISH": "es",
    "FRENCH": "fr",
    "GERMAN": "de",
    "CHINESE": "zh",

}

category_list = [
    "business", "entertainment", "general", "health", "science", "sports", "technology"
]




def prompt_for_country():
    print("\n🌍 What country do you want news from?")
    print("Options: " + ", ".join(country_map.keys()))
    country = input("> ").strip().upper()
    
    if country not in country_map.keys():
        raise "SELECT A ONE COUNTRAY "    

    return country_map.get(country, "all")


def prompt_for_language():
    print("\n🗣️ What language should the news be in?")
    print("Options: " + ", ".join(language_map.keys()))
    language = input("> ").strip().upper()
    if language not in language_map.keys():
        raise "SELECT A ONE LANGAUAGE "
    return language_map.get(language, "all")


def prompt_for_category():
    print("\n📰 What category of news do you want?")
    print("Options: " + ", ".join(category_list) + ", or press Enter for all categories")
    category = input("> ").strip().lower()    
    return category if category in category_list else "all"



def fetch_headlines(url):
    for attempt in range(3):
        try:
            response = requests.get(url, timeout=10)
            return response.json()
        except requests.RequestException:
            if attempt < 2:
                time.sleep(1)
    raise requests.RequestException("Failed to fetch headlines after 3 attempts")


def get_news():

    print("🧠 News Source Selector (Interactive CLI)\n")

    country_code = prompt_for_country()
    language_code = prompt_for_language()
    category = prompt_for_category()

    print("\n🔍 You selected:")
    print(f"  Country: {country_code}")
    print(f"  Language: {language_code}")
    print(f"  Category: {category}")
    
    
    url = f"https://newsapi.org/v2/top-headlines?"
      
        
        

    if country_code != 'all':
        url +=   f"country={country_code}&"

    if category != 'all':
        url +=   f"category={category}&"
        
    if language_code != 'all':
        url +=  f"language={language_code}&"
    


    url += f"apiKey={API_KEY}"
    

    res = fetch_headlines(url)
   
    if res['totalResults'] == 0:
        raise "Not found any artical with your filter try diffrent filter "
    

    included_artical = int(input(f"there are {res['totalResults']} artical , how many of them you want it (enter a number )" ))
    

    return res['articles'][:included_artical]
    
    # print(artical)
