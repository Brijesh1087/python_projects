import pytube as pt
#link = "https://youtu.be/JdG1cVFyj5A"
#link = "https://youtu.be/OKuiyX5k6zg"
print("\033c")
print(" ***** YouTube Video Downloader ***** ")
link = input("Enter YouTube URL : " )
print("Processing...")
y = pt.YouTube(link)
v = y.streams.all()
#l = list(enumerate(v))
#for x in l:
  #print(x)
print("\033c")
print("1. Video \n2. Audio")
ts = int(input("Enter Index : " ))
if(ts == 1):
  print("Downloading...")
  v[1].download()
elif ts == 2:
  print("Downloading...")
  v[25].download()
else:
  print("Please Correct Number ?" )
print("Finished")
