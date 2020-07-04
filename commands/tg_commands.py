from dao import *
from commands.keyboards import *
from commands.admin_commands import ask_admin
from commands.plant_commands import plants_keyboard_handler
from commands.users_plants_commands import user_plants_keyboard_handler
from commands.notifications_commands import notifications_keyboard_handler
from telegram import Message


def start(bot, update):
    telegram_id = update.effective_message.chat_id

    if not does_user_exist(telegram_id=telegram_id):
        first_name = update.message.from_user.first_name
        last_name = update.message.from_user.last_name
        login = update.message.from_user.username
        add_user_by_telegram(telegram_id, first_name, last_name, login)
        update.message.reply_text(
            """Привет! Теперь ты можешь воспользоваться мной.
            Если тебе нужна полная информация по функциям бота, воспользуйся командой /info.
            Также ты можешь задать вопрос администратору с помощью команды /help.""")
    update.message.reply_text(
        "Выбери, что ты хочешь сделать.",
        reply_markup=create_reply_keyboard(MAIN_KEYBOARD)
        )


def main_keyboard_handler(bot, update):
    text = update.message.text

    if text == SEARCH:
        update.message.reply_text(
            "Выбери, что ты хочешь сделать.",
            reply_markup=create_reply_keyboard(PLANTS_KEYBOARD)
        )
        return plants_keyboard_handler(bot, update)
    elif text == MY_PLANTS:
        update.message.reply_text(
            "Выбери, что ты хочешь сделать.",
            reply_markup=create_reply_keyboard(USER_PLANTS_KEYBOARD)
        )
        return user_plants_keyboard_handler(bot, update)
    elif text == NOTIFICATIONS:
        update.message.reply_text(
            "Выбери, что ты хочешь сделать.",
            reply_markup=create_reply_keyboard(NOTIFICATIONS_KEYBOARD)
        )
        return notifications_keyboard_handler(bot, update)


def info(bot, update):
    bot.send_message(chat_id=update.message.chat_id, 
                    text="Чувак, подожди, помощи пока не жди.")


def help_me(bot, update):
    bot.send_message(chat_id=update.message.chat_id, 
                    text="""Хочешь задать вопрос администратору бота? 
                            Напиши его в следующем сообщении.""")
    ask_admin(bot, update)


def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                    text="Упс, я не понял команду. Попробуй еще.")