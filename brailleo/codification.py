import getch


def mappingToNumbers(n):
    return {
            'f': '1',
            'd': '2',
            's': '3',
            'j': '4',
            'k': '5',
            'l': '6',
            }[n]


shouldStop = False
while not shouldStop:
    stri = ""
    while True:
        key = getch.getch()
        if ord(key) == 32:
             break
        elif ord(key) == 27:
            shouldStop = True
            break
        try:
            corrNum = mappingToNumbers(key)
            print(corrNum)
            stri = stri + corrNum
        except KeyError:
            pass
    print(stri)

