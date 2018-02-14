from kconfiglib import *
import irmaDBCredentials
import sys
import os
import MySQLdb

kconf = Kconfig(sys.argv[1])
arch = os.environ.get("ARCH")
version = os.environ.get("KERNELVERSION")

# SQL requests
arch_insert = "INSERT IGNORE INTO Arch (name) VALUES (%s)"
version_insert = "INSERT IGNORE INTO Version (version) VALUES (%s)"
arch_get_id = "SELECT id FROM Arch WHERE name = %s"
version_get_id = "SELECT id FROM Version WHERE version = %s"
remove_previous = "DELETE FROM Properties WHERE arch = %s AND version = %s"
fill = "INSERT INTO Properties (arch, version, name, type) VALUES (%s, %s, %s, %s)"

data_fill = []

try:
    conn = MySQLdb.connect(**irmaDBCredentials.info)
    cursor = conn.cursor()
    # Insert arch and get id
    cursor.execute(arch_insert, (arch,))
    cursor.execute(arch_get_id, (arch,))
    arch_id = cursor.fetchone()[0]
    # Insert version and get id
    cursor.execute(version_insert, (version,))
    cursor.execute(version_get_id, (version,))
    version_id = cursor.fetchone()[0]
    # Remove previous entries of same version and arch
    cursor.execute(remove_previous, (arch_id, version_id))
    # Add new entries
    for sym in kconf.defined_syms:
        data_fill.append((
            arch_id,
            version_id,
            sym.name, 
            TYPE_TO_STR[sym.orig_type].upper()))

    cursor.executemany(fill, data_fill)
    conn.commit()

except MySQLdb.Error as err:
    print("Error : Can't write to db : {}".format(err.args[1]))
    exit(-1)
finally:
    conn.close()