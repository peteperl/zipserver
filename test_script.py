# Usage: python test_script.py
#
# Make sure to change the file in the 'main' below
#

import time
import urllib2
import requests
import json

server_url = 'http://104.155.153.18/'


# Just a server test
def test_server():
    return urllib2.urlopen(server_url + 'test').read()


# Uploading a file
def upload_file_test(filename, username):
    """
        Sends POST sequest to the server, uploading the file
    """
    files = {'file': open(filename, 'rb')}
    payload = {'username': username}
    response = requests.post(server_url + 'upload', files=files, data=payload)
    print 'Your uploaded file unic id: ' + response.content
    return response.content


# Retrieves file by its unic Id from the server
def retrieve_file(fileid):
    """
        Saves a zipped file from the server
    """
    response = requests.get(server_url + 'retrievezip/' + fileid)
    try:
        zipfilen = fileid + '.zip'
        with open(zipfilen, 'w') as f:
            f.write(response.content)
        return 'Zip file has been saved'
    except:
        return response.text


# Get listing of files on server
def get_listfiles():
    """
        Returns a dict of the zips info
    """
    response = requests.get(server_url + 'listfiles')
    return json.loads(response.content)


def unzip(fileid):
    """
        Returns the unzipped file of a zipfile already on the server
    """
    response = requests.get(server_url + 'unzip/' + fileid)
    try:
        response_info = requests.get(server_url + 'listfiles')
        zinfo = json.loads(response_info.content)
        filen = zinfo[fileid]['filename']
        with open(filen, 'w') as f:
            f.write(response.content)
        return 'Unzipped file has been saved'
    except:
        return response.text


if __name__ == '__main__':
    """
    afile = 'cat.jpg'
    username = 'mrzip'

    print test_server()

    print '* Testing: upload'
    fileid = upload_file_test('cat.jpg', 'mrzip')
    print fileid

    print '* Testing: retrieve zip'
    print retrieve_file(fileid)
    time.sleep(1)
    print retrieve_file(fileid)

    print '* Testing: listfiles'
    print get_listfiles()
    """
    print 'Testing: unzip'
    print unzip('JNUVA2XJ49')
