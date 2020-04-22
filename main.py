'''Links for help:
https://github.com/python-telegram-bot/python-telegram-bot/blob/master/README.rst
'''
from priv import TOKEN

def main():
    from telegram.ext import Updater, CommandHandler
    import logging

    updater = Updater(token=TOKEN, 
                        use_context=True)
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    def start(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, 
                            text="Привет! Теперь ты можешь воспользоваться мной.")
    def helpme(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, 
                            text="Чувак, подожди, помощи пока не жди.")
        
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    helpme_handler = CommandHandler('help', helpme)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(helpme_handler)

    updater.start_polling()

if __name__ == '__main__':
    main()