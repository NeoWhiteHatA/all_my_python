#Шифр Цезаря
SYMBOLS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЪЭЮЯаивгдеёжзийклмнопрстуфхцчшщъьэюя 1234567890~!@#$%^&*()_+{}[]:;'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
    while True:
        print('Вы хотите зашифровать, расшифровать или ВЗЛОМАТЬ сообщение?')
        mode = input().lower()
        if mode in['зашифровать', 'з', 'расшифровать', 'р', 'взлом', 'в']:
            return mode
        else:
            print('Введите "зашифровать", "з" или "расшифровать", "р","взломать", "в"')

def getMessage():
    print('Введите текст:')
    return input()


def getKey():
    key = 0
    while True:
        print('Введите ключ шифрования(1 - %s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'р':
        key = -key
    translated = ''
    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1:
#символ не найден тогда добавить этот символ без изменений
            translated += symbol
        else:
            symbolIndex += key
            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)
            translated += SYMBOLS[symbolIndex]
    return translated
mode = getMode()
message = getMessage()
if mode[0] != 'в':
    key = getKey()
print('Преобразованный текст: ')

if mode[0] != 'в':
 print(getTranslatedMessage(mode, message, key))
else:
    for key in range(1, MAX_KEY_SIZE + 1):
        print(key, getTranslatedMessage('расшифровать', message, key))
