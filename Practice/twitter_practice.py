import sys
import tweepy
import keys
import datetime, time
import tkinter as tk
import requests


auth = tweepy.OAuthHandler(keys.TWITTER_APP_KEY, keys.TWITTER_APP_SECRET)
auth.set_access_token(keys.TWITTER_KEY, keys.TWITTER_SECRET)
api = tweepy.API(auth)


#the function for actually retrieving tweets for a username. Count = the number of tweets
def get_tweets(api,username):
    display_message = ""
    try:
        stuff = api.user_timeline(screen_name = username, count = 5, include_rts = False)
        for status in stuff:
            display_message += status.text + "\n\n"
        return display_message
    except tweepy.TweepError as e:
        display_message = "Something went wrong.."
        return display_message

#button actions, how it writes the retrieved tweets into the label 
def write_75():
    #message = "You've clicked on I-75"
    label.config(text = get_tweets(api, "GDOT_I75_ATL"))
def write_85():
    #message = "You've clicked on I-85"
    label.config(text = get_tweets(api, "GDOT_I85_ATL"))
def write_285():
    #message = "You've clicked on I-285"
    label.config(text = get_tweets(api, "GDOT_I285_ATL"))
def write_20():
    #message = "You've clicked on I-20"
    label.config(text = get_tweets(api, "GDOT_I20_ATL"))
def write_400():
    #message = "You've clicked on SR 400"
    label.config(text = get_tweets(api, "GDOT_SR400_ATL"))
    
#set up tkinter framework (buttons, label, whatever)

HEIGHT = 600
WIDTH = 600

root = tk.Tk()
root.title("Atlanta Highway Incidents")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='blue_background.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

#upper
frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=.01, relwidth=0.80, relheight=0.8, anchor='n')

label = tk.Label(frame, font=('verdana', 11), text="", wraplength=450, anchor='w', justify='left')
label.place(relwidth=1, relheight=1)

#lower
lower_frame = tk.Frame(root, bg='#80c1ff', bd=5)
lower_frame.place(relx=0.5, rely=0.82, relwidth=0.80, relheight=0.17, anchor='n')

button_75 = tk.Button(lower_frame, text='I-75', font=("verdana", 14), command= write_75)
button_75.place(relwidth=0.20, relheight=1)

button_85 = tk.Button(lower_frame, text='I-85', font=("verdana", 14), command= write_85)
button_85.place(relx=.20, relwidth=0.20, relheight=1)

button_285 = tk.Button(lower_frame, text='I-285', font=("verdana", 14), command= write_285)
button_285.place(relx=.40, relwidth=.20, relheight=1)

button_20 = tk.Button(lower_frame, text='I-20', font=("verdana", 14), command= write_20)
button_20.place(relx=0.60, relwidth=0.20, relheight=1)

button_400 = tk.Button(lower_frame, text="SR 400", font=("verdana", 14), command= write_400)
button_400.place(relx=0.80, relwidth=0.20, relheight=1)


#get_tweets(api, "GDOT_I75_ATL")


root.mainloop()