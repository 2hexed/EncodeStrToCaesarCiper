import os
from sys import platform
def EncodeCaesarCiper(string: str, shift: int):
    if platform == "linux" or platform == "linux2":
        os.system('clear')
    elif platform == "win32":
        os.system('title Encoding Caesar Ciper Text.')
        os.system('color 0a')
        os.system('cls')
    dict1: dict = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O', 15:'P', 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21:'V', 22:'W', 23:'X', 24:'Y', 25:'Z'}
    dict2: dict = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}
    string=string.upper()
    empty_lst=[]
    main_lst=[]
    for alphabet in string:
        empty_lst.append(dict2.get(f'{alphabet}'))
    for num in empty_lst:
        main_lst.append(dict1.get(num+shift))
    ciper_text=(''.join(i for i in main_lst))
    print('Your given string: ', string, '\nConverted Caesar Ciper Text: ', ciper_text)
