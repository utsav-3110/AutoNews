import requests

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




def ask_choice(question, options):
    print(question)
    print("Options: " + ", ".join(options))
    for attempt in range(3):
        answer = input("> ").strip().upper()
        if answer in options:
            return answer
        print("Not a valid choice, try again.")
    raise ValueError("Too many invalid attempts. Please run the program again and enter a valid option.")


def prompt_for_country():
    country = ask_choice("\n🌍 What country do you want news from?", list(country_map.keys()))
    return country_map[country]


def prompt_for_language():
    language = ask_choice("\n🗣️ What language should the news be in?", list(language_map.keys()))
    return language_map[language]


def prompt_for_category():
    print("\n📰 What category of news do you want?")
    print("Options: " + ", ".join(category_list) + ", or press Enter for all categories")
    category = input("> ").strip().lower()    
    return category if category in category_list else "all"



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
    


    url += f"apiKey=< your api key  >"
    

    response = requests.get(url)
    res = response.json()
   
    if res['totalResults'] == 0:
        raise "Not found any artical with your filter try diffrent filter "
    

    included_artical = int(input(f"there are {res['totalResults']} artical , how many of them you want it (enter a number )" ))
    

    return res['articles'][:included_artical]
    
    # print(artical)
