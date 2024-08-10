import vlc
import time
import RPi.GPIO as GPIO
import random


#This tells the gpio to use board numberings for pins rather than gpio numbers
GPIO.setmode(GPIO.BOARD)

#Set pin 40 to an input pin and tell it to star low/off
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Now we create an instance of the VLC player
player = vlc.Instance()

#We create a media list - this is only to ensure that we can loop the video,
#but normally we'd have more than one media source in this list
mediaList= player.media_list_new()

#Now we make a new player and tell it that it is specifically a list player
mediaPlayer = player.media_list_player_new()

#Creating a new media source and adding that media to our list of media
media = player.media_new("/home/pi/Desktop/Hall/HauntedHallVideo.mp4")
mediaList.add_media(media)

#And here we tell the media player what list it should be using
mediaPlayer.set_media_list(mediaList)

#THIS TELLS IT TO LOOP THE VIDEO
#You wouldn't beleive how annoying this was to find
mediaPlayer.set_playback_mode(1)

mediaPlayer.get_media_player().set_fullscreen(True)
#Setting up pins for the lamp controls
GPIO.setup(38, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.output(36, GPIO.LOW)
GPIO.output(38, GPIO.LOW)

mediaPlayer.play()
time.sleep(2)
mediaPlayer.set_pause(True)
mediaPlayer.get_media_player().set_position(0.0)
lights = True
loops = 0
while(True):
    if GPIO.input(40)==GPIO.HIGH:
        time.sleep(0.5)
        if GPIO.input(40)==GPIO.HIGH:        
            print("Button Pushed")
            mediaPlayer.set_pause(False)
            time.sleep(2)
            if lights ==True:
                while(loops <2):
                    GPIO.output(38, GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(38, GPIO.LOW)
                    GPIO.output(36, GPIO.HIGH)
                    time.sleep(0.3)
                    GPIO.output(38, GPIO.HIGH)
                    time.sleep(1)
                    GPIO.output(36, GPIO.LOW)
                    GPIO.output(38, GPIO.LOW)
                    time.sleep(1)
                    GPIO.output(36, GPIO.HIGH)
                    time.sleep(0.1)
                    GPIO.output(36, GPIO.LOW)
                    time.sleep(0.1)
                    GPIO.output(36, GPIO.HIGH)
                    GPIO.output(38, GPIO.HIGH)
                    time.sleep(0.2)
                    GPIO.output(36, GPIO.LOW)
                    GPIO.output(38, GPIO.LOW)
                    time.sleep(0.1)
                    GPIO.output(36, GPIO.HIGH)
                    GPIO.output(38, GPIO.HIGH)
                    time.sleep(5)
                    GPIO.output(36, GPIO.LOW)
                    time.sleep(2)
                    GPIO.output(38, GPIO.LOW)
                    loops=loops+1
                time.sleep(22)
        if GPIO.input(40)==GPIO.LOW:
            print("Button Released")
            mediaPlayer.set_pause(True)
            time.sleep(2)
            mediaPlayer.get_media_player().set_position(0.0)
            GPIO.output(36, GPIO.LOW)
            GPIO.output(38, GPIO.LOW)
            loops=0
    
    