from pathlib import PosixPath
from typing import Union, List

from aiogram.types import InputFile, InputMediaPhoto, FSInputFile


def from_path_to_tg_media(files_path: Union[str, PosixPath, List[str]]) -> Union[InputFile, List[InputMediaPhoto]]:
    """Приводит путь до фото к нужному для отправки телеграму
    Если передан пустой список или None то вызовет исключение!
    """
    if isinstance(files_path, (str, PosixPath)):
        return FSInputFile(files_path)
    if len(files_path) == 1:
        return FSInputFile(files_path[0])
    if 1 < len(files_path) <= 10:
        input_files = []
        for file in files_path:
            input_files.append(InputMediaPhoto(media=FSInputFile(file)))
        return input_files
    raise ValueError(f'Неверная длина списка файлов [1, 10] (у вас {len(files_path)}) либо другая ошибка')
