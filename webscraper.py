from pathlib import Path
from matplotlib import pyplot as plt
import pandas as pd
import regex as re
import json

# Importing selenium components
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#importing huggingface transformers
from transformers import pipeline

def webscraper(url_input):
    # Setting up the selenium webdriver
    options = Options()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    # importing the list of australian stocks
    # csv_path = Path('Resources/ASX_Listed_Companies_25-03-2024_02-42-20_AEDT.csv')
    # company_symbols = pd.read_csv(csv_path)
    # company_symbols

    query_start = 'https://au.finance.yahoo.com/quote/';
    query_end = '?.tsrc=fin-srch'

    article_dict = {}
    query_URL = query_start + url_input + query_end
    driver.get(query_URL)

    articles = driver.find_elements(By.CSS_SELECTOR, 'li[class="js-stream-content Pos(r)"]')
    i = 0

    # The following code parses the raw html from selenium to a regex patern which extracts the text
    for article in articles:
        raw_html = article.get_attribute('outerHTML')

        # Creating regex patterns
        title_pattern = r'(?:</u>)(.*?)(?:</a>)'
        blurb_pattern = r'(?:\(0\)">)(.*?)(?:</p>)'
        link_pattern = r'(?:href=")(.*?)(?:" data-uuid)'

        # Performing a regex search
        title = re.search(title_pattern, raw_html)
        blurb = re.search(blurb_pattern, raw_html)
        link = re.search(link_pattern, raw_html)
        article_dict[f"article{i}"] = {'title':str(title.group(1)), 'blurb':str(blurb.group(1)), 'link':str(link.group(1))}
        i+=1
        
    # for article in article_dict:
    #     print(article_dict[article]['title'])

    # Closing the webdriver
    driver.quit()

    for article in article_dict:
        sentiment = pipeline(task='sentiment-analysis')
        result = sentiment(article_dict[article]['blurb'])
        # print(sentiment_result, article)
        article_dict[article]['label'] = result[0]['label']
        article_dict[article]['score'] = result[0]['score']

    # implement code to export into mongoDB
    with open('Resources/newsArticles.json', 'w') as outfile:
        json.dump(article_dict, outfile)
    
    return article_dict
