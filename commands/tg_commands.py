from commands.keyboards import *
from dao import *


def start(bot, update, telegram_id):
    if not does_telegram_id_exist(telegram_id):
        first_name = update.message.from_user.first_name
        last_name = update.message.from_user.last_name
        login = update.message.from_user.username
        add_user_by_telegram(telegram_id, first_name, last_name, login)
        update.message.reply_text(
            """Привет! Теперь ты можешь воспользоваться мной.
            Если тебе нужна полная информация по функциям бота, воспользуйся командой /info.
            Также ты можешь задать вопрос администратору с помощью команды /help.""")
    update.message.reply_text(
        "Выбери, что ты хочешь сделать.", reply_markup=MAIN_KEYBOARD)


def info(bot, update):
    bot.send_message(chat_id=update.message.chat_id, 
                            text="Чувак, подожди, помощи пока не жди.")


def help(bot, update):
    bot.send_message(chat_id=update.message.chat_id, 
                            text="""Хочешь задать вопрос администратору бота? 
                            Напиши его в следующем сообщении.""")


def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                            text="Упс, я не понял команду. Попробуй еще.")