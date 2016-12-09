# Zipfiles.py: main logic for each request
#

import time
import json
import utils
import ziputils
from multiprocessing import Process

FILE_FOLDER = '/var/www/flaskserver/files/'
# FILE_FOLDER = '/Users/pete/PycharmProjects/zipfiles/files/'


# Should take a file and username, and return some type of file ID.
# Should trigger a background job that zips the file.
# Multiple uploads and zips should be able to happen in parallel.
# Return 'fileid' while zipping is done in the background.
def zipupload(filename, username):
    fileid = utils.id_generator()
    print (filename, fileid, username)
    srcpath = FILE_FOLDER + 'upload/'
    dest = FILE_FOLDER + 'zips/' + fileid + '.zip'
    p = Process(target=zipworker, args=(srcpath, filename, dest, fileid, 'zip', username))
    p.start()
    # ziputils.zip_file(srcpath, filename, dest)
    return fileid


# Zip worker for background process
def zipworker(srcpath, filename, dest, fileid, compression, username):
    # Allows for compartmentalization of compression method
    ziputils.zip_file(srcpath, filename, dest)
    # print 'Zipety do da zipety a'
    utils.storeZipInfo(dest, fileid, compression, username, FILE_FOLDER)  # Store zip info
    ### delete_file(srcpath, filename)  # Possibly delete uploaded file to save space


def list_files_mock():
    return [
        {'filename': 'cat.jpg', 'zipfilename': 'cat.jpg.zip', 'username': 'mrblah', 'date': (2016, 11, 4, 21, 2, 38),
         'filesizebytes': 136356, 'zipfilesizebytes': 136468}]


# Return list of the uploaded files, with username, date and size
def list_zipfiles():
    # Get dict of saved files
    almost_a_db = utils.read_dict(FILE_FOLDER + '/almost_a_db.json')  # Lightweight file storage of metadata
    return almost_a_db


# Should take a file ID and return the unzipped file, or an error if the file hasn't been zipped yet.
# This applies to files that were previously uploaded to be zipped or zip files uploaded.
def unzip(fileid):
    zfile = fileid + '.zip'
    zpath = FILE_FOLDER + 'zips/'
    uzfile_folder = FILE_FOLDER + 'unzips/'
    ziputils.unzip_file(zpath, zfile, uzfile_folder)
    zinfo = utils.read_dict(FILE_FOLDER + '/almost_a_db.json')
    filen = zinfo[fileid]['filename']
    return filen


# Main program
if __name__ == '__main__':
    print "Hello"
    #print list_files_mock()
    #ts = time.time()
    #print zipupload('cat2.jpg', 'mrzip')
    #tf = time.time()
    #print tf-ts
    zfileid = 'I6GEVVDOJK'
    zfile = unzip(zfileid)
    print zfile
