from pymongo import MongoClient


class MongoDB:

    @staticmethod
    def connection():
        # Connection object to MongoDB Server.
        user = ""
        password = ""
        conn = MongoClient(
            "mongodb+srv://"
            + user + ":"
            + password
            + "@cluster0.hz9ax.mongodb.net/<dbname>?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")

        return conn
