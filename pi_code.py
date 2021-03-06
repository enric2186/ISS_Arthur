import time
import RPi.GPIO as GPIO
from twython import TwythonStreamer

# Search terms - Use a unique hashtag here eg. '#ISSoverheadMyStreet'
TERMS = '#ISSoverhead'


# Setup GPIO as output
GPIO.setmode(GPIO.BOARD)



# GPIO pin number of LED
LED = 36

GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)



# Twitter application authentication
APP_KEY = 'YourTwitterInfoHere'
APP_SECRET = 'YourTwitterInfoHere'
OAUTH_TOKEN = 'YourTwitterInfoHere'
OAUTH_TOKEN_SECRET = 'YourTwitterInfoHere'

# Setup callbacks from Twython Streamer
class BlinkyStreamer(TwythonStreamer):
        def on_success(self, data):
                if 'text' in data:
                        print data['text'].encode('utf-8')
                        print
                        i=0
                        while i < 20:
                        	GPIO.output(LED,1)
                         	time.sleep(0.5)
                         	GPIO.output(LED,0)
                         	time.sleep(0.5)
                         	i = i + 1




# Create streamer
try:
        stream = BlinkyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        stream.statuses.filter(track=TERMS)
except KeyboardInterrupt:
        GPIO.cleanup()

