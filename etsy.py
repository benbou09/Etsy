import urllib
import pandas as pd
import json
import os

API_KEY = 'xxxxxxxxxxxxxxxxxxxxxx' # API key is we you get when you register to the API
ETSY_API_VERSION = 'https://openapi.etsy.com/v2'

def download_data(url):
    inst = urllib.urlopen(url)
    data_json = json.load(inst)
    return data_json['results']

def filter_columns(data_json, columns):
    if columns == []:
        return data_json
    filtered_columns = [{}]
    for i in columns:
        try:
            filtered_columns[0][i] = data_json[0][i]
        except IndexError:
            print i + ' not given for this user'
    return filtered_columns

def create_table(data_json, columns):
    filtered_data_json = filter_columns(data_json, columns)
    return pd.DataFrame(filtered_data_json)

def save_data(df, file_name):
    with open(file_name, 'a') as f:
        if os.path.getsize(file_name) == 0:
            df.to_csv(f, sep='|', encoding='utf-8', header=True)
        else:
            df.to_csv(f, sep='|', encoding='utf-8', header=False)

def print_url(url):
    print 'importing from: ' + url

def getUser(user, columns=[]):
    url = ETSY_API_VERSION + '/users/' + str(user) + '/profile?limit=100&' + 'api_key=' + API_KEY
    print_url(url)
    data_json = download_data(url)
    return create_table(data_json, columns)

def findAllUserShops(user, columns=[]):
    url = ETSY_API_VERSION + '/users/' + str(user) + '/shops?limit=100&'  + 'api_key='+ API_KEY
    print_url(url)
    data_json = download_data(url)
    return create_table(data_json, columns)

def findAllShopListingsActive(shop, columns=[]):
    p = 1
    listing_json = []
    while True: # many shops have more than 100 listings, so we iterate through pages, until the result is []
        url = ETSY_API_VERSION + '/shops/' + str(shop) + '/listings/active?limit=100&page=' + str(p) + '&' + 'api_key='+ API_KEY
        page_data_json = download_data(url)
        if page_data_json != []:
            listing_json += page_data_json
            p += 1
            print_url(url)
        else:
            return create_table(listing_json, columns)
