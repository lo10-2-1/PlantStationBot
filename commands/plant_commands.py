from telegram import Message
from dao import does_plant_exist, get_plant_id_by_title, get_plant
from commands.keyboards import *


def plants_keyboard_handler():
    pass


def search_plant(bot, update, plant_title):
    chat_id = update.effective_message.chat_id

    if not does_plant_exist(plant_title):
        return bot.send_message(
            chat_id=chat_id,
            text='Кажется, растения "{}" нет в нашей базе. А может, вы сделали опечатку?'.format(plant_title),
        )
    else:
        plant_id = get_plant_id_by_title(plant_title)
        plant = get_plant(plant_id)
        show_plant(bot, update, plant)


def show_plant(bot, update, plant_obj):
    chat_id = update.effective_message.chat_id

    bot.send_message(text='')


def plant_inline_keyboard_handler(bot, update, plant):
    query = update.callback_query
    data = query.data
    
    '''All conditions work the same:
    1. Delete keyboard from previous message;
    2. Send message with the same keyboard.
    '''
    if data == LIGHT:
        delete_inline_keyboard(update)
        send_inline_item(bot, update, TITLES[LIGHT], plant.light)
    elif data == TEMPERATURE:
        delete_inline_keyboard(update)
        send_inline_item(bot, update, TITLES[TEMPERATURE], plant.temperature)
    elif data == WATERING:
        delete_inline_keyboard(update)
        send_inline_item(bot, update, TITLES[WATERING], plant.watering)
    elif data == MOISTURE:
        delete_inline_keyboard(update)
        send_inline_item(bot, update, TITLES[MOISTURE], plant.moisture)
    elif data == FERTILIZER:
        delete_inline_keyboard(update)
        send_inline_item(bot, update, TITLES[FERTILIZER], plant.fertilizer)
    elif data == TRANSFER:
        delete_inline_keyboard(update)
        send_inline_item(bot, update, TITLES[TRANSFER], plant.transfer)
    elif data == MORE_INFO:
        delete_inline_keyboard(update)
        send_inline_item(bot, update, TITLES[MORE_INFO], plant.more_info)