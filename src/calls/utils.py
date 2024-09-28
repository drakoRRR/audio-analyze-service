import os
import uuid

import requests
from urllib.parse import unquote


async def download_audio_file(audio_url: str) -> str:
    decoded_url = unquote(str(audio_url))

    file_extension = decoded_url.split('.')[-1]

    unique_filename = f"{uuid.uuid4()}.{file_extension}"

    response = requests.get(audio_url)

    with open(unique_filename, "wb") as file:
        file.write(response.content)

    return unique_filename


def delete_file(file_path: str):
    if os.path.exists(file_path):
        os.remove(file_path)

