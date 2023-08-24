import mysql.connector
import config

__cnx = None


def get_mysql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user=config.DatabaseConfig.user,
                                        password=config.DatabaseConfig.password,
                                        host=config.DatabaseConfig.host,
                                        database=config.DatabaseConfig.database
                                        )

    return __cnx
