import itertools
<<<<<<< HEAD
from PyQt5 import QtCore

class EmittingStream(QtCore.QObject):
=======
from pynput import keyboard # Monitoring
from pynput.keyboard import Key, Controller    # Controlling
import pyperclip #clipboard
from time import sleep #timer
>>>>>>> upstream/master

    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))

<<<<<<< HEAD
=======
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
        '⠽' : '13456' ,      #101111
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
>>>>>>> upstream/master

    def mappingToNumbers(n):
        return {
                'f': '1',
                'd': '2',
                's': '3',
                'j': '4',
                'k': '5',
                'l': '6',
                }[n]


<<<<<<< HEAD
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
=======
#set keyboard controller
keyboard_ctrl = Controller()
#init numKey,ctrl_pressed
numKey = ""
ctrl_pressed = False


#press function of the listener
#detect if control is pressed:
#   set ctrl_pressed to True
def on_press(key):
    global ctrl_pressed
    try:
        '{0}'.format(key.char)
        #print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        #print('special key {0} pressed'.format(key))
        if key==Key.ctrl_l:
            ctrl_pressed = True
>>>>>>> upstream/master

#release function of the listener
#detect if key is char/num or special
#if char/num and ctrl is not pressed
#       press,release backspace one time
#       set Numkey accordingly
#if release Ecs
#       end program
#if release ctrl 
#       set ctrl_pressed to False
#if release space
#       press,release backspace one time
#       save last clipboard
#       copy numKey's char to clipboard
#       paste clipboard and wait 0.2 sec
#       set clipboard back to it's vallue
def on_release(key):
    global numKey,ctrl_pressed
    try:
        '{0}'.format(key.char)
        #print('alphanumeric key {0} release'.format(key.char))
        if ctrl_pressed!=True:
            keyboard_ctrl.press(Key.backspace)
            keyboard_ctrl.release(Key.backspace)
            try:
                corrNumKey = mappingToNumbers(key.char)
                #print(corrNumKey)
                numKey = numKey + corrNumKey
                #print(numKey)
            except KeyError:
                pass
    except AttributeError:
        #print('special key {0} release'.format(key))
        if key == Key.esc:
            return False
        elif key == Key.ctrl_l:
            ctrl_pressed = False
        elif key == Key.space:
            keyboard_ctrl.press(Key.backspace)
            keyboard_ctrl.release(Key.backspace)
            old_clipboard= pyperclip.paste()
            numKey = ''.join(ch for ch, _ in itertools.groupby(sorted(numKey)))
            #print('numKey is',numKey,'char is',numToBraille[numKey])
            #print(numToBraille[numKey], end="", flush=True)
            #copy gen char
            pyperclip.copy(numToBraille[numKey])
            #paste the char
            with keyboard_ctrl.pressed(Key.ctrl_l):
                keyboard_ctrl.type('v')
            #wait some time for the cp perform
            sleep(0.2) # Time in seconds.
            #reset numkey and set clipboard back to it's vallue
            numKey = ""
            pyperclip.copy(old_clipboard)

<<<<<<< HEAD
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
=======
#set the listener
# Collect events until released
with keyboard.Listener(
        on_release=on_release,
        on_press=on_press) as listener:
    listener.join()
>>>>>>> upstream/master
