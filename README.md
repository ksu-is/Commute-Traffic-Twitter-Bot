# Commute-Traffic-Twitter-Bot
This will use Twitter API, Tweepy, Tkinter, and  GDOT Twitter Feeds to show relavent updates for Atlanta commuters.
[Requires Tweepy installed]


Google maps is doing a good job of showing you travel times during navigation, but sometimes you need to see at a glance if there are any wrecks near your commute. We’re going to use python and twitter API (accessed using Tweepy library) to give a stream of DOT traffic data that is relavent to major Atlanta highways with one click. Using Tkinter, we will create a graphical user interface to select options and display that data. 

This could be used in conjunction with a touch screen display next to the front door to give at-a-glance traffic data before you hit the road. Or could be combined with text messaging or a phone app’s push messaging to give updates directly to your phone. Mostly, I want to experiment with twitter data and learn how to use an API in my Python programming. I expect that I will want to build some projects in the future using Twitter (auto reply, posting bot, collect tweets and sort, and more)

What you need to know:

Georgia GDOT posts timely traffic updates on their twitter, in a standard format. 
There are separate twitter accounts for each Atlanta-area major highway:
@GDOT_I75_ATL  -  Interstate 75
@GDOT_I85_ATL  -  Interstate 85
@GDOT_I285_ATL  -  Interstate 285
@GDOT_I20_ATL  -  Interstate 20
@GDOT_SR400_ATL  -  State Route 400

In order to interact with twitter, I will need to apply and be accepted for a developer account on developer.twitter.com and recieve the authentication keys for accessing the API. 

We're going to build a window with buttons and a display area in tkinter to interact with the code. Buttons on the user interface would be labeled for each highway, and clicking those buttons would display the last 5 tweets of the relavent highway twitter account (just the text) in a display area. This would show at-a-glance traffic incident information.

Members: Just 1



Links I used to build this :

Get user feed from Twitter API:
https://www.alexkras.com/how-to-get-user-feed-with-twitter-api-and-python/

Using Twitter API:
https://stackabuse.com/accessing-the-twitter-api-with-python/

Using Tweepy to pull single users tweets
https://www.youtube.com/watch?v=KtiGYui68T4

Using Tweepy (documentation)
http://docs.tweepy.org/en/v3.5.0/getting_started.html

Video tutorial I used for learning Tkinter (and a weather api)
https://www.youtube.com/watch?v=D8-snVfekto

