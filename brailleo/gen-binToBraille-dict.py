import itertools


bitToBraille = dict ()
s = ""
for bit in itertools.product('01', repeat=6):
    bitToBraille[str(bit)] = '1'
print(bitToBraille)
strToOutput = str(bitToBraille)
chck = eval(strToOutput)
print(strToOutput == chck)
with open("Bit-To-Braille.txt", "w") as text_file:
    print("dict: {}\n".format(strToOutput == chck), file=text_file)
