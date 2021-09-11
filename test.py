from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import random
import os
from boto.s3.connection import S3Connection

TOKEN = os.environ['API_KEY']
PORT = int(os.environ.get('PORT', '8443'))
URL = os.environ['URL']

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

updater = Updater(token = TOKEN, use_context = True) #Use the api key given from BotFather
dispatcher = updater.dispatcher

theri = ["andi", "punda", "koothi", "myran", "shuklam", "beejam", "poori", "kakkos", "pundachi", "punda", "shuklamtheeni", "Kannappi", "thayli"]


def start(update, context):
    context.bot.sendMessage(chat_id = update.effective_chat.id, text = "Oombikko myre Ente andi oomban vannathaana??")

def poore(update, context):
    if(len(context.args) == 0):
        message = 'Nintappan'
    else:
        user = context.args[0].lower()
        message = ''

        if user != 'akash':
            message = user + ' punda'
        else:
            message = user + ' killedi'

    context.bot.sendMessage(chat_id = update.effective_chat.id, text = message)

def echo(update, context):
    msg = update.message.text.lower()
    words = msg.split()
    out = ''

    #print(msg)

    if words[0] == 'poorimon':
        if len(words) == 1:
            out = 'pooran nintappan'
        else:
            out = words[1] + ' ' + random.choice(theri)
    else:
        return

    context.bot.sendMessage(chat_id = update.effective_chat.id, text = out)


startHandler = CommandHandler('start', start)
echoHandler = MessageHandler(Filters.text & (~Filters.command), echo)
pooreHandler = CommandHandler('poore', poore)
dispatcher.add_handler(startHandler)
dispatcher.add_handler(echoHandler)
dispatcher.add_handler(pooreHandler)
updater.start_polling()
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN,
                      webhook_url= URL + TOKEN)
updater.idle()
