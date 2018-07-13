#!/usr/bin/env python3

import kconfiglib
import sys
import MySQLdb
import DBCredentials

# Autor Pierre LE LURON, Alexis LE MASLE


def fill_types(input):
    kconf = kconfiglib.Kconfig(input)

    # SQL requests
    truncate = "TRUNCATE TABLE Properties"
    fill = "INSERT INTO Properties (name, type) VALUES (%s, %s)"

    if len(DBCredentials.db) == 0:
        print("No database(s) have been selected. Please modify DBCredentials.py to add your databases")
        exit(-1)

    for creds in DBCredentials.db:
        print("Filling database {} at {}".format(creds["creds"]["db"], creds["creds"]["host"]))
        data_fill = []

        # Add new entries
        for sym in set(kconf.defined_syms):
            data_fill.append((
                sym.name,
                kconfiglib.TYPE_TO_STR[sym.orig_type].upper()))

        conn = MySQLdb.connect(creds["creds"]["host"], creds["creds"]["user"], creds["creds"]["passwd"], creds["creds"]["db"])
        cursor = conn.cursor()

        try:
            # Remove previous entries and add properties
            cursor.execute(truncate)
            cursor.executemany(fill, data_fill)
            conn.commit()

        except MySQLdb.Error as err:
            print("Error : Can't write to db : {}".format(err.args[1]))
            exit(-1)

        finally:
            conn.close()
            cursor.close()


fill_types(sys.argv[1])
