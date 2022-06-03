import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials


def authenticate_general(client_id, client_secret):
    """Takes a Spotify client ID and client secret,
    authenticates and returns spotipy object.
    """
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id,
                                                      client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    return sp


def authenticate_user(username, scope, client_id, client_secret, redirect_uri):
    """Takes a Spotify username, scope, client ID, client secret,
    and redirect URI, authenticates with user's account and returns
    spotipy object.
    """
    token = spotipy.util.prompt_for_user_token(
        username,
        scope,
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri)
    sp = spotipy.Spotify(auth=token)
    return sp


def get_track_uris(playlist, sp):
    """Takes a Spotify playlist URL and spotipy object, returns URIs of playlist tracks."""
    playlist_uri = playlist.split('/')[-1].split('?')[0]
    track_uris = [x['track']['uri'] for x in sp.playlist_tracks(playlist_uri)['items']]
    return track_uris


def get_track_data(playlist, sp):
    """Takes a Spotify playlist URL and spotipy object,
    returns DataFrame of data for tracks on playlist.
    """
    playlist_uri = playlist.split('/')[-1].split('?')[0]
    tracks = get_track_uris(playlist, sp)
    track_features = sp.audio_features(tracks) #Get track audio features
    tracks_df = pd.json_normalize(track_features)
    tracks_df['track_pop'] = [track['track']['popularity'] #Get track popularity
                              for track in sp.playlist_tracks(playlist_uri)['items']]
    tracks_df['name'] = [track['track']['name'] #Get track name
                         for track in sp.playlist_tracks(playlist_uri)['items']]
    tracks_df['artist'] = [track['track']['artists'][0]['name'] #Get main artist name
                           for track in sp.playlist_tracks(playlist_uri)['items']]
    tracks_df['artist_id'] = [track['track']['artists'][0]['uri'] #Get main artist ID
                              for track in sp.playlist_tracks(playlist_uri)['items']]
    artist_info = [sp.artist(artist_id) for artist_id in tracks_df['artist_id']]
    tracks_df['artist_genres'] = [artist_info[i]['genres'] #Get artist genres
                                  for i in range(len(artist_info))]
    return tracks_df


def get_playlist_id(username, playlist_name, sp):
    """Takes Spotify username, playlist name and spotipy object,
    returns Spotify ID of that playlist.
    """
    playlist_id = ''
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:
        if playlist['name'] == playlist_name:
            playlist_id = playlist['id']
    return playlist_id


def populate_playlist(username, playlist_id, track_uris, sp):
    """Takes a Spotify username, playlist ID, list of track URIs, and spotipy object,
    populates playlist with tracks from list.
    """
    for i in range(0, len(track_uris), 100):
        sp.user_playlist_add_tracks(username, playlist_id, track_uris[i:i + 100])
