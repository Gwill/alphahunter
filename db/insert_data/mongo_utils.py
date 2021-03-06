# -*- coding: utf-8 -*-

from pymongo import MongoClient

MONGO_POOL = MongoClient(host="127.0.0.1",
                         maxPoolSize=10,
                         socketTimeoutMS=10000,  # warn:单位毫秒
                         connectTimeoutMS=10000,
                         socketKeepAlive=True,
                         w="majority",
                         j=True,
                         authSource="admin",
                         username="admin",
                         password="admin")


def get_mongo_conn(db="test"):
    """
    use me like this:

    collection = get_mongo_conn()["collection_name"]
    collection.insert({})
    """
    return MONGO_POOL[db]
