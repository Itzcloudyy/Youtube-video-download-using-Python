print("\n****************************************************************")
print("\n* Copyright of Nitin Sharma, 2022                              *")
print("\n* Black and White Hat Hacking                                  *")
print("\n* Instagram @itzcloudy9                         *")
print("\n****************************************************************")

from pytube import YouTube
url = ' Your Video Link '
my_video = YouTube(url)
print(my_video.title)
print(my_video.thumbnail_url)
my_video = my_video.streams.first()
my_video.download()