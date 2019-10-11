echo "===>Installing Video_Wallpaper depedence - mplayer"
sudo apt install mplayer
echo "===>Installing Video_Wallpaper depedence - xwinwrap"
sudo apt-get install xorg-dev build-essential libx11-dev x11proto-xext-dev libxrender-dev libxext-dev
git clone https://github.com/ujjwal96/xwinwrap.git
cd xwinwrap
make
sudo make install
make clean

echo Finish installing
echo '''
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
            You can‘t leave it blank!
============================================
$ python3 wallpaper.py -h
display this screen
============================================
$ python3 wallpaper-setup.py
Set the folder with videos that you want to
set as your background
===========================================
'''
