from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup
from telegram import CallbackQuery


MAIN_KEYBOARD = ReplyKeyboardMarkup([['Поиск растений', 'Мои растения', 'Уведомления']], 
                                    resize_keyboard=True)


def create_keyboard():
    pass


def plant_inline_keyboard(bot, chat_id):
    plants_buttons_list = [
        [
        InlineKeyboardButton("Освещение", #callback_data=),
        InlineKeyboardButton("Температура", #callback_data=),
        ],
        [
        InlineKeyboardButton("Полив", #callback_data=),
        InlineKeyboardButton("Влажность", #callback_data=)
        ],
        [
        InlineKeyboardButton("Удобрения", #callback_data=),
        InlineKeyboardButton("Пересадка", #callback_data=)
        ],
        [
        InlineKeyboardButton("Больше информации", #callback_data=),
        ]
    ]
    return reply_markup = InlineKeyboardMarkup()
    # bot.send_message(chat_id=chat_id, text=, reply_markup=reply_markup)