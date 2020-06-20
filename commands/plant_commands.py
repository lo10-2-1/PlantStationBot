from dao import does_plant_exist, get_plant_id_by_title, get_plant
from commands.keyboards import *
from commands.tg_commands import start
from telegram import Message


def plants_keyboard_handler(bot, update):
    chat_id = update.effective_message.chat_id
    text = update.message.text

    if text == SEARCH_PLANT:
        bot.send_message(
            chat_id=chat_id,
            text='Какое растение вы хотите найти?'
        )
        search_plant(bot, update)
    elif text == BACK:
        return start(bot, update)


def search_plant(bot, update):
    chat_id = update.effective_message.chat_id
    plant_title = update.message.text

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
    '''Shows plant description and photo
    '''
    chat_id = update.effective_message.chat_id

    bot.send_message(
        chat_id=chat_id,
        text='<b>{0}<b>\n\n{1}\n<a href="{2}">&#8288;</a>'.format(plant_obj.name, 
                                                                plant_obj.description,
                                                                plant_obj.photo),
        reply_markup=plant_inline_keyboard(),
        parse_mode='HTML'
        )


def plant_inline_keyboard_handler(bot, update, plant):
    '''All conditions work the same:
    1. Delete keyboard from previous message;
    2. Send message with the same keyboard.
    '''
    query = update.callback_query
    data = query.data
    
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