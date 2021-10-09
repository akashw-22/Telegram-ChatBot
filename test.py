from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import random
import os
import psycopg2

TOKEN = os.environ['API_KEY']
PORT = os.environ.get('PORT')
URL = os.environ['URL']
DATABASE = "postgres://tfljkvwj:IbnOgi6XgAbgYF6LlO1Hdd9JzJYlwzvt@john.db.elephantsql.com/tfljkvwj"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

updater = Updater(token = TOKEN, use_context = True) #Use the api key given from BotFather
dispatcher = updater.dispatcher

theri = ["andi", "punda", "koothi", "myran", "shuklam", "beejam", "poori", "kakkos", "pundachi", "punda", "shuklamtheeni", "Kannappi", "thayli", "ശുക്ലമുഖൻ പുണ്ഡചി", "പപ്പടം പൂറി പുണ്ടച്ചി", "വ്യാകൻസിഎജെ പൂറിമോനെ", "വ്യാകൻസിഎജെ പൂറിമോനെ", "ചിണ്ടമൈരൻ കത്രിക്കകുണ്ണ", "വവ്വാൽ കുണ്ണ തയൊളി"]


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

def theri(update, context):

    reply = ''

    if(len(context.args) == 0):
        reply = "nthelum konachatt po kunne"

    else:
        theristr = ''

        for i in context.args:
            theristr += i

        theris = theristr.split(',')

        for theri in theris:
            conn = psycopg2.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute('insert into (theri) values (%s)', (theri,))
            reply += cursor.fetchall()

        reply = 'theri poottikkettind'

    print(reply)
    context.bot.sendMessage(chat_id = update.effective_chat.id, text = reply)

startHandler = CommandHandler('start', start)
echoHandler = MessageHandler(Filters.text & (~Filters.command), echo)
pooreHandler = CommandHandler('poore', poore)
theriHandler = CommandHandler('theri', theri)
dispatcher.add_handler(startHandler)
dispatcher.add_handler(echoHandler)
dispatcher.add_handler(pooreHandler)
dispatcher.add_handler(theriHandler)
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN,
                      webhook_url= URL + TOKEN)
updater.idle()
