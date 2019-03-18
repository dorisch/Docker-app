from quart import Quart 
import asyncio
import uuid
import re
from app import workers

app = Quart(__name__)

tasks = {}

@app.route('/api/download/text/<path:url>')
async def download_text(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if not re.match(regex, url):
        return 'URL is not valid'

    uid = uuid.uuid4().hex
    tasks[uid] = asyncio.create_task(workers.text_worker(url))
    return uid

@app.route('/api/download/images/<path:url>')
async def download_images(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if not re.match(regex, url):
        return 'URL is not valid'

    uid = uuid.uuid4().hex
    tasks[uid] = asyncio.create_task(workers.img_worker(url))
    return uid

@app.route('/api/status/<id>')
async def status(id):
    isFinished = tasks[id].done()
    if isFinished:
        return 'Results are ready'
    else:
        return 'Results are not ready yet'

@app.route('/api/result/<id>')
async def result(id):
    if id not in tasks:
        return 'There is no such task'

    if not tasks[id].done():
        return 'Task is not finished yet'
    
    return await tasks[id]

