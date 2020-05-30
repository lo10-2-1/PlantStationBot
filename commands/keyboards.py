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
    reply_markup = InlineKeyboardMarkup(build_menu(plants_buttons_list, n_cols=2))
    bot.send_message(chat_id=chat_id, text="What should I do with remind?🤔", reply_markup=reply_markup)


def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu