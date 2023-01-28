from os import listdir
from os.path import isfile, join
import re

src_dir = r'D:\Anime\_subs\Candy-Candy\Eng'
dest_dir = r'C:\Home\Fansub\Candy-Candy\out'

fixes = {
'l' : 'I',
'lt' : 'It',
'lts' : 'Its',
'lf' : 'If',
'ln' : 'In',
'ls' : 'Is',
'lsn' : 'Isn',
'lgnition' : 'Ignition',
'lmmediately' : 'Immediately',
'lmpossible' : 'Impossible',
'lncredible' : 'Incredible',
'lnside' : 'Inside',
'lnstead' : 'Instead',
'lntroduce' : 'Introduce',
'lnvitation' : 'Invitation'
}

pat = re.compile(r'\b(l[a-z]*)\b')

def fix_typo(m):
    found = m.group(1)
    if found in fixes:
        return fixes[found]
    else:
        return found


file_names = [f for f in listdir(src_dir) if isfile(join(src_dir, f))]
for name in file_names:
    fixed_lines = []
    with open(join(src_dir, name), 'rt') as inf:
        for line in inf.readlines():
            # line = line.strip()
            if re.search(pat, line) is not None:
                line = re.sub(pat, fix_typo, line)
            fixed_lines.append(line)

    with open(join(dest_dir, name), 'wt') as outf:
        outf.writelines(fixed_lines)
