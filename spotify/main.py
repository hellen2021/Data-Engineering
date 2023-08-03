from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = client_id + ":" + client_secret
    # encode 
    auth_bytes = auth_string.encode("utf-8")
    # encode using base 64 encoding
    auth_base64_bytes = base64.b64encode(auth_bytes)
    # convert bytes to a string
    auth_base64 = auth_base64_bytes.decode("utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization" : "Basic " + auth_base64,
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    data = {"grant_type" : "client_credentials"}
    result = post(url, headers = headers, data = data)
    # convert json to a dictionary
    json_results = json.loads(result.content)
    token = json_results["access_token"]
    return token

def get_auth_header(token):
     return{"Authorization" : "Bearer "+ token}

# # function to serach for an artist, then search for that artist's top tracks
# def search_for_artist(token, artist_name):
#     url = "https://api.spotify.com/v1/search"
#     headers = get_auth_header(token)
#     query = f"q={artist_name}&type=artist&limit=1"
#     #query = f"q={artist_name}&type = artist&limit = 1"

#     query_url = url + query
#     result = get(query_url, headers = headers)
#     json_results = json.loads(result.content)
#     print(json_results)

def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    
    headers = get_auth_header(token)
    query = f"q={artist_name}&type=artist&limit=1"

    query_url = url + "?" + query  # Add "?" between the base URL and the query
    result = get(query_url, headers=headers)
    json_results = json.loads(result.content)["artists"]["items"]
    
    if len (json_results) == 0:
        print("No artist with this name exist.....")
        return None
    #print(json_results)
    return json_results[0]

def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_results = json.loads(result.content)["tracks"]
    return json_results

token = get_token()
result = search_for_artist(token, "bahati")
artist_id = result["id"]
songs = get_songs_by_artist(token, artist_id)

for idx, song in enumerate(songs):
    print(f"{idx + 1}. {song['name']}")
