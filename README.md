# Statistics Using Python

Welcome to my project! This repository contains all the code and resources related to my awesome project.

## Table of Contents

- statistics.py
- Data Visualization (Images)
- Statistics Summarization
- Data Description

## statistics.py

Python script using Pandas for descriptive statistics.

In this script, it includes the following functions:

## Data Visualization
For more pictures, please see "plots" folder!
![image](https://github.com/nogibjj/hy218_statistics_scipt_week2/blob/main/plots/energy_histogram.png?raw=true)

## Statistics Summarization
The following are the result of the statistics
For danceability, the result means hit songs are more likely to have the ability to make people dance, the median result is also 0.7 which means the deviation is small.
For energy, we can get the same result as danceability.
Artist_popularity is the ranking of songs, the median result is bigger than the mean result which means popular songs above the mean value are less than other songs.
The median result of loudness is smaller than the mean result, meaning loud songs above the mean value are more than other songs.


'mean': 

danceability          0.7
energy                0.7
artist_popularity    72.9
loudness             -5.8
dtype: float64



'median': 

danceability          0.7
energy                0.7
artist_popularity    74.0
loudness             -5.5
dtype: float64

## Data Description

Source
The data is extracted through Spotify API directly. For a comprehensive overview of the data extraction process, you can check out the notebook here.

Content
The dataset includes information on songs/tracks (100 per year) from Top Hit playlists from 2010 to 2022 created by Spotify.

2300 attributes
23 variables
2 playlist related (playlist_url, year)
3 track related (track_id, track_name, track_popularity)
13 track's audio features (danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, duration_ms, time_signature)
1 album related (album)
4 artist related (artist_id, artist_name, artist_genre, artist_popularity)
