import getch

#prints out braille characters's correspondant ASCII code equivalents
string = "⠁⠂⠃⠄⠅⠆⠇⠈⠉⠊⠋⠌⠍⠎⠏⠐⠑⠒⠓⠔⠕⠖⠗⠘⠙⠚⠛⠜⠝⠞⠟⠠⠡⠢⠣⠤⠥⠦⠧⠨⠩⠪⠫⠬⠭⠮⠯⠰⠱⠲⠳⠴⠵⠶⠷⠸⠹⠺⠻⠼⠽⠾⠿"
for char in string:
  print(ord(char))
print("every keypress will return it's correspondant ASCII code\npress esc to exit")
while True:
    key = ord(getch.getch())
    print(key)
    if key == 27:
        break
