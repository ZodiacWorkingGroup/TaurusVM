import sys

def lexargs():
    args = ['']
    flags = []
    sm = False

    a = ' '.join(sys.argv[1:])

    x = 0
    while x < len(a):
        if a[x] == '"':
            sm = not sm

        elif a[x] == ' ' and not sm:
            args.append('')

        elif a[x] == '-' and args[-1] == '':
            if a[x+1] == '-':
                flag = ''
                x += 1
                while a[x] != ' ' and x < len(a)-1:
                    x += 1
                    flag += a[x]
                flags += flag
            else:
                while a[x] != ' ' and x < len(a)-1:
                    x += 1
                    flags += a[x]

        else:
            args[-1]+=a[x]

        x += 1

    return (args, flags)

if __name__ == '__main__':
    (args, flags) = lexargs()
    if any(x in flags for x in ['d', 'debog']):
        print(args)
        print(flags)
    c = open(sys.argv[1]).read()

    ids = c[:c.find(chr(0))]  # Identifier string
    prog = c[c.find(chr(0))+1:]

    en = ids.split(';')[0]  # Executer name
    ev = ids.split(';')[1]  # Executer version



    if any(x in flags for x in ['i', 'info', 'd', 'debug']):
        print('\nFile properties:')
        print('    Identifier String: ' + ids)
        print('    Executer Name: ' + en)
        print('    Executer Version: ' + ev)

    if en == 'Indeterminant':
        if ev == '0.5':
            from Executers.indeterminant.v05 import main
            Executers.indeterminant.v05.main(prog)