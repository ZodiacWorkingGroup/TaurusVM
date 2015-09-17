import sys


def usage():
    print('Executes a file on the TaurusVM\n')
    print('\tUsage:\n')
    print('\t\ttaurus <path> [-d|--debug] [-i|--info] [-r|--regs] [-h|--help\n')
    print('\tFlags:\n\n\t\t-d or --debug: Enter debug mode (for debugging the executer)\n\t\t-i or --info: Print file info'
          'Prior to execution\n\t\t-r or --regs: Print out registries after execution\n\t\t-h or --help: Get help on '
          'how to run (which you\'ve clearly figured out)')

def lexargs():
    ar = ['']
    fl = []
    sm = False

    a = ' '.join(sys.argv[1:])

    x = 0
    while x < len(a):
        if a[x] == '"':
            sm = not sm

        elif a[x] == ' ' and not sm:
            ar.append('')

        elif a[x] == '-' and ar[-1] == '':
            if a[x+1] == '-':
                flag = ''
                x += 1
                while a[x] != ' ' and x < len(a)-1:
                    x += 1
                    flag += a[x]
                fl.append(flag)
            else:
                while a[x] != ' ' and x < len(a)-1:
                    x += 1
                    fl += a[x]

        else:
            ar[-1] += a[x]

        x += 1

    return ([x for x in ar if x], [x for x in fl if x])

if __name__ == '__main__':
    (args, flags) = lexargs()

    if any([x in flags for x in ['h', 'help']]):
        usage()
    if any(x in flags for x in ['d', 'debug']):
        print('args:\n    '+'\n    '.join(args))
        print('\n')
        print('flags:\n    '+'\n    '.join(flags))

    if len(args) < 1:
        if not any([x in flags for x in ['h', 'help']]):
            usage()
    else:
        c = open(args[0]).read()

        ids = c[:c.find(chr(0))]  # Identifier string
        prog = c[c.find(chr(0))+1:]

        en = ids.split(';')[0]  # Executer name
        ev = ids.split(';')[1]  # Executer version

        if any([x in flags for x in ['i', 'info', 'd', 'debug']]):
            print('\nFile properties:')
            print('    Identifier String: ' + ids)
            print('    Executer Name: ' + en)
            print('    Executer Version: ' + ev)

        if en == 'Indeterminant':
            if ev == '0.5':
                from Executers.indeterminant.v05 import main

        regout = main(prog)
        if any([x in flags for x in ['r', 'regs']]):
            print(regout)