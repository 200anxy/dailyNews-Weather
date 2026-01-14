import os
from newsapi import NewsApiClient
from dotenv import load_dotenv

# Initialize client
load_dotenv()
api_key = os.getenv("NEWSAPI")
newsapi = NewsApiClient(api_key=api_key)

def format_for_sms(articles, label):
    sms_text = f"=== {label} ===\n"

    for i, art in enumerate(articles[:3], 1):
        title = art.get('title', 'No Title')
        url = art.get('url', '')
        source = art.get('source', {}).get('name', 'News')
        
        
        sms_text += f"\n{i}. [{source}] {title}\n🔗 {url}\n"
    
    return sms_text

def textOutput():
    bbc_news = newsapi.get_top_headlines(sources='bbc-news')
    tech_news = newsapi.get_top_headlines(category='technology', language='en', country='us')
    bbc_sms = format_for_sms(bbc_news['articles'], "BBC TOP NEWS")
    tech_sms = format_for_sms(tech_news['articles'], "TECH UPDATES")
    # print(bbc_sms+tech_sms)
    return bbc_sms + tech_sms

    
# textOutput()

# print(bbc_sms)
# print(tech_sms)