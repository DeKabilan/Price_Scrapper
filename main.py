from ast import Delete
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
switcheth="switcheth"
switchbtc="switchbtc"




def start(update, context):
    #INLINE FOR SWITCH
     update.message.reply_text(
        """
         Welcome to Price_Checker BOT

Use /help tp know the list of commands

        """)

        #INLINE FOR SWITCH
     buttons = [[InlineKeyboardButton("ETH", callback_data=switcheth)], [InlineKeyboardButton("BTC", callback_data=switchbtc)]]
     context.bot.send_message(chat_id=update.effective_chat.id, reply_markup= InlineKeyboardMarkup(buttons), text = "What do you want to Switch to?")


    


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

def btc(update: Update, context: CallbackContext):
     buttons1 = [[KeyboardButton(namebtc)], [KeyboardButton(pricebtc)]]
     context.bot.send_message(chat_id=update.effective_chat.id,text="BTC PRICE",
     reply_markup=ReplyKeyboardMarkup(buttons1))

    #  #INLINE FOR SWITCH
     buttons = [[InlineKeyboardButton("ETH", callback_data=switcheth)], [InlineKeyboardButton("BTC", callback_data=switchbtc)]]
     context.bot.send_message(chat_id=update.effective_chat.id, reply_markup= InlineKeyboardMarkup(buttons), text = "What do you want to Switch to?")

def eth(update: Update, context: CallbackContext):
     buttons1 = [[KeyboardButton(nameeth)], [KeyboardButton(priceeth)]]
     context.bot.send_message(chat_id=update.effective_chat.id,text="ETH PRICE",
     reply_markup=ReplyKeyboardMarkup(buttons1))

    #  #INLINE FOR SWITCH
     buttons = [[InlineKeyboardButton("ETH", callback_data=switcheth)], [InlineKeyboardButton("BTC", callback_data=switchbtc)]]
     context.bot.send_message(chat_id=update.effective_chat.id, reply_markup= InlineKeyboardMarkup(buttons), text = "What do you want to Switch to?")

        

def dev(update, context):
    update.message.reply_text("https://github.com/DeKabilan")

#QUERY_Handler
def queryHandler(update: Update, context = CallbackContext):
    query = update.callback_query.data
    update.callback_query.answer()
    global switcheth, switchbtc

    if switcheth in query:
        buttons1 = [[KeyboardButton(nameeth)], [KeyboardButton(priceeth)]]
        context.bot.send_message(chat_id=update.effective_chat.id,text="ETH PRICE",
     reply_markup=ReplyKeyboardMarkup(buttons1))
        
        
    if switchbtc in query:
        buttons1 = [[KeyboardButton(namebtc)], [KeyboardButton(pricebtc)]]
        context.bot.send_message(chat_id=update.effective_chat.id,text="BTC PRICE",
     reply_markup=ReplyKeyboardMarkup(buttons1))
        
        



dispatcher.add_handler(CallbackQueryHandler(queryHandler))
dispatcher.add_handler(telegram.ext.CommandHandler("start", start))
dispatcher.add_handler(telegram.ext.CommandHandler("help", help))
dispatcher.add_handler(telegram.ext.CommandHandler("dev", dev))
dispatcher.add_handler(telegram.ext.CommandHandler("btc", btc))
dispatcher.add_handler(telegram.ext.CommandHandler("eth", eth))


updater.start_polling()
updater.idle()
