# from pytubefix import YouTube
# from pytubefix.cli import on_progress

# video_url = input("enter url: ")
# yt = YouTube(video_url, on_progress_callback=on_progress)

# # get video information
# print(f"title: {yt.title}\ndescription: {yt.description}\nthumbnail url: {yt.thumbnail_url}\nlength: {yt.length}\nviews: {yt.views}")
    
    
# # Download YouTube Videos
# stream = video.streams.get_highest_resolution()
# stream.download()
# print("video downlode completed...")


# # different streams of videos
# streams = yt.streams.all()
# for stream in streams:
#     print(stream)

# # filter only audio strems
# streams = yt.streams.filter(only_audio = True)
# for stream in streams:
#     print(stream)


# # filter only video strems
# streams = yt.streams.filter(only_video = True)
# for stream in streams:
#     print(stream)


# # get a stream with a specific resolution
# streams = yt.streams.filter(res = "720p")
# for stream in streams:
#     print(stream)


# # download specific stream
# stream = yt.streams.get_by_itag(250)
# stream.download()


# # download audio only
# stream = yt.streams.get_audio_only()
# stream.download()

# # Download YouTube playlist
from pytubefix import Playlist

playlist_url = "https://www.youtube.com/watch?v=BFp0gK5ipo8&list=PLo2ANaTOgy-PqrqcP8y6GkY3CFAOAny6W"
playlist = Playlist(playlist_url)

for video in playlist.videos:
    video.streams.get_highest_resolution().download()