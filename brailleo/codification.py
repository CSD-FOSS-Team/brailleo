import getch
import itertools
from PyQt5 import QtCore

class EmittingStream(QtCore.QObject):

    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))


    def mappingToNumbers(n):
        return {
                'f': '1',
                'd': '2',
                's': '3',
                'j': '4',
                'k': '5',
                'l': '6',
                }[n]


    brailleToNum = dict ({
                        ' ' : ''      ,      #000000
                        '⠠' : '6'     ,      #000001
                        '⠐' : '5'     ,      #000010
                        '⠰' : '56'    ,      #000011
                        '⠈' : '4'     ,      #000100
                        '⠨' : '46'    ,      #000101
                        '⠘' : '45'    ,      #000110
                        '⠸' : '456'   ,      #000111
                        '⠄' : '3'     ,      #001000
                        '⠤' : '36'    ,      #001001
                        '⠔' : '35'    ,      #001010
                        '⠴' : '356'   ,      #001011
                        '⠌' : '34'    ,      #001100
                        '⠬' : '346'   ,      #001101
                        '⠜' : '345'   ,      #001110
                        '⠼' : '3456'  ,      #001111
                        '⠂' : '2'     ,      #010000
                        '⠢' : '26'    ,      #010001
                        '⠒' : '25'    ,      #010010
                        '⠲' : '256'   ,      #010011
                        '⠊' : '24'    ,      #010100
                        '⠪' : '246'   ,      #010101
                        '⠚' : '245'   ,      #010110
                        '⠺' : '2456'  ,      #010111
                        '⠆' : '23'    ,      #011000
                        '⠦' : '236'   ,      #011001
                        '⠖' : '235'   ,      #011010
                        '⠶' : '2356'  ,      #011011
                        '⠎' : '234'   ,      #011100
                        '⠮' : '2346'  ,      #011101
                        '⠞' : '2345'  ,      #011110
                        '⠾' : '23456' ,      #011111
                        '⠁' : '1'     ,      #100000
                        '⠡' : '16'    ,      #100001
                        '⠑' : '15'    ,      #100010
                        '⠱' : '156'   ,      #100011
                        '⠉' : '14'    ,      #100100
                        '⠩' : '146'   ,      #100101
                        '⠙' : '145'   ,      #100110
                        '⠹' : '1456'  ,      #100111
                        '⠅' : '13'    ,      #101000
                        '⠥' : '136'   ,      #101001
                        '⠕' : '135'   ,      #101010
                        '⠵' : '1356'  ,      #101011
                        '⠍' : '134'   ,      #101100
                        '⠭' : '1346'  ,      #101101
                        '⠝' : '1345'  ,      #101110
                        '⠽' : '13465' ,      #101111
                        '⠃' : '12'    ,      #110000
                        '⠣' : '126'   ,      #110001
                        '⠓' : '125'   ,      #110010
                        '⠳' : '1256'  ,      #110011
                        '⠋' : '124'   ,      #110100
                        '⠫' : '1246'  ,      #110101
                        '⠛' : '1245'  ,      #110110
                        '⠻' : '12456' ,      #110111
                        '⠇' : '123'   ,      #111000
                        '⠧' : '1236'  ,      #111001
                        '⠗' : '1235'  ,      #111010
                        '⠷' : '12356' ,      #111011
                        '⠏' : '1234'  ,      #111100
                        '⠯' : '12346' ,      #111101
                        '⠟' : '12345' ,      #111110
                        '⠿' : '123456',      #111111
                        })


    numToBraille = dict ((v,k) for k,v in brailleToNum.items())


    shouldStop = False
    while not shouldStop:
        numKey = ""
        while True:
            key = getch.getch()
            if ord(key) == 32:            #space key
                break
            elif ord(key) == 27:          #esc   key
                shouldStop = True
                print("\n")
                break
            elif ord(key) == 10:          #enter key
                print("\n", end = "", flush=True)
                break
            elif ord(key) == 9:           #tab   key
                print("\t", end = "", flush=True)
                break
            try:
                corrNumKey = mappingToNumbers(key)
                #print(corrNumKey)
                numKey = numKey + corrNumKey
            except KeyError:
                pass
        '''
        removes duplicate characters in numKey after sorting it
        '''
    numKey = ''.join(ch for ch, _ in itertools.groupby(sorted(numKey)))
    print(numToBraille[numKey], end="", flush=True)
