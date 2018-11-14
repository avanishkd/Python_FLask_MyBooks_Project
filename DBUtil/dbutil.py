from pymongo import MongoClient
import logging
'''
Connecting Database...
'''
def connect():
    logging.basicConfig(filename="logbook.log", format='%(asctime)s %(message)s', filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    client = MongoClient("mongodb://127.0.0.1:27017")
    db = client['MyBookDB']
    try:
        db.command("serverStatus")
    except Exception as e:
        print(e)
    else:
        logger.info("Connected to the database")
        return db