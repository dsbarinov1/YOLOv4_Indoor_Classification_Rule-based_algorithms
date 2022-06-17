import os

path = '.'

rez = sorted(os.listdir(path))
for n, item in enumerate(rez):
    print(n+1, item)

import os

ext = "jpg"
i = 1
dir = '.'
for file in os.listdir(dir):
    if file.endswith(ext):
        os.rename(f'{dir}/{file}', f'{dir}/{i}.{ext}')
        i = i + 1