ls = {'A': '.-', 'B': '-...','C': '-.-.', 'D': '-..', 'E': '.',
                       'F': '..-.', 'G': '--.', 'H': '....',
                       'I': '..', 'J': '.---', 'K': '-.-',
                       'L': '.-..', 'M': '--', 'N': '-.',
                       'O': '---', 'P': '.--.', 'Q': '--.-',
                       'R': '.-.', 'S': '...', 'T': '-',
                       'U': '..-', 'V': '...-', 'W': '.--',
                       'X': '-..-', 'Y': '-.--', 'Z': '--..',
                       '1': '.----', '2': '..---', '3': '...--',
                       '4': '....-', '5': '.....', '6': '-....',
                       '7': '--...', '8': '---..', '9': '----.',
                       '0': '-----', ', ': '--..--', '.': '.-.-.-',
                       '?': '..--..', '/': '-..-.', '-': '-....-',
                       '(': '-.--.', ')': '-.--.-'}

def encrypt(x): #szöveget morse kóddá alakítás
    inmorse = ''
    for i in x:
        if i != ' ':
            inmorse += ls[i] + ' '
        else:
            inmorse += '\t'
    return inmorse

def decrypt(x): #morse kód szöveggé
    regular = ''
    text = ''
    for j in x.replace('\t', ' '): #j = betű
        if (j != ' '):
            space_in_between = 0
            text += j
        else:
            space_in_between += 1
            if space_in_between == 2:
                regular += ' '
            else:
                regular += list(ls.keys())[list(ls.values()).index(text)]
                text = ''
    return regular

x = input("Message: ")
for i in x.upper():
    if ("a" <= i <= "z") is True or ("A" <= i <= "Z") is True: #ha betű akkor morse koddá alakítja a szöveget
        morse = encrypt(x.upper())
        print("Original Message in Morse:", morse)
        break
    else:  #ha morse kód akkor meg szöveggé
        text = decrypt(x)
        print("Original Message in Regular:",text)
        break