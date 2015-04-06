# Etsy

A very simplified wrapper written in Python for the Etsy API (https://www.etsy.com/developers/documentation). It requires Pandas

First, you will need to 'open a session' by entering your Etsy api key (which you get for free once you register to the Etsy developer website):
API_KEY = 'xxxxxxxxxxxxxx'

3 functions based on the Etsy API functions have been implemented:
- getUser(user, columns=[]) # user can be either the user_id or login_name / by default, all columns will be imported
- findAllUserShops(user, columns=[])
- findAllShopListingsActive(shop, columns=[])# shop can be either the shop_id or login_name

These functions return a pandas DataFrame, for instance:
user_df = getUser('0000000', ['user_id', 'transaction_buy_count', 'transaction_sold_count'])

DataFrames can be saved in CSV format, for instance:
save_data(user_df, 'users.txt')
