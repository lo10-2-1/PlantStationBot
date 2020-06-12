from telegram import Message
from commands.keyboards import *
from dao import does_plant_exist, get_plant

def search_plant():
    pass


def show_plant():
    pass


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