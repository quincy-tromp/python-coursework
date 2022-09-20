import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Scraping Billboard 100
date = input("What year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(url="https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, "html.parser")

songs = soup.find_all(name="h3", class_="a-no-trucate", id="title-of-a-story")
song_titles = [song.getText().replace("\t", "").replace("\n", "") for song in songs]

# Spotify authentication
spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id="3c2b0529e2d44bf9bc24f14faa1f10d", 
        client_secret="475cbb1be73d4ba0bd9f1b9941f4733", 
        redirect_uri="https://example.com", 
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = spotify.current_user()["id"]

# Searching Spotify for songs by title
song_uris = []
year = date[:4]
for song in song_titles:
    result = spotify.search(q=f"track: {song} year: {year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except KeyError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = spotify.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard 100",
    public=False,
    description=f"Top 100 music from {date}"
)

# Adding songs found into the new playlist
spotify.user_playlist_add_tracks(
    user=user_id,
    playlist_id=playlist["id"],
    tracks=song_uris
)

print("Finished adding songs to playlist.")