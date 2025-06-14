import base64
from django.core.files.base import ContentFile


def base64_to_file(data: str, name: str) -> ContentFile:
    splitted = data.split(';base64,')
    if len(splitted) == 2:
        format, imgstr = splitted
        ext = format.split('/')[-1]
        name = name + '.' + ext
    else:
        imgstr = data


    return ContentFile(base64.b64decode(imgstr), name=name)

