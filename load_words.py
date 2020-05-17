import requests
import sys

def get_words(url):

    try:
        response = requests.get(url).text
        words_list = response.strip().split('\n')
        words_list = [x.lower().replace('\r', '') for x in words_list]
        
    except Exception as e:
        print(e)
        with open(url, 'r') as f:
            words_list = f.read().strip().split('\n')
            words_list = [x.lower().replace('\r', '') for x in words_list]

    return words_list