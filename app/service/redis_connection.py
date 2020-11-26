import sys
sys.path.append('connection/')

from connection import *
import redis

class RedisConnection(DatabaseConnection):
    def __init__(self, host, port, db):
        self._connection = redis.Redis(host=host, port=port, database=db)
        atexit.register(self.close)

    def close(self):
        self._connection.exit()
    
    def add(self, key, value):
        self._connection.set(key, value)

    def get(self, key)
        return self._connection.get(key)

class RedisConnectionConfig(DatabaseConnectionConfig)
    def __init__(self, filename):
        super.__init__(self, filename)
        with open(filename, 'r') as config: 
            args = yaml.load(config) # todo
            self.username = args['database']

    def create_connection(self, class_constructor):
        return RedisConnection(self.host, self.port, self.database)

class RedisConnectionConfigurationManager(ConnectionConfigurationManager):
    def create_database_conf(filename="conf/redis_config.yaml"):
        return RedisConnectionConfig(filename)

