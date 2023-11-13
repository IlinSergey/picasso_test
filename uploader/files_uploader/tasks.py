import asyncio

from files_uploader.models import File
from uploader.celery import app
from .services import process_file


@app.task
def start_process_file(file_id: int):
    '''Таска для фоновой обработки файла, после обработки ставит флаг в БД на True'''
    file_obj = File.objects.get(id=file_id)
    asyncio.run(process_file(file_id=file_id))
    file_obj.processed = True
    file_obj.save()
