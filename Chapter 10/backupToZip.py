#! /usr/bin/env python3

'''
backupToZip.py - Copies an entire folder and its content
into a ZIP file whose filename increments
'''
import zipfile, os
from pathlib import Path

USAGE_TEXT = 'usage: python3 backupToZip <directory>'
INVALID_DIR_TEXT = 'Invalid directory %s!'
BACKUP_DIR = '/Users/jorge/.backups/'

def backupToZip(directory):
    path = Path(directory)
    if not path.is_dir():
       print(INVALID_DIR_TEXT % (directory))
       sys.exit(1)

    path = os.path.abspath(path)

    # Find appropriate backup folder #
    i = 1
    zipFileName = BACKUP_DIR + os.path.basename(path) + '_backup{}.zip'
    while os.path.exists(zipFileName.format(i)):
        i += 1

    zipFileName = zipFileName.format(i)

    # Create the ZIP file
    print(f'Creating {zipFileName}')
    backupZipFile = zipfile.ZipFile(zipFileName, 'w')

    # Compress each file in folder
    for folderName, subfolders, filenames in os.walk(path):
        print(f'Adding files in {folderName}')
        backupZipFile.write(folderName)


        for filename in filenames:
            backupBase = os.path.basename(folderName) + '_backup'
            # Skip already-created backup folders
            if filename.startswith(backupBase) and filename.endswith('.zip'):
                continue

            print(Path(folderName) / filename)
            backupZipFile.write(Path(folderName) / filename)
    
    backupZipFile.close()
    print('Backup complete.')

backupToZip('.')
