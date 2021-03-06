from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import KeyboardButton, ReplyKeyboardMarkup
from telegram import CallbackQuery

SEARCH = 'Поиск'
MY_PLANTS = 'Мои растения'
NOTIFICATIONS = 'Уведомления'

SEARCH_PLANT = 'Найти растения'
PLANTS_LIST = 'Список моих растений'
NOTIF_LIST = 'Список уведомлений'

ADD = 'Добавить'
CHANGE = 'Изменить'
DELETE = 'Удалить'

BACK = "Назад"

MAIN_KEYBOARD = [
    [
        KeyboardButton(SEARCH),
        KeyboardButton(MY_PLANTS),
        KeyboardButton(NOTIFICATIONS)
    ]
]

PLANTS_KEYBOARD = [
    [
        KeyboardButton(SEARCH_PLANT),
        KeyboardButton(BACK)
    ]
]

USER_PLANTS_KEYBOARD = [
    [
        KeyboardButton(PLANTS_LIST),
        KeyboardButton(BACK)
    ],
    [
        KeyboardButton(ADD),
        KeyboardButton(CHANGE),
        KeyboardButton(DELETE)
    ]
]

NOTIFICATIONS_KEYBOARD = [
    [
        KeyboardButton(NOTIF_LIST),
        KeyboardButton(BACK)
    ],
    [
        KeyboardButton(ADD),
        KeyboardButton(CHANGE),
        KeyboardButton(DELETE)
    ]
]

NAME = 'name'
DESCRIPTION = 'description'
LIGHT = 'light'
TEMPERATURE = 'temperature'
WATERING = 'watering'
MOISTURE = 'moisture'
FERTILIZER = 'fertilizer'
TRANSFER = 'transfer'
MORE_INFO = 'more_info'
PHOTO_LINK = 'photo_link'

TITLES = {
    NAME: 'Название',
    DESCRIPTION: 'Описание',
    LIGHT: 'Освещение',
    TEMPERATURE: 'Температура',
    WATERING: 'Полив',
    MOISTURE: 'Влажность',
    FERTILIZER: 'Удобрения',
    TRANSFER: 'Пересадка',
    MORE_INFO: 'Подробнее',
    PHOTO_LINK: 'Ссылка на фото'
}


def create_reply_keyboard(keyboard: list):
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
    )


def plant_inline_keyboard():
    plant_buttons_list = [
        [
        InlineKeyboardButton(TITLES[LIGHT], callback_data=LIGHT),
        InlineKeyboardButton(TITLES[TEMPERATURE], callback_data=TEMPERATURE),
        ],
        [
        InlineKeyboardButton(TITLES[WATERING], callback_data=WATERING),
        InlineKeyboardButton(TITLES[MOISTURE], callback_data=MOISTURE)
        ],
        [
        InlineKeyboardButton(TITLES[FERTILIZER], callback_data=FERTILIZER),
        InlineKeyboardButton(TITLES[TRANSFER], callback_data=TRANSFER)
        ],
        [
        InlineKeyboardButton(TITLES[MORE_INFO], callback_data=MORE_INFO),
        ]
    ]
    return InlineKeyboardMarkup(plant_buttons_list)


def send_inline_item(bot, update, title, db_item):
    '''Sends new message with one plant item
    '''
    chat_id = update.effective_message.chat_id

    bot.send_message(
        chat_id=chat_id,
        text="*{0}*\n\n{1}".format(title, db_item),
        reply_markup=plant_inline_keyboard(),
        parse_mode='Markdown'
    )
    

def delete_inline_keyboard(update):
    '''Deletes inline keyboard from previous message
    '''
    query = update.callback_query
    current_text = update.effective_message.text

    query.edit_message_text(
            text=current_text,
            parse_mode='Markdown',
        )