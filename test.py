from ast import Delete
from telegram import *
from telegram.ext import *
import telegram.ext
import os
from scrapper import namebtc, pricebtc, nameeth, priceeth, priceltc, nameltc
from dotenv import load_dotenv
from requests import *

def bot(update: Update, context: CallbackContext) -> None:

    update.message.reply_text("Beginning of inline keyboard")

    keyboard = [[InlineKeyboardButton("Button 1", callback_data='1')],[InlineKeyboardButton("Button 2", callback_data='2')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Replying to text", reply_markup=reply_markup)