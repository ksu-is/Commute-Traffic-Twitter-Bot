# Commute-Traffic-Twitter-Bot
This will use Twitter API and  GDOT Twitter Feeds to show relavent updates depending on your weekday commute. 

Google maps is doing a good job of showing you travel times during navigation, but sometimes you need to see at a glance if there are any wrecks near your commute. We’re going to use python and twitter to give a stream of DOT traffic data that is relevant to your route. This app would be used by anyone that is traveling on a regular schedule as in a normal commute to work. It would ask for your travel patterns, and filter out all the irrelevant data to only display wreck/clearing data on the route you specified. 
This could be used in conjunction with a 20x4 LCD display next to the front door to give at-a-glance traffic data before you hit the road. Or could be combined with text messaging or a phone app’s push messaging to give updates directly to your phone. Mostly, I want to experiment with twitter data and learn how to use an API in my Python programming. I expect that I will want to build some projects in the future using Twitter (auto reply, posting bot, collect tweets and sort, and more)
What you need to know:
Georgia GDOT posts timely traffic updates on their twitter, in a standard format:
First, the app would determine user commute (choose a highway):
-My morning commute (m-f):   (75 South, 75 North, 85 South, 85 North, 285 any, I20 west, I20 East)
-My Evening Commute (m-f):   (75 SB 75 NB, 85 SB, 85 NB, 285 any, I20 WB, I20 EB)
App would use twitter API to receive tweets from Georgia DOT Twitter.
During the morning time (5am-9am) the app would display the tweets that contain user’s MORNING highway choice (ex “I-20 EB”).
During the afternoon/evening time (3pm-7pm) the app would display the tweet that contain the user’s EVENING highway choice. 
Members: Just 1
Get user feed from Twitter API:
https://www.alexkras.com/how-to-get-user-feed-with-twitter-api-and-python/
Using Twitter API:
https://stackabuse.com/accessing-the-twitter-api-with-python/
Twitter Feed Display Using Raspberry Pi And 20x4 LCD:
https://www.hackster.io/samik/twitter-feed-display-using-raspberry-pi-and-20x4-lcd-875640
An alternative to this project could be a program that constantly displays commute time. Could use Google Maps to calc and display commute times on a LCD Display using Raspberry Pi:
https://www.hackster.io/dilpreet/display-commute-time-on-lcd-using-raspberry-pi-183ff0


