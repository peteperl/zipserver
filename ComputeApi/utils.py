import os
import random
import string
import json
import ziputils


# Generates a unique id
def id_generator():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))


def delete_file(directory, fname):
    print os.path.join(directory, fname)
    try:
        os.remove(os.path.join(directory, fname))  # Delete file
        return fname
    except:
        return False


# Write a dict to a file
def write_dict(some_dict, path):
    # save to file:
    with open(path, 'w') as f:
        json.dump(some_dict, f)


# Read dict from a file
def read_dict(path):
    try:
        with open(path, 'r') as f:
            try:
                data = json.load(f)
            except ValueError:  # If the file is empty the ValueError will be thrown
                data = {}
        return data
    except Exception as e:  # Exception if no file
        data = {}
    return data


# Store zip info
def storeZipInfo(zipfile, fileid, compression, username, file_folder):
    zinfo = ziputils.zipinfo(zipfile)[0]  # Get the file details for the 1 file in our present zip
    zinfo['fileid'] = fileid
    zinfo['compression'] = compression
    zinfo['username'] = username

    # Get the present zip info list file
    zipsinfo = read_dict(file_folder + '/almost_a_db.json')

    zipsinfo[fileid] = zinfo  # Add the present zipfile info to the dict

    # Store the updated zip info list file
    write_dict(zipsinfo, file_folder + '/almost_a_db.json')

    return True


# Main program
if __name__ == '__main__':
    print '1'
    FILE_FOLDER = '/Users/pete/PycharmProjects/zipfiles/files/'
    # print delete_file(FILE_FOLDER + 'zips/', '64XSUINL8R.zip')
