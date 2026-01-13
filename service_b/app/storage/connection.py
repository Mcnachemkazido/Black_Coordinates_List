import redis
from dotenv import load_dotenv
import os

load_dotenv()


class Connection:
    def __init__(self):
        self.conn = None

    def get_connection(self):
        if self.conn is None:
            self.conn = redis.Redis(
                host= os.getenv("REDIS_HOST"),
                port= int(os.getenv("REDIS_PORT")),
                username =os.getenv("REDIS_USER"),
                password =os.getenv("REDIS_PASS"),
                decode_responses =True)
            print(f"create connection: {(self.conn.ping())}")

    def close_connection(self):
        self.conn.close()
