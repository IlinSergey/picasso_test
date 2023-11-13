from asgiref.sync import sync_to_async

import aiofiles
import asyncio

from files_uploader.models import File


async def process_file(file_id: int) -> None:
    '''Имитируем обработку файла'''
    file_object = await sync_to_async(File.objects.get)(id=file_id)
    try:
        async with aiofiles.open(file_object.file.path, mode='rb') as file:
            await asyncio.sleep(2)
    except FileNotFoundError:
        pass
