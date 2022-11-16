from telegram.ext import *
from telegram.bot import *
import responses as r
import config as c

print('Operating...')

def start_command(update, context):
    update.message.reply_text('Type something to get started')
    
def help_command(update, context):
    update.message.reply_text('Type something or not')
    
def handle_message(update, context):
    text = str(update.message.text).lower()
    response =r.sample_responses(text)
    
    update.message.reply_text(response)
    
def error(update,context):
    print(f'Update {error} caused error {context.error}')

def main():
    updater = Updater(c.TOKEN,use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    
    dp.add_handler(CommandHandler('error', error))
    updater.start_polling()
    updater.idle()
main()

    
    