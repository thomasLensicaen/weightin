import pymongo
from config import DbConfig
import logging
from common.logtool import log_debug, create_logger 

class AppBase:
    db_name = "appbase"
    collections_list = ["appbase"]

    def __init__(self, dbconfig: DbConfig):
        self.dbconfig = dbconfig
        self.mongo_client = pymongo.MongoClient(dbconfig.host, dbconfig.port)
        server_info = self.mongo_client.server_info()
        self.db = self.mongo_client[self.db_name]
        self.collections = dict()
        for col_name in self.collections_list:
            self.collections[col_name] = self.db[col_name]
        print(self.mongo_client.list_database_names())
        if not self.db_name in self.mongo_client.list_database_names():
            logging.info("{} Database is not created inside MongoDb, maybe no content has been pushed yet".format(self.db_name))
