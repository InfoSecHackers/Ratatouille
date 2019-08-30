import configparser
import MySQLdb

config = configparser.ConfigParser()
config.read('config/dbconfig.ini')

def connect():
    return MySQLdb.connect(host = config['mysqlDB']['host'],
                           user = config['mysqlDB']['user'],
                           passwd = config['mysqlDB']['pass'],
                           db = config['mysqlDB']['db'])