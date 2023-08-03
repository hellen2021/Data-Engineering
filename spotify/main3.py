import requests
import csv

# Spotify API credentials
CLIENT_ID = "0caf14de63e749278b4a64e890889cc2"
CLIENT_SECRET = "6a5cacd8fde3419e8d7290b0652d7d2c"

# Function to get the access token
def get_access_token(client_id, client_secret):
    url = 'https://accounts.spotify.com/api/token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'grant_type': 'client_credentials'}

    response = requests.post(url, headers=headers, auth=(client_id, client_secret), data=data)
    access_token = response.json().get('access_token')
    return access_token

# Function to search for a track and get its information
def get_track_info(access_token, track_name):
    url = 'https://api.spotify.com/v1/search'
    headers = {'Authorization': f'Bearer {access_token}'}
    params = {'q': track_name, 'type': 'track', 'limit': 1}

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    if 'tracks' in data and 'items' in data['tracks']:
        track = data['tracks']['items'][0]
        track_info = {
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'genre': 'Genre information not directly available through the API',
            'popularity': track['popularity']
        }
        return track_info
    else:
        return None

# Function to extract songs from different artists and save to CSV
# def extract_songs_to_csv(file_path):
#     # Read the list of track names and artists from a file (one track per line)
#     with open(file_path, 'r') as file:
#         tracks = file.read().splitlines()

#     access_token = get_access_token(CLIENT_ID, CLIENT_SECRET)

#     # List to store track information for all songs
#     all_tracks_info = []

#     for track in tracks:
#         track_info = get_track_info(access_token, track)
#         if track_info:
#             all_tracks_info.append(track_info)

#     # Save the data to a CSV file
#     csv_file_path = 'extracted_songs.csv'
#     with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
#         fieldnames = ['Track', 'Artist', 'Popularity']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()
#         for track_info in all_tracks_info:
#             writer.writerow({'Track': track_info['name'], 'Artist': track_info['artist'], 'Popularity': track_info['popularity']})

# # Example usage

def extract_songs_to_csv(file_path):
    # Ensure the provided file path is valid
    try:
        with open(file_path, 'r') as file:
            tracks = file.read().splitlines()
    except FileNotFoundError:
        print(f"File not found: {C:\Users\Elle\Documents\dataEng\spotify}")
        return
if __name__ == '__main__':
    # Replace 'track_list.txt' with the path to your file containing the list of track names
    extract_songs_to_csv('track_list.txt')
