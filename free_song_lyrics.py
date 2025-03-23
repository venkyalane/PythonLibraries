import lyricsgenius

# # https://docs.genius.com/
api_key = "hnrVa5iJ7ZSj1cDk9b_RvYX_Rbh4hZhUSuv-YdiX9w4ZYNTsMoePT1pxw4rSLqLG"
genius = lyricsgenius. Genius (api_key)
name = input("Enter Artist Name: ")
artist = genius.search_artist(name)
song = input("Type your song for Lyrics: ")
song = artist.song(song)
print(song.lyrics)