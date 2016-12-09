# Zipfiles Server

Simple zipfile server via a Flask API.  

## Details

All of the code logic is in the 'ComputeApi' directory.  

My server is here: http://54.197.64.168/  
  
See some zips:  
http://54.197.64.168/seezip  

Soon you will get to zip a cat:  
http://54.197.64.168/uploads/yourupload  

Run the test script:  

    python test_script.py
  
  
## Done
  
Uploading a file & background zipping.  
Store data for file uploads & zips. Retrieving zip file data.
Retrieving uploaded file.  
Retrieving zipped file.  
Endpoint for unzipping files.  
Basic web UI to view & upload files (in progress). Uploading via the UI does not trigger zipping.  
Compartmentalized zip & tag for compression format. For each format you need to make a function in ziputils.py & 
add the compression format tag to what is passed to the 'upload' route and then through to zipfiles.py.  
  
  
## Setup

Start an instance (Ubuntu 14.04) and open the HTTP ports.  

ssh into the instance.  

Download the repo and unzip. (you may need to: sudo apt-get install unzip)  
Or git clone the repo.  

You must now have a 'zipserver' directory in your home directory.  

Go into the repo directory:  

    cd zipserver

In the compute-api.conf file, change the ServerName to your domain or cloud server's IP address:  

    vi compute-api.conf

Install the necessary dependencies and setup by running:  

    ./setup_node
  
