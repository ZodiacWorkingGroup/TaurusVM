snn = open('setdocs_no_numbers.txt').read()

x = 0
y = 0
while '$v' in snn:
    while len(hex(y)[2:]) < 3:
        snn = snn.replace('$v', (hex(x)[2:].zfill(2)+hex(y)[2:].zfill(2)).upper(), 1).replace('$c', chr(x)+chr(y), 1)
        y += 1
    y = 0
    x += 1

open('setdocs.txt', 'w').write(snn)