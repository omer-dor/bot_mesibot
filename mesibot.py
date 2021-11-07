""" 
Simple Telegram Bot to automate the process of obtaining Outline.com links. 
Created by Raivat Shah in 2019. 
"""
# Imports
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import time
# Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
from instagrapi import Client

def start(update, context):
    last_link = None
    cl = Client()
    cl.login("omerdor49", "49Omerdor49")
    while True:
        named_tuple = time.localtime() # get struct_time
        time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
        logging.warning(time_string)
        party_link = cl.user_info_by_username('ragerdizen').dict()["external_url"]
        logging.warning(party_link)
        if last_link != party_link and party_link!=None:
            context.bot.send_message(chat_id=-666138035, text=party_link)
            last_link = party_link
        time.sleep(360)
        context.bot.send_message(chat_id=-642766618, text="I'm Alive")
def read(update, context):
    pass

        
def main():


    # Create updater and pass in Bot's auth key. 
    updater = Updater(token='2082184762:AAGC-GSwCfe_s193DmleHmYCm5s6L_Q5K8U', use_context=True)
    # Get dispatcher to register handlers
    dispatcher = updater.dispatcher
    # answer commands
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('read', read))
    # start the bot
    updater.start_polling()
    # Stop
    updater.idle()

if __name__ == '__main__':
    main()

