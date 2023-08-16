from typing import Union

from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery

from bot.config.settings import BASE_DIR
from bot.endpoints.keyboards import main_keyboard, main_keyboard_inline, voice_message_keyboard_inline
from bot.endpoints.text import story_text, voice_menu_text, github_text
from bot.services.files import from_path_to_tg_media
from bot.services.models import VoiceAction

router = Router()


async def get_my_photo(message: Union[Message, CallbackQuery]):
    """Отправляет 2 фото пользователю"""
    photos = from_path_to_tg_media(
        files_path=[
            BASE_DIR / 'media/photo1.jpg',
            BASE_DIR / 'media/photo2.jpg',
        ]
    )
    if isinstance(message, Message):
        await message.answer_media_group(media=photos)
    if isinstance(message, CallbackQuery):
        await message.message.answer_media_group(media=photos)


async def get_my_story(message: Union[Message, CallbackQuery]):
    if isinstance(message, Message):
        await message.answer(story_text)
    if isinstance(message, CallbackQuery):
        await message.message.answer(story_text)


async def get_my_voices(message: Union[Message, CallbackQuery]):
    if isinstance(message, Message):
        await message.answer(voice_menu_text, reply_markup=voice_message_keyboard_inline)
    if isinstance(message, CallbackQuery):
        await message.message.answer(voice_menu_text, reply_markup=voice_message_keyboard_inline)


async def get_github_url(message: Union[Message, CallbackQuery]):
    if isinstance(message, Message):
        await message.answer(github_text)
    if isinstance(message, CallbackQuery):
        await message.message.answer(github_text)


@router.message(F.voice)
async def set_voice(message: Message, bot: Bot):
    print('voice recording')
    await bot.download(message.voice, destination=f'bot/media/{message.voice.file_id}.ogg')


# Дабы не дублировать код зарегистрируем так
router.message.register(get_my_photo, F.text == 'посмотреть фото')
router.callback_query.register(get_my_photo, F.data == 'photos')

router.message.register(get_my_story, F.text == 'посмотреть мое увлечение')
router.callback_query.register(get_my_story, F.data == 'story')

router.message.register(get_my_voices, F.text == 'посмотреть голосовое')
router.callback_query.register(get_my_voices, F.data == 'voices_list')

router.message.register(get_github_url, F.text == 'github')
router.callback_query.register(get_github_url, F.data == 'github')


@router.message(F.text == 'Вызвать меню')
async def inline_menu_answer(message: Message):
    await message.answer('Вот inline клавиатура', reply_markup=main_keyboard_inline)


@router.callback_query(VoiceAction.filter())
async def get_voice(callback: CallbackQuery, callback_data: VoiceAction, bot: Bot):
    print('run_voice', callback_data.voice_id)
    files_path = ''
    if callback_data.voice_id == 1:
        files_path = BASE_DIR / 'media/gpt_voice.ogg'
    if callback_data.voice_id == 2:
        files_path = BASE_DIR / 'media/sql.ogg'
    if callback_data.voice_id == 3:
        files_path = BASE_DIR / 'media/lovestory.ogg'
    voice = from_path_to_tg_media(files_path)
    await callback.message.answer_voice(voice=voice)


@router.message(F.text)
async def hello_world(message: Message):
    await message.answer(f'Hello {message.from_user.username}!', reply_markup=main_keyboard)
