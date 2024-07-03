# YouTube_Query_Automation
YouTube Query Automation
Overview
This is a Python program that takes a topic to search on YouTube as input and returns two CSV files: one containing video-related data and the other containing playlist-related data. The program is designed to automate the process of gathering detailed information about YouTube videos and playlists based on a given query using Selenium.

Features
Automated YouTube Search with Selenium: Enter a topic and the program uses Selenium to automatically search YouTube for videos and playlists related to that topic.
CSV File Generation: The program generates two CSV files:
video_data.csv: Contains data about the videos related to the search query.
playlist_data.csv: Contains data about the playlists related to the search query.
Detailed Video Data: The video_data.csv file includes the following columns:
Query No: A unique identifier for the search query.
Query: The search topic entered by the user.
Video No: A unique identifier for each video.
Title: The title of the video.
Views: The number of views the video has.
Channel: The name of the channel that uploaded the video.
Length: The duration of the video.
Upload Date: The date the video was uploaded.
Video Link: The URL to the video.
Channel Link: The URL to the channel.
Detailed Playlist Data: The playlist_data.csv file includes the following columns:
Query No: A unique identifier for the search query.
Query: The search topic entered by the user.
Playlist No: A unique identifier for each playlist.
Title: The title of the playlist.
No of Videos: The number of videos in the playlist.
Views: The number of views the playlist has.
Channel: The name of the channel that created the playlist.
Total Length: The total duration of all videos in the playlist.
Avg Length: The average duration of the videos in the playlist.
Last Upload Date: The date of the most recent video uploaded in the playlist.
Playlist Link: The URL to the playlist.
Channel Link: The URL to the channel.
Installation
Prerequisites
Python 3.x
Selenium
WebDriver (e.g., ChromeDriver)
YouTube Data API key
Steps
Clone the repository:
sh
Copy code
git clone https://github.com/AIML-Sagnik-Ghosal/YouTube_Query_Automation.git
Navigate into the project directory:
sh
Copy code
cd YouTube_Query_Automation
Install dependencies:
sh
Copy code
pip install -r requirements.txt
Download and set up WebDriver:
For ChromeDriver, download from here and place it in a directory included in your system's PATH.
Usage
To use the program, follow these steps:

Run the application:
sh
Copy code
python main.py
Enter the topic to search on YouTube when prompted.
The program will generate two CSV files: video_data.csv and playlist_data.csv with the relevant information.
Analyzing the CSV Data
The data in the generated CSV files can be used to perform various analyses to determine the quality and relevance of videos and playlists:

Selecting Best Quality Videos or Playlists:

Based on Views: Sort the Views column in descending order to find the most viewed videos or playlists.
Based on Length: For videos, sort the Length column. For playlists, consider the Total Length or Avg Length to find those that best match your preference for content duration.
Based on Upload Date: Sort the Upload Date column in descending order to find the most recently uploaded videos or the Last Upload Date for playlists.
Frequent Channels:

Use the Channel column to count occurrences of each channel. This will help identify which channels are most frequent or popular among the search results for a given query.
Combining Results from Different Queries:

Combine multiple CSV files by merging them based on the Query No and Query columns.
Perform aggregate analysis to compare results from different queries. For example, compare the total views or the number of videos from each query to identify trends or popular topics.
By analyzing these aspects, you can make informed decisions about which videos or playlists are of higher quality or more relevant to your needs.
