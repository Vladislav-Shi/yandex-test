from aiogram import types

from bot.services.models import VoiceAction

main_keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(text='посмотреть фото'), types.KeyboardButton(text='посмотреть голосовое')],
        [types.KeyboardButton(text='посмотреть мое увлечение'), types.KeyboardButton(text='github')],
        [types.KeyboardButton(text='Вызвать меню')],
    ]
)

main_keyboard_inline = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(text='посмотреть фото', callback_data='photos'),
            types.InlineKeyboardButton(text='посмотреть голосовое', callback_data='voices_list')
        ],
        [
            types.InlineKeyboardButton(text='посмотреть мое увлечение', callback_data='story'),
            types.InlineKeyboardButton(text='github', callback_data='github')
        ],
    ]
)

voice_message_keyboard_inline = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text='что такое GPT', callback_data=VoiceAction(voice_id=1).pack())],
        [types.InlineKeyboardButton(text='SQL и NoSQL', callback_data=VoiceAction(voice_id=2).pack())],
        [types.InlineKeyboardButton(text='история первой любви', callback_data=VoiceAction(voice_id=3).pack())],
    ]
)
