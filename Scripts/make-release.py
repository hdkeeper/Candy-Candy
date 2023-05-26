# Создание ZIP-архива с субтитрами для архива Kage

from os import listdir
from os.path import isfile, join, realpath, dirname
import re
from zipfile import ZipFile, ZIP_DEFLATED, ZIP_LZMA

root_dir = realpath(join(dirname(__file__), '..'))
sub_dir = join(root_dir, '2-Russian')

def get_ep(file_name: str):
    m = re.search(r'(\d+)', file_name)
    return None if m is None else int(m[1])

def zip_eps(episodes: list[int]) -> str:
    ints: list[list[int]] = []
    for n in episodes:
        if len(ints) == 0:
            ints.append([n])
            continue

        last = ints[-1]
        if last[-1] == n-1:
            if len(last) == 1:
                last.append(n)
            else:
                last[1] = n
        else:
            ints.append([n])

    return ','.join('-'.join(str(n) for n in i) for i in ints)


file_names = [f for f in listdir(sub_dir) if isfile(join(sub_dir, f))]
episodes = sorted([get_ep(f) for f in file_names if get_ep(f) is not None])
zip_file_name = 'Candy-Candy TV %s.zip' % zip_eps(episodes)

with ZipFile(zip_file_name, 'w', compression=ZIP_LZMA, compresslevel=9) as zf:
    zf.write(join(root_dir, 'README.txt'), 'README.txt')
    for name in file_names:
        zf.write(join(sub_dir, name), name)
