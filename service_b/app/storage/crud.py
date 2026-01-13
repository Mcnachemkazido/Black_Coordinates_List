from connection import Connection
import json


class DbOperations:
    def __init__(self):
        self.connection = Connection()
        self.connection.get_connection()

    def add_location(self,location):
        self.connection.conn.set(location["query"], json.dumps(location))

    def get_all_location(self):
        conn = self.connection.conn
        all_location = []
        keys = conn.keys()
        for k in keys:
            all_location.append(json.loads(conn.get(k)))
        return all_location





# ip = { "query": "213.151.56.82229",
#          "lat": 31.7674,
#          "lon": 35.2186}
