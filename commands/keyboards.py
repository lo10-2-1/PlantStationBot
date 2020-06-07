from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import KeyboardButton, ReplyKeyboardMarkup
from telegram import CallbackQuery

MAIN_KEYBOARD = [
    [
        KeyboardButton('Поиск растений'),
        KeyboardButton('Мои растения'),
        KeyboardButton('Уведомления')
    ]
]

USER_KEYBOARD = [
    [
        KeyboardButton('Список растений')
    ],
    [
        KeyboardButton('Добавить'),
        KeyboardButton('Удалить')
    ]
]

NOTIFICATIONS_KEYBOARD = [
    [
        KeyboardButton('Список уведомлений')
    ],
    [
        KeyboardButton('Добавить'),
        KeyboardButton('Изменить'),
        KeyboardButton('Удалить')
    ]
]

LIGHT = 'light'
TEMPERATURE = 'temperature'
WATERING = 'watering'
MOISTURE = 'moisture'
FERTILIZER = 'fertilizer'
TRANSFER = 'transfer'
MORE_INFO = 'more_info'

TITLES = {
    LIGHT: 'Освещение',
    TEMPERATURE: 'Температура',
    WATERING: 'Полив',
    MOISTURE: 'Влажность',
    FERTILIZER: 'Удобрения',
    TRANSFER: 'Пересадка',
    MORE_INFO: 'Подробнее'
}


def create_reply_keyboard(keyboard: list):
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
    )


def plant_inline_keyboard(bot, chat_id):
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