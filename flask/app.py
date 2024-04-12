import numpy as np

from sqlalchemy.orm import Session
from sqlalchemy import create_engine,  text

from flask import Flask, jsonify, Response

engine = create_engine("sqlite:///taylor.sqlite")

app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/taylor<br/>"
        f"/api/v1.0/taylor3<br/>"
        
    )

@app.route("/api/v1.0/taylor")
def type2()-> Response:


    taylor_group_main = text("SELECT * FROM taylor_main_albums_group")
    data = engine.execute(taylor_group_main)
    
    album_data = {}

    for taylor in data:
        # Use album_name as the key for the current dictionary entry
        album_data[taylor.album_name] = {
            "key": taylor.album_key,
            "popularity": taylor.popularity,
            "acousticness": taylor.acousticness, 
            "valence": taylor.valence,
            "energy": taylor.energy,
            "danceability": taylor.danceability,
            "intrumentalness": taylor.instrumentalness,
            "loudness": taylor.loudness,
            "liveness": taylor.liveness,
            "energy": taylor.energy
        }
    
    all_taylor_group_main = text("SELECT * FROM taylor_group")
    all_data = engine.execute(all_taylor_group_main)
    
    all_album_data = {}

    for taylor in all_data:
        # Use album_name as the key for the current dictionary entry
        all_album_data[taylor.album_name] = {
            "key": taylor.album_key,
            "popularity": taylor.popularity,
            "acousticness": taylor.acousticness, 
            "valence": taylor.valence,
            "energy": taylor.energy,
            "danceability": taylor.danceability,
            "intrumentalness": taylor.instrumentalness,
            "loudness": taylor.loudness,
            "liveness": taylor.liveness,
            "energy": taylor.energy
        }
    
    all_taylor_data = {}

    # Query for song details from taylor_main_albums table
    song_details_query = text("SELECT * FROM taylor_main_albums")
    song_data = engine.execute(song_details_query)

    for song in song_data:
        album_name = song.album_name  # Extract album name

        # Create an empty list for song details if the album doesn't exist in the dictionary
        if album_name not in all_taylor_data:
            all_taylor_data[album_name] = []

        # Add song details as a dictionary to the corresponding album's list
        song_details = {
            "song_name": song.song_name,
            "release_date": song.release_date,
            "album_key": song.album_key,
            "popularity": song.popularity,
            "acousticness": song.acousticness, 
            "valence": song.valence,
            "energy": song.energy,
            "danceability": song.danceability,
            "intrumentalness": song.instrumentalness,
            "loudness": song.loudness,
            "liveness": song.liveness,
            "energy": song.energy
        }
        all_taylor_data[album_name].append(song_details)

    taylor_main = {}

    # Query for song details from taylor_main_albums table
    taylor_main_query = text("SELECT * FROM taylor_main")
    everything = engine.execute(taylor_main_query)

    for song in everything:
        album_name = song.album_name  # Extract album name

        # Create an empty list for song details if the album doesn't exist in the dictionary
        if album_name not in taylor_main:
            taylor_main[album_name] = []

        # Add song details as a dictionary to the corresponding album's list
        song_details = {
            "song_name": song.song_name,
            "release_date": song.release_date,
            "album_key": song.album_key,
            "popularity": song.popularity,
            "acousticness": song.acousticness, 
            "valence": song.valence,
            "energy": song.energy,
            "danceability": song.danceability,
            "intrumentalness": song.instrumentalness,
            "loudness": song.loudness,
            "liveness": song.liveness,
            "energy": song.energy
        }
        taylor_main[album_name].append(song_details)
    
    
    
    
    
    response_data = {"main albums that are grouped average": album_data,
                     "all of main albums taylor": all_taylor_data,
                     "entire discography": taylor_main,
                     "entire discography grouped": all_album_data}


    return make_json_response(response_data)

