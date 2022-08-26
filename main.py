import telegram.ext
token = "5391767465:AAF7WbcoMfVqdTwkntJBXdEr0fltr-8wfYU"

updater = telegram.ext.updater("5391767465:AAF7WbcoMfVqdTwkntJBXdEr0fltr-8wfYU", use_context = True)
dispatcher = updater.dispatcher

def start(update, context):
    update.message.reply_text("Hello to Simply Learn")

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
    update.message.reply_text("Under Development")

def dev(update, context):
    update.message.reply_text("https://github.com/DeKabilan")

dispatcher.add_handler(telegram.ext.COmmandHandler("start", start))
dispatcher.add_handler(telegram.ext.COmmandHandler("help", help))
dispatcher.add_handler(telegram.ext.COmmandHandler("run", run))
dispatcher.add_handler(telegram.ext.COmmandHandler("dev", dev))

updater.start_polling()
updater.idle()