# https://pypi.org/project/MySQL-python/

import MySQLdb

def connect(role):
    if (role == 'app'):
        return MySQLdb.connect(
            host="35.231.197.213", 
            user="bbd-create", 
            passwd="bbd-create-123", 
            db="bluebike")
    elif (role == 'creator'):
        return MySQLdb.connect(
            host="35.231.197.213", 
            user="root", 
            passwd="rachlin-sesame", 
            db="bluebike")
