import requests
from mongo_db.quandl.markets import Markets
from mongo_db.json import Json
import datetime as dt

# My API key.
api_key = '####################'


def get_json_payload(code):

    # Assign URL to variable: url.
    url = 'https://www.quandl.com/api/v3/datasets/EOD/' + code + '.json?api_key=' + api_key + '&start_date=2013-09-03&end_date=2017-12-28'

    # Packaging and sending of the request operation.
    r = requests.get(url)

    return r


# GET LATEST STOCK MARKET DATA.
markets = Markets.get_markets()

# Empty the collection to run demo.
Markets.remove_all_stocks()

# The file path for the JSON documents storage.
filepath = '/Users/julianmuscatdoublesin/PycharmProjects/PythonLibrary/ds_quandal/json_api_stock_markets/2013/'

for market in markets:
    # Display message on screen of current operation in process.
    print("\nPayload request for: EOD/" + market["code"] + " - " + market["name"] + " {_id: " + str(market["_id"]) + "}")
    print('https://www.quandl.com/api/v3/datasets/EOD/' + market["code"] + '.json?api_key=' + api_key + '&start_date=2013-01-01&end_date=2013-12-31')

    # Decode the JSON data into a dictionary.
    json_data = get_json_payload(market["code"].upper()).json()

    # Display returned payload for verification.
    print(json_data)

    # Insert document item into collection.
    Markets.insert_stock(json_data)

    """
    The code below has been added as an alternative to inserting the documents in raw format in MongoDB. 
    Reference to Markets.insert_stock(json_data).
    The raw JSON documents are stored in raw format in individual JSON files within the specified file path.
    The filename for each document consist of the date whe latest data was extracted and the respective market code. 
    """
    # ------------------------------------------------------
    # Dump document to JSON file.
    date_today = str(dt.date.today().strftime("%Y%m%d"))

    filename = date_today + "_" + market["code"]

    Json.dump_to_file(filename, json_data, filepath)
    print("JSON document payload stored to file:")
    print("Filename: " + filepath + filename + ".json")
    # ------------------------------------------------------

    # Display payload details for verification.
    print("")
    print("Dataset Preview:")
    print(json_data['dataset']['dataset_code'])
    print(json_data['dataset']['name'])
    print(json_data['dataset']['data'])

print("\nPayload request process completed.")
