# Creating a Spotify Running Playlist with Python and SQL

## Overview

This project uses Python and SQL to build a Spotify running playlist based on insights gathered from data on the Spotify songs that I already listen to while running. As I have gotten better at running over the years, I've realized the importance of running with a high number of steps per minute. I strive to run at about 180 steps per minute, and I find that music helps me stay on pace. Over the past year or two, I have built a playlist of 81 songs that are all around 90 beats per minute (BPM) or 180 beats per minute. However, finding new songs to add to this list is never easy.

Spotify maintains a large amount of data on its songs that is accessible through the [Spotify Web API](https://developer.spotify.com/documentation/web-api/reference/#/). This includes tempo information as well as other audio features such as danceability, energy, and valence. This project uses the spotipy library for Python to extract data on the songs that I currently listen to while running. It then performs an exploratory analysis on the data, figuring out which genres and artists I listen to the most as well as the audio features of the songs on my current running playlist. It uses these insights to query a SQLite database of Spotify data and select a new list of songs, which it then uses to populate a new running playlist directly in Spotify. The result is a playlist of 735 songs that match attributes of the songs I already listen to while running.

## Project Organization

The SQLite database used in this project contains about 600k tracks and 1 million artists. It is very large and is therefore not included in the repository. However, it can be built using the code in my [spotify-database repository](https://github.com/tommcd09/spotify-database). The rest of the project is organized as follows:

* The extract_current_playlist notebook covers extracting data on my current running playlist from Spotify.
* The exploratory_analysis notebook covers exploring the data from my current running playlist and drawing insights on how to search for new songs.
* The populate_playlist notebook covers querying the SQLite database for new songs and populating a new playlist directly in Spotify.
* The spotifyfuncs.py, cleaningfuncs.py, and plottingfuncs.py are modules containing custom functions used in the project.
* The images folder contains images used in the project.
* The requirements.txt files contains packages needed for a virtual environment to run the project.
