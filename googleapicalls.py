import json
import urllib
import requests

from json import load
from urllib import request
from urllib import parse


## AIzaSyCdDlKuUrte_gJiObZqI8P8ArBXndUqzA4

## https://maps.googleapis.com/maps/api/geocode/json?address=GU51&key=AIzaSyCdDlKuUrte_gJiObZqI8P8ArBXndUqzA4

main_api= 'https://maps.googleapis.com/maps/api/geocode/json'
address = 'GU51'
## akey = 'AIzaSyCdDlKuUrte_gJiObZqI8P8ArBXndUqzA4'

url='https://maps.googleapis.com/maps/api/geocode/json?address=GU51'

urls = main_api + urllib.parse.urlencode({'address': address});

## Method 1
jsondata = json.load(urllib.request.urlopen(url))
print(jsondata)
print(jsondata['results'][0]['address_components'])

print(json.dumps(jsondata))

## Method 2
## works on 3.5.2
##jsondata = requests.get(urls).json()