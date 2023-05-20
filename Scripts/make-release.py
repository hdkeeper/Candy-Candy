# Создание zip-архива для архива Kage

from os import listdir
from os.path import isfile, join, realpath, dirname
import re
from zipfile import ZipFile, ZIP_DEFLATED, ZIP_LZMA

root_dir = realpath(join(dirname(__file__), '..'))
sub_dir = join(root_dir, '2-Russian')

file_names = [f for f in listdir(sub_dir) if isfile(join(sub_dir, f))]
episodes = list(map(lambda s: int(re.search(r'(\d+)', s)[1]), file_names))
zip_file_name = 'Candy-Candy TV %d-%d.zip' % (min(episodes), max(episodes))

with ZipFile(zip_file_name, 'w', compression=ZIP_LZMA, compresslevel=9) as zf:
    zf.write(join(root_dir, 'README.txt'), 'README.txt')
    for name in file_names:
        zf.write(join(sub_dir, name), name)
