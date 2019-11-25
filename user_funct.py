


## will create text file for new users with info on each line. (not able to do OOP yet reliably so this is the best I've got)
# do you have an account?
user_ask = input("Before we start, lets specify what user this is for\nHave you used this program before?\nType 'y' or 'n' only:    ")

if user_ask.lower() == "n":
    filename = input("Okay, new user! What is your name?\nType your first name here to create your username:   ").lower() + ".txt"
    user_file = open(filename, 'w+')
    print("\nNow lets load up all the highways that you use for your commute into your user account.")

#at this point, i am able to make a custom text file for any new user
    while True:
        append = input("\nEnter one highway at a time\nType '75', '85, '285', '20', or '400'\nOr type 'end' to finish.\nEnter here:  ")
        if append.lower() == "end":
            break
        else:
            user_file.write(append)
            user_file.write("\n")
    user_file.seek(0)
    print(user_file.readlines())




#def make_user():