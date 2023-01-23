from os import listdir
from os.path import isfile, join
import re

src_dir = r'C:\Home\Fansub\Candy-Candy\1-Typos-fixed'


file_names = [f for f in listdir(src_dir) if isfile(join(src_dir, f))]
found = set()
for name in file_names:
    with open(join(src_dir, name), 'rt') as inf:
        for line in inf.readlines():
            line = line.strip()
            m = re.search('^(l[a-z]*)', line)
            if m is not None:
                word = m.group(1)
                found.add(word)
                if word == 'll':
                    print(name)
                

for word in sorted(list(found)):
    print(word)



