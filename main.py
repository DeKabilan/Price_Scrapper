from telegram import *
from telegram.ext import *
import telegram.ext
import os
from scrapper import namebtc, pricebtc, nameeth, priceeth
from dotenv import load_dotenv
from requests import *

load_dotenv()
token = os.getenv('token')
updater = telegram.ext.Updater(token, use_context=True)
dispatcher = updater.dispatcher



def start(update, context):
        update.message.reply_text(
        """
         Welcome to Price_Checker BOT

Use /help tp know the list of commands

        """)

    


def help(update, context):
    update.message.reply_text(
        """
         /start -> Welcome
/help -> Help
/btc -> BTC Price
/eth ->ETH Price
/dev -> Directs to Developers Git Page

        """
    )

def btc(update, context):
    update.message.reply_text(namebtc)
    update.message.reply_text(pricebtc)

def eth(update, context):
    update.message.reply_text(nameeth)
    update.message.reply_text(priceeth)

def dev(update, context):
    update.message.reply_text("https://github.com/DeKabilan")


dispatcher.add_handler(telegram.ext.CommandHandler("start", start))
dispatcher.add_handler(telegram.ext.CommandHandler("help", help))
dispatcher.add_handler(telegram.ext.CommandHandler("btc", btc))
dispatcher.add_handler(telegram.ext.CommandHandler("eth", eth))
dispatcher.add_handler(telegram.ext.CommandHandler("dev", dev))

updater.start_polling()
updater.idle()
