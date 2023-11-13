from flask import Flask, request
from flask_cors import CORS
import requests


app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World'


@app.route('/getToken')
def getToken():
    url = "https://api.iq.inrix.com/auth/v1/appToken?appId=&hashToken="

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()['result']['token']


@app.route('/getLots')
def getLots():
    url = "https://api.iq.inrix.com/lots/v3?point=37.74638779388551%7C-122.42209196090698&radius=150"
    auth_token = getToken()

    payload = {}
    headers = {'Authorization': 'Bearer ' + auth_token}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()['result']

@app.route('/processData', methods=['GET'])
def processData():
    adr = request.args.get('address')
    rad = float(request.args.get('radius'))
    latLon = adrToLatLon(adr) 
    lat = str(latLon[0])
    lon = str(latLon[1])
    rad = str(int(rad * 1609)) #convert miles to meters
    
    url = "https://api.iq.inrix.com/blocks/v3?point=" + lat + "%7C" + lon + "&radius=" + rad + "&limit=10"
    auth_token = getToken()

    payload = {}
    headers = {'Authorization': 'Bearer ' + auth_token}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()['result']

@app.route('/adrToLatLon/<adr>', methods=['GET'])
def adrToLatLon(adr):
    adr = adr.replace(" ", "%20")
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + adr + "&key=KEY"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return [response.json()['results'][0]['geometry']['location']['lat'], response.json()['results'][0]['geometry']['location']['lng']]

if __name__ == '__main__':
    app.run(debug=True)