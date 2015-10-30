# This script converts "..._no_numbers" files to their normal equivalents by adding the
# number codes. It makes it easier for the authors to add new instructions by inserting,
# and inserts character codes that cannot be typed

import os.path


def curindex(fs):
    fs = hex(fs)
    if len(fs[2:]) == 1:
        return '0x0'+fs[2:]
    else:
        return fs

for filesuffix in range(256):
    if os.path.isfile('setdocs_'+curindex(filesuffix)+'_no_numbers.txt'):
        snn = open('setdocs_'+curindex(filesuffix)+'_no_numbers.txt').read()

        y = 0
        while '$v' in snn:
            while len(hex(y)[2:]) < 3:
                snn = snn.replace('$v', (hex(filesuffix)[2:].zfill(2)+hex(y)[2:].zfill(2)).upper(), 1).replace('$c', chr(filesuffix)+chr(y), 1)
                y += 1
            y = 0

        open('setdocs_'+curindex(filesuffix)+'.txt', 'w').write(snn)
