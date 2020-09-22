#!/usr/local/bin/python3

"""
Will backup all the databases listed, will put files in same DIR as script'
To run: $ python dbbackup.py
"""

import configparser
import os
import time
import getpass
import zipfile
from zipfile import ZipFile

HOST ='127.0.0.1'
DB_USER ='PyBackup'
DB_PASS ='*+*Vs>3ytaUR3g!LV5>r5L&'
DB_BACKUPS = ('auth', 'characters', 'world')
# Lokal
#MYSQLDUMP_PATH = 'C:/Program Files/MySQL/MySQL Server 5.7/bin/mysqldump.exe'

# Root
MYSQLDUMP_PATH = 'C:/Program Files/MySQL/MySQL Server 8.0/bin/mysqldump.exe'
ZIP_PATH = 'backup/zip_file/'

def get_dump(database):
    filestamp = time.strftime('%d.%m.%Y')

    print('"' + MYSQLDUMP_PATH + '" %s > backup/%s.sql -h %s -u %s -p"%s"' % (database, database + '_' + filestamp, HOST, DB_USER, DB_PASS))
    asa = os.popen('"' + MYSQLDUMP_PATH + '" %s > backup/%s.sql -h %s -u %s -p"%s"' % (database, database + '_' + filestamp, HOST, DB_USER,  DB_PASS))
    var = asa.readline()
    for x in var:
        print(x)
    print(str(DB_BACKUPS) + " DB fully dumped to backup/" + database + "_" + filestamp + ".sql \n")
    print('Starting ZIP Function for this DB')
    zip_file(database, filestamp)

def zip_file(database, filestamp):
    print('Starting to ZIP ' + database + 'DB...')
    db_backup_file = "backup/" + database + '_' + filestamp + '.sql'

    filestamp = time.strftime('%d.%m.%Y_%H.%M')

    db_backup_zip = ZIP_PATH + database + '_' + filestamp + '.zip'
    print('Erstelle Archiv...')
    zf = zipfile.ZipFile(db_backup_zip, mode='w', compression=zipfile.ZIP_DEFLATED, compresslevel=9)
    try:
        print('Schreibe Daten in ZIP...')
        zf.write(db_backup_file)
    except:
        print('Zipping fehlgeschlagen...')
    finally:
        print('Schließe Datei...')
        zf.close()

if __name__=="__main__":
    while 1 == 1:
        for DB in DB_BACKUPS:
            get_dump(DB)
        print('Dumped all DBS! Starting to ZIP the Backups.')
        time.sleep(900)