from kconfiglib import *
import sys
import os
import MySQLdb
import DBCredentials

def fill_types(input, credentials):
    kconf = Kconfig(input)

    # SQL requests
    fill = "TRUNCATE TABLE Properties; INSERT INTO Properties (name, type) VALUES (%s, %s)"

    if len(DBCredentials.db) == 0:
        print("No database(s) have been selected. Please modify DBCredentials.py to add your databases")
        exit(-1)

    for creds in DBCredentials.db:
        data_fill = []
        try:
            conn = MySQLdb.connect(**DBCredentials.db)
            cursor = conn.cursor()
            # Add new entries
            for sym in kconf.defined_syms:
                data_fill.append((
                    sym.name, 
                    TYPE_TO_STR[sym.orig_type].upper()))

            # Remove previous entries and add properties
            cursor.executemany(fill, data_fill)
            conn.commit()

        except MySQLdb.Error as err:
            print("Error : Can't write to db : {}".format(err.args[1]))
            exit(-1)
        finally:
            conn.close()

fill_types(sys.argv[1])
