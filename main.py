import telegram.ext
import os
from scrapper import name, price
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('token')
updater = telegram.ext.Updater(token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    update.message.reply_text("""Hello, Welcome to Price_Checker Bot
Use /help""")

def help(update, context):
    update.message.reply_text(
        """
         /start -> Welcome
/help -> Help
/run -> Runs the Program
/dev -> Directs to Developers Git Page

        """
    )

def run(update, context):
    update.message.reply_text(name)
    update.message.reply_text(price)

def dev(update, context):
    update.message.reply_text("https://github.com/DeKabilan")

dispatcher.add_handler(telegram.ext.CommandHandler("start", start))
dispatcher.add_handler(telegram.ext.CommandHandler("help", help))
dispatcher.add_handler(telegram.ext.CommandHandler("run", run))
dispatcher.add_handler(telegram.ext.CommandHandler("dev", dev))

updater.start_polling()
updater.idle()
