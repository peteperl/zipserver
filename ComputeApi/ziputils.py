import os
import zipfile


# Zip src file to dst and return dst filename
def zip_file(srcpath, src, dst):
    # print src
    with zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as myzip:
        myzip.write(os.path.join(srcpath, src), src)  # Zip file without the path
    return dst


# Unzip zipfile and save it to the file_folder
def unzip_file(zpath, zfile, uzfile_folder):
    # print zfile
    # print uzfile_folder
    zf = zipfile.ZipFile(os.path.join(zpath, zfile), 'r')
    zf.extractall(uzfile_folder)
    zf.close()


# Get info from a zip file
def zipinfo(zfname):
    try:
        zf = zipfile.ZipFile(zfname)
        zipfiles = zf.namelist()
    except:
        print 'ERROR: Did not find zipfile %s' % zfname
        return False
    else:
        infolist = []
        for filename in zipfiles:
            zinfo = {}
            try:
                info = zf.getinfo(filename)
            except KeyError:
                print 'ERROR: Did not find %s in zip file' % filename
            else:
                zinfo['filename'] = info.filename
                zinfo['file_size'] = info.file_size
                zinfo['compress_size'] = info.compress_size
                zinfo['date_time'] = info.date_time
                # print '%s is %d bytes, %d zipbytes, on datetime %s' % (info.filename, info.file_size, info.compress_size, info.date_time)
                infolist.append(zinfo)
        return infolist


# Main program
if __name__ == '__main__':
    filedir = "/Users/pete/PycharmProjects/zipfiles/files/"
    # src = "1j_test.jpg"
    # src = "big.txt"
    # zipfname = src + ".zip"

    # print zip_file(filedir+'upload/', src, filedir+'zips/'+zipfname)
    # print zipinfo(filedir+'zips/'+zipfname)

    #unzip_file('', 'UCX7SUZ1OC.zip', filedir+'unzips/')
