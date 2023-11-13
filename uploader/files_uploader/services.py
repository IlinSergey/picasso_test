from asgiref.sync import sync_to_async
import asyncio
import mimetypes

import aiofiles

from files_uploader.models import File


def check_file_type(path_to_file: str) -> str | None:
    '''Проверяем тип файла для последующей, различной обработки(при необходимости)'''
    mime_type, encoding = mimetypes.guess_type(path_to_file)
    return mime_type


async def process_file(file_id: int) -> None:
    '''Имитируем обработку файла'''
    file_object = await sync_to_async(File.objects.get)(id=file_id)
    await sync_to_async(check_file_type)(file_object.file.path)
    try:
        async with aiofiles.open(file_object.file.path, mode='rb') as file:
            await asyncio.sleep(2)
    except FileNotFoundError:
        pass

