# This script converts "..._no_numbers" files to their normal equivalents by adding the
# number codes. It makes it easier for the authors to add new instructions by inserting,
# and inserts character codes that cannot be typed

snn = open('setdocs_no_numbers.txt').read()

x = 0
while '$v' in snn:
    snn = snn.replace('$v', hex(x)[2:].zfill(2).upper(), 1).replace('$c', chr(x), 1)
    x += 1

open('setdocs.txt', 'w').write(snn)