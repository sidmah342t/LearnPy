import os
import shutil
import urllib
import json

## play with json
## Call an API that returns json and parse json

from os import path
from urllib import request
from json import load

def main():
    src = ""
    ## Get Current Working directory
    print ("Current working directory is:" + os.getcwd())
    ## Check if File Exists
    if path.exists("file1.txt"):
        src = path.realpath("file1.txt")
    else:
        print("No file found")

    print (src)

    ### Google API Key
    ### AIzaSyCBSeezk3A07zgvK06EsuMUXeL4ALfTzHg

    ### https://roads.googleapis.com/v1/nearestRoads?points=60.170880,24.942795|60.170879,24.942796|60.170877,24.942796&key=AIzaSyCBSeezk3A07zgvK06EsuMUXeL4ALfTzHg



    url = "https://roads.googleapis.com/v1/nearestRoads?points=60.170880,24.942795|60.170879,24.942796|60.170877,24.942796&key=AIzaSyCBSeezk3A07zgvK06EsuMUXeL4ALfTzHg"

    ##urllib.request.urlopen("https://roads.googleapis.com/v1/nearestRoads?points=60.170880,24.942795|60.170879,24.942796|60.170877,24.942796&key=AIzaSyCBSeezk3A07zgvK06EsuMUXeL4ALfTzHg")
    print(json.load(urllib.request.urlopen("https://roads.googleapis.com/v1/nearestRoads?points=60.170880,24.942795|60.170879,24.942796|60.170877,24.942796&key=AIzaSyCBSeezk3A07zgvK06EsuMUXeL4ALfTzHg")))

    jsondata = json.load(urllib.request.urlopen(url))
    print(jsondata)
    print(jsondata['snappedPoints'])

    listread = jsondata['snappedPoints'] ## json datais a dictionary

    print(len(listread))

    print(listread[0])
    print(listread[1])
    print(listread[2])

    print(listread[0]['location'])
    print(listread[0]['location']['latitude'])
    print(listread[0]['location']['longitude'])
    print(listread[0]['placeId'])

    for item in listread:
        print('########')
        print(item['location'])
        print(item['location']['latitude'])
        print(item['location']['longitude'])
        print(item['placeId'])


main()