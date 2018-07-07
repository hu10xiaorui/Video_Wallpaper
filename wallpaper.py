from os import system as cmd
from random import randint as rand
import sys
from time import sleep
import ast

movfilesl = open("howmuchmovfiles.txt", "r")
long=movfilesl.read()
print(long)

long=int(long)

movfiles = open("movfiles.txt", "r")
vdlist=movfiles.read()
vdlist = ast.literal_eval(vdlist)
print (vdlist)
print(type(vdlist))

from random import randint as rand

'''
videos={"1":"./alter.mp4","2":"./atthedge.mp4","3":"./candygirl(tsar_remix).mp4","4":"./Fragments.mp4",
"5":"./lovelyrabbitandstarycat.mp4","6":"./mrkittengrove.mp4","7":"./power.mp4","8":"yiran.mp4",
"9":"allweknow.mp4","10":"alone.mp4","11":"alter.mp4","12":"atthedge.mp4","13":"candygirl(tsar_remix).mp4",
"14":"continue.mp4","15":"Fragments.mp4","16":"Hymnfortheweekend(remix).mp4","17":"iknewyouwereintroubl.mp4",
"18":"lookwhatyoumademedo.mp4","19":"luvletter.mp4","20":"movingon.mp4","21":"Nanamori.mp4",
"22":"memsofyou.mp4","23":"newlife.mp4","24":"ninelie.mp4","25":"withoutyou.mp4","26":"lifeline.mp4",
"27":"lifeline1.mp4"}
'''
def help():
    print('''
============================================
Useage:
============================================
$ python3 wallpaper.py [sound] [volume]
                           |
                -mute for nosound
                -sound for sound
                (you have to fill
                 out the volume
                 if you want to
                 have sound)
            You can't leave it blank!
============================================
$ python3 wallpaper.py -h
display this screen
============================================

    ''')
try:
    mute=sys.argv[1]
    if mute == "-mute":
        while(1):
            #give you give few sec to press contrl+c
            cmd("reset")
            print("If you want to stop,press contrl+c now!")
            sleep(2)
            randnum=rand(0,long)
            cmd("xwinwrap -ni -o 1.0 -fs -s -st -sp -b -nf -- mplayer -wid WID -quiet -nosound 0 "+vdlist[randnum])

    elif mute=="-h":
        cmd("reset")
        help()
    elif mute=="-sound":
        try:
            while(1):
                volume=sys.argv[2]
                cmd("reset")
                print("If you want to stop,press contrl+c now!")
                sleep(2)
                randnum=rand(0,long)
                cmd("xwinwrap -ni -o 1.0 -fs -s -st -sp -b -nf -- mplayer -volume "+volume+" -wid WID "+vdlist[randnum])

        except Exception as ine:
            cmd("reset")
            help()
            #print("Error in inner loop:",ine)
#mplayer -volume 40
except Exception as e:
    cmd("reset")
    help()
    #print("Error in outer loop:",e)
