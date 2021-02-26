import os
import requests
from webexteamsbot import TeamsBot
from webexteamsbot.models import Response
import sys
import json
import pyautogui
import pygetwindow 
import datetime
from PIL import Image

bot_email = "HackandCodey@webex.bot"
teams_token = "ODViODBlNzAtZmY4ZC00ZjFmLTgwM2MtYzhjOTQ1NzFmN2FmZDFjNmM1ZjItZjUw_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
bot_url =  "http://a0b3d64dccde.ngrok.io"
bot_app_name = "Hack And Codey"



if not bot_email or not teams_token or not bot_url or not bot_app_name:
    print(
        "sample.py - Missing Environment Variable. Please see the 'Usage'"
        " section in the README."
    )
    if not bot_email:
        print("TEAMS_BOT_EMAIL")
    if not teams_token:
        print("TEAMS_BOT_TOKEN")
    if not bot_url:
        print("TEAMS_BOT_URL")
    if not bot_app_name:
        print("TEAMS_BOT_APP_NAME")
    sys.exit()

# Create a Bot Object
#   Note: debug mode prints out more details about processing to terminal
#   Note: the `approved_users=approved_users` line commented out and shown as reference
bot = TeamsBot(
    bot_app_name,
    teams_bot_token=teams_token,
    teams_bot_url=bot_url,
    teams_bot_email=bot_email,
    debug=True,
    # approved_users=approved_users,
    webhook_resource_event=[
        {"resource": "messages", "event": "created"},
        {"resource": "attachmentActions", "event": "created"},
    ],
)


def botgreeting(incoming_msg):
    
    sender = bot.teams.people.get(incoming_msg.personId)

    response = Response()
    #welome message
    response.markdown = "Hi {}, The Suite Life of Hack and Codey Bot here! ".format(sender.firstName)
    

   
    response.markdown += "Check out the bot features available by typing **/help**."
    return response


#function below which generates screenshot 
def capturescreen(incoming_msg):
   
    response = Response()
    datetime_object = datetime.datetime.now()
    print(datetime_object)
    response.text = "Here is your current Network Health as of " + str(datetime_object)
    
    #im1 = pyautogui.screenshot()
    #im1.save (r"C:\Users\aykorri\OneDrive - Cisco\Desktop\SE Hack\screenshot.png")

    path = (r"C:\Users\aykorri\OneDrive - Cisco\Desktop\SE Hack\screenshot.png")
    #titles = pygetwindow.getAllTitles()

    #x1, y1, width, height = pygetwindow.getWindowGeometry('How to screenshot a specific window using Python')
    #x2 = x1 + width
    #y2 = y1 + height

    #pyautogui.screenshot(path)

    #im = Image.open(path)
    #im = im.crop((x1, y1, x2, y2))
    #im.save(path)
    #im.show(path)

    u = r"C:\Users\aykorri\OneDrive - Cisco\Desktop\SE Hack\screenshot.png"
    response.files = u
    return response


bot.set_greeting(botgreeting)



bot.add_command(
    "/capture dashboard", "Takes a screenshot from your Grafana dashboard to be returned", capturescreen
)


if __name__ == "__main__":
    # Run Bot
    bot.run(host="0.0.0.0", port=5000)
