import numpy as np
from mondo_db.quandl.markets import Markets

# Create a sequential list of numbers to be used as an index for the DataFrame.
row_labels = np.arange(10)

# The list of codes required by the API.
lst_code = ["DIS", "MSFT", "INTC", "IBM", "AAPL", "MMM", "PFE", "JNJ", "PG", "NKE"]

# List of names as a reference to each code.
lst_names = ["The Walt Disney Company (DIS)",
             "Microsoft Corporation (MSFT)", "Intel Corporation (INTC)",
             "International Business Machines Corporation (IBM)", "Apple Inc. (AAPL)",
             "3M Company (MMM)", "Pfizer inc. (PFE)", "Johnson & Johnson (JNJ)",
             "Procter & Gamble Company (PG)", "Nike Inc. (NKE)"]

# Empty the collection to run demo.
Markets.remove_all_markets()

print("")
for index in row_labels:
    # Converts both lists into on data dictionary for insertion into the Mongo database.
    dict_markets = {
        "_id": str((index + 1)),
        "name": lst_names[index],
        "code": lst_code[index]
    }
    # Insert dictionary item into collection.
    Markets.insert_market(dict_markets)

    # Display conformation for each insertion operation.
    print("Inserted: {_id: " + str((index + 1)) + ", name: " + lst_names[index] + ", code: " + lst_code[index] + "}")
