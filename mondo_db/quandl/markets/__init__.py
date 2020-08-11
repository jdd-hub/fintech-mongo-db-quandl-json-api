from mondo_db import MongoDB

global cluster
global db
global collection


class Markets:
    # Creates the MongoDB cluster instance and initiates the connection.
    cluster = MongoDB.connection()
    # Creates the database object and connects to the specified database.
    db = cluster["quandl"]
    # Creates the collection object referencing the required collection from the database.
    collection = db["markets"]

    @staticmethod
    def get_markets():
        # Get the all the collection of markets from the database.
        markets = Markets.collection.find({})
        return markets

    def insert_market(dict_markets):
        # Insert document into collection.
        Markets.collection.insert_one(dict_markets)

    @staticmethod
    def remove_all_markets():
        # Clear the entire collection.
        Markets.collection.remove({})

    def insert_stock(dict_markets):
        # Update the collection object referencing the required collection from the database.
        Markets.collection = Markets.db["stocks"]
        # Insert document into collection.
        Markets.collection.insert(dict_markets)

    @staticmethod
    def remove_all_stocks():
        # Update the collection object referencing the required collection from the database.
        Markets.collection = Markets.db["stocks"]
        # Clear the entire collection
        Markets.collection.remove({})
