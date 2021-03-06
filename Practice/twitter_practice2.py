import sys
import tweepy
import keys
import datetime, time
import tkinter as tk


auth = tweepy.OAuthHandler(keys.TWITTER_APP_KEY, keys.TWITTER_APP_SECRET)
auth.set_access_token(keys.TWITTER_KEY, keys.TWITTER_SECRET)
api = tweepy.API(auth)

def get_tweets(api,username):
    display_message = ""
    try:
        stuff = api.user_timeline(screen_name = username, count = 4, include_rts = False)
        for status in stuff:
            display_message += status.text + "\n\n"
        return display_message
    except tweepy.TweepError as e:
        display_message = "Something went wrong.."
        return display_message

#set up tkinter framework (buttons, label, whatever)

HEIGHT = 600
WIDTH = 600

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='blue_background.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=.01, relwidth=0.80, relheight=0.8, anchor='n')

label = tk.Label(frame, font=('courier', 8), text="", wraplength=450, anchor='w', justify='left')
label.place(relwidth=1, relheight=1)


lower_frame = tk.Frame(root, bg='#80c1ff', bd=5)
lower_frame.place(relx=0.5, rely=0.82, relwidth=0.80, relheight=0.17, anchor='n')

button_75 = tk.Button(lower_frame, text='I-75')
button_75.place(relwidth=0.20, relheight=1)

button_85 = tk.Button(lower_frame, text='I-85')
button_85.place(relx=.20, relwidth=0.20, relheight=1)

button_285 = tk.Button(lower_frame, text='I-285')
button_285.place(relx=.40, relwidth=.20, relheight=1)

button_20 = tk.Button(lower_frame, text='I-20')
button_20.place(relx=0.60, relwidth=0.20, relheight=1)

button_400 = tk.Button(lower_frame, text="SR 400")
button_400.place(relx=0.80, relwidth=0.20, relheight=1)


label.config(text = get_tweets(api, "GDOT_I75_ATL"))

root.mainloop()