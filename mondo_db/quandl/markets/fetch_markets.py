import requests
from mondo_db.quandl.markets import Markets

# My API key.
api_key = '####################'

def get_json_payload(code):

    # Assign URL to variable: url.
    url = 'https://www.quandl.com/api/v3/datasets/EOD/' + code + '.json?api_key=' + api_key + '&start_date=2017-01-01&end_date=2017-12-28'

    # Packaging and sending of the request operation.
    r = requests.get(url)

    return r


# GET LATEST STOCK MARKET DATA.
markets = Markets.get_markets()

# Empty the collection to run demo.
Markets.remove_all_stocks()

print("")
for market in markets:
    # Display message on screen of current operation in process.
    print("Payload request for: EOD/" + market["code"] + " - " + market["name"] + " {_id: " + str(market["_id"]) + "}")
    print('https://www.quandl.com/api/v3/datasets/EOD/' + market["code"] + '.json?api_key=' + api_key + '&start_date=2017-01-01&end_date=2017-12-28')

    # Decode the JSON data into a dictionary.
    json_data = get_json_payload(market["code"].upper()).json()

    # Display returned payload for verification.
    print("")
    print(json_data)

    # Insert document item into collection.
    Markets.insert_stock(json_data)

    # Display payload details for verification.
    print("")
    print(json_data['dataset']['dataset_code'])
    print(json_data['dataset']['name'])
    print(json_data['dataset']['data'])
