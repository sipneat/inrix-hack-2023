from flask import Flask
import requests


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World'


@app.route('/getToken')
def getToken():
    url = "https://api.iq.inrix.com/auth/v1/appToken?appId=97ld5sp5d8&hashToken=OTdsZDVzcDVkOHxXdkl2dzE3ZDVoR3daSVVYQjdHVWF2ejNrdXRaakZYMUlsQlVhT205"

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

@app.route('/processData/<adr>', methods=['GET'])
def processData(adr):
    latLon = adrToLatLon(adr)
    lat = str(latLon[0])
    lng = str(latLon[1])
    url = "https://api.iq.inrix.com/lots/v3?point=" + lat + "%7C" + lng + "&radius=150"
    auth_token = getToken()

    payload = {}
    headers = {'Authorization': 'Bearer ' + auth_token}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()['result']

def adrToLatLon(adr):
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + adr + "&key=AIzaSyBKpiq156O3XjKxdWvoEeSOWwqeX_ZNW5c"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return [response.json()['results'][0]['geometry']['location']['lat'], response.json()['results'][0]['geometry']['location']['lng']]

if __name__ == '__main__':
    app.run(debug=True)