@app.route("/api/v1.0/taylor3")
def type4():
    taylor_group_main = text("SELECT * FROM taylor_main_albums_group")
    data = engine.execute(taylor_group_main)
    
    album_data = {}

    for taylor in data:
        # Use album_name as the key for the current dictionary entry
        album_data[taylor.album_name] = {
            "key": taylor.album_key,
            "popularity": taylor.popularity,
            "acousticness": taylor.acousticness, 
            "valence": taylor.valence,
            "energy": taylor.energy,
            "danceability": taylor.danceability,
            "intrumentalness": taylor.instrumentalness,
            "loudness": taylor.loudness,
            "liveness": taylor.liveness,
            "energy": taylor.energy
        }
    
    all_taylor_group_main = text("SELECT * FROM taylor_group")
    all_data = engine.execute(all_taylor_group_main)
    
    all_album_data = {}

    for taylor in all_data:
        # Use album_name as the key for the current dictionary entry
        all_album_data[taylor.album_name] = {
            "key": taylor.album_key,
            "popularity": taylor.popularity,
            "acousticness": taylor.acousticness, 
            "valence": taylor.valence,
            "energy": taylor.energy,
            "danceability": taylor.danceability,
            "intrumentalness": taylor.instrumentalness,
            "loudness": taylor.loudness,
            "liveness": taylor.liveness,
            "energy": taylor.energy
        }

    all_taylor_data = {}

    # Query for song details from taylor_main_albums table
    song_details_query = text("SELECT * from taylor_main_albums")
    song_data = engine.execute(song_details_query)

    for song in song_data:
        album_name = song.album_name  # Extract album name

        # Create an empty dictionary for the album if it doesn't exist
        if album_name not in all_taylor_data:
            all_taylor_data[album_name] = {
                "song_names": [],  # List to store song names
                "release_dates": [],  # Additional list for release dates (optional)
                "album_keys": [],   # Additional list for album keys (optional)
                "popularities": [], 
                 "instrumentalness": [],
                 "danceability": [],
                 "loudness": [],
                 "key": [],
                 "liveness": [],
                 "energy": [],
                 "tempo": [],
            }

        # Add song details to the corresponding album's dictionary
        all_taylor_data[album_name]["song_names"].append(song.song_name)

        # Optionally add other details to separate lists (if desired)
        all_taylor_data[album_name]["release_dates"].append(song.release_date)
        all_taylor_data[album_name]["album_keys"].append(song.album_key)
        all_taylor_data[album_name]["popularities"].append(song.popularity)
        all_taylor_data[album_name]["instrumentalness"].append(song.instrumentalness)
        all_taylor_data[album_name]["danceability"].append(song.danceability)
        all_taylor_data[album_name]["loudness"].append(song.loudness)
        all_taylor_data[album_name]["key"].append(song.album_key)
        all_taylor_data[album_name]["liveness"].append(song.liveness)
        all_taylor_data[album_name]["energy"].append(song.energy)
        all_taylor_data[album_name]["tempo"].append(song.tempo)
    
    taylor_main = {}

    # Query for song details from taylor_main_albums table
    taylor_main_query = text("SELECT * from taylor_main")
    everything = engine.execute(taylor_main_query)

    for song in everything:
        album_name = song.album_name  # Extract album name

        # Create an empty dictionary for the album if it doesn't exist
        if album_name not in taylor_main:
            taylor_main[album_name] = {
                "song_names": [],  # List to store song names
                "release_dates": [],  # Additional list for release dates (optional)
                "album_keys": [],   # Additional list for album keys (optional)
                "popularities": [], 
                 "instrumentalness": [],
                 "danceability": [],
                 "loudness": [],
                 "key": [],
                 "liveness": [],
                 "energy": [],
                 "tempo": [],
            }

        # Add song details to the corresponding album's dictionary
        taylor_main[album_name]["song_names"].append(song.song_name)

        # Optionally add other details to separate lists (if desired)
        taylor_main[album_name]["release_dates"].append(song.release_date)
        taylor_main[album_name]["album_keys"].append(song.album_key)
        taylor_main[album_name]["popularities"].append(song.popularity)
        taylor_main[album_name]["instrumentalness"].append(song.instrumentalness)
        taylor_main[album_name]["danceability"].append(song.danceability)
        taylor_main[album_name]["loudness"].append(song.loudness)
        taylor_main[album_name]["key"].append(song.album_key)
        taylor_main[album_name]["liveness"].append(song.liveness)
        taylor_main[album_name]["energy"].append(song.energy)
        taylor_main[album_name]["tempo"].append(song.tempo)
    



        

   
   
   
   
   
    # Wrap the data in a top-level dictionary
    response_data = {"taylor main group": album_data,
        "all of main taylor": all_taylor_data,
        "entire discogrpahy": taylor_main,
        "entire discogrpahy grouped": all_album_data,
    }

    return make_json_response(response_data)



def make_json_response(content) -> Response:
    """Turns a piece of content into a json Response with CORS"""
    response = jsonify(content)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True)