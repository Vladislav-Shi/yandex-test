from aiogram.filters.callback_data import CallbackData


class VoiceAction(CallbackData, prefix="g_voice"):
    voice_id: int
