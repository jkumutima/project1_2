import flask
import requests
import json
import spotipy
# import pandas as pd
import random
from flask import render_template

app=flask.Flask(__name__)

artist_id = '1uNFoZAHBGtllmzznpCI3s'

@app.route('/')
def index():
    headers = { 'Accept':'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer BQC-3BhjWwIxyoTKW8atsZPZBD_c1RoIgRPS2N-Lmc7_Vs3JlFCEgg69c3PSIGwrCc771daUvVF-CdnYh0syh4s3DcKnuEt3mhVS_sNnJGWXdO2_5HP8BrSEB0Bez7zbi7FktNNobH7ZwtbNBCaNvraB9ZlOQKJlUTEOfaEG2zKt2dJMSAfbnM3cqr1bKQbvL9Y'}
    response = requests.get('https://api.spotify.com/v1/artists/{}'.format(artist_id), headers=headers)
    response_payload = response.json()
    popularity = response_payload['popularity']
    genres = response_payload['genres']

    top_five_response = requests.get('https://api.spotify.com/v1/artists/{}/top-tracks?market=ES'.format(artist_id), headers=headers)
    top_five = top_five_response.json()
    random_song = random.choice(top_five['tracks'])

    # create token from genius api
    # genius api url for songs
    # get random song url

    return render_template('index.html', popularity=popularity, genres=genres, random_song=random_song)
app.run()