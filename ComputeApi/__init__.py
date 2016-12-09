from flask import Flask, request
import flask
from flask import send_from_directory
from flask.ext.cors import CORS
import os
import json
import logging
import zipfile
import utils
import zipfiles
import ziputils
import time
from werkzeug.utils import secure_filename

# logging.basicConfig(filename='/var/www/flaskserver/log/server.log',level=logging.INFO)
logging.getLogger('flask_cors').level = logging.INFO

FILE_FOLDER = '/var/www/flaskserver/files'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

# Get dict of saved files
try:
    almost_a_db = utils.read_dict(UPLOAD_FOLDER + '/almost_a_db.json')
except Exception as e:
    almost_a_db = {}

app = Flask(__name__)

# addin an upload folder
app.config['UPLOAD_FOLDER'] = FILE_FOLDER + '/upload'
app.config['ZIP_FOLDER'] = FILE_FOLDER + '/zips'
app.config['UNZIP_FOLDER'] = FILE_FOLDER + '/unzips'
CORS(app)


@app.route('/')
def home():
    return 'Home sweet home'


@app.route('/test')
def test():
    return 'Test a route: Success!!'


# Check if file extension is allowed
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# Route that will process the file upload and send for background zipping
@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        # Extract details from request
        file = request.files['file']
        username = request.form['username']

        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.filename)

        # Save file to UPLOAD_FOLDER
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Start the background zipping
        fileid = zipfiles.zipupload(filename, username)

        return fileid

    else:
        # If it is a GET method create an upload website
        return """
            <!doctype html>
            <title>Upload new File</title>
            <h1>Upload new File</h1>
            <form action="" method=post enctype=multipart/form-data>
              <p><input type=file name=file>
                 <input type=submit value=Upload>
            </form>
            <p>%s</p>
            """ % "<br>".join(os.listdir(app.config['UPLOAD_FOLDER'], ))


@app.route('/uploads/<filename>')
def download_file(filename):
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    except Exception as e:
        return 'That file has not been uploaded to the server'


# See zip files on the server
@app.route('/seezip')
def seezip():
    return """
        <!doctype html>
        <title>Zips</title>
        <h1>Zips on server</h1>
        <p>%s</p>
        """ % "<br>".join(os.listdir(app.config['ZIP_FOLDER'], ))


# Retrieve zip file from server
@app.route('/retrievezip/<fileid>')
def retrievezip(fileid):
    try:
        return send_from_directory(app.config['ZIP_FOLDER'], fileid + '.zip')
    except Exception as e:
        return 'Your file has not been zipped yet'


# Get files listing from the server
@app.route('/listfiles')
def get_listfiles():
    return json.dumps(zipfiles.list_zipfiles())


# Get unzipped file from the server
@app.route('/unzip/<fileid>')
def get_unzipped(fileid):
    try:
        filename = zipfiles.unzip(fileid)
        return send_from_directory(app.config['UNZIP_FOLDER'], filename)
    except Exception as e:
        return 'There is no such a file'


if __name__ == '__main__':
    app.run(debug=True)
