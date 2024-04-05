import json
import urllib3
import asyncio
from aiohttp import ClientSession
import aiohttp

header_raw = """
!! PASTE YOUR HEADER HERE (COPY RAW HEADER FROM FIREFOX) !!
"""

headers = dict([line.split(": ", 1) for line in header_raw.strip().split("\n")])

# load links from data.json:
with open("data.json", "r") as f:
    jpg_links = json.load(f)

# parrallel download images:
jobs = []
total = len(set(jpg_links))
progress = 0

async def download_img(url, session):
    async with session.get(url, headers=headers, raise_for_status=True) as response:
        content = await response.read()
        with open(f"imgs/{url.split('/')[-1]}", "wb") as f:
            f.write(content)

        global progress
        progress += 1
        print(f"Progress: {progress}/{total}")

async def main():
    async with ClientSession() as session:
        for url in jpg_links:
            jobs.append(download_img(url, session))
        await asyncio.gather(*jobs)

asyncio.run(main())