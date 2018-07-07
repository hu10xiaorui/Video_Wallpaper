import glob
from tkinter.filedialog import askdirectory
folder = askdirectory()
print (folder)
mp4files=glob.glob(folder+"/*.mp4")
movfiles=glob.glob(folder+"/*.mov")
avifiles=glob.glob(folder+"/*.avi")
flvfiles=glob.glob(folder+"/*.flv")
allvideofiles=mp4files+movfiles+avifiles+flvfiles
print (mp4files)
file = open("movfiles.txt","w")
file.write(str(allvideofiles))
file.close()

hl=len(allvideofiles)
hm = open("howmuchmovfiles.txt","w")
hm.write(str(hl))
hm.close()
