import pytube

video_url = input ("What is url of the youtube video you want to download: ")

yt = pytube.YouTube(video_url)

stream = yt.streams.get_highest_resolution()
stream.download()
print("The video has been downloaded.")