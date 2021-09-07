from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


updater = Updater(token = 'API_KEY', use_context = True) #Use the api key given from BotFather
dispatcher = updater.dispatcher


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
    print(context.args)
    context.bot.sendMessage(chat_id = update.effective_chat.id, text = "Mindandiri Koothi")


startHandler = CommandHandler('start', start)
echoHandler = MessageHandler(Filters.text & (~Filters.command), echo)
pooreHandler = CommandHandler('poore', poore)
dispatcher.add_handler(startHandler)
dispatcher.add_handler(echoHandler)
dispatcher.add_handler(pooreHandler)
updater.start_polling()
updater.idle()
