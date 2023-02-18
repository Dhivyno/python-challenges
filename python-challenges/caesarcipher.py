menu = int(input("type 1 if you want to encode and 2 if you want to decode: "))
letterdict = {
    "Z": 0,
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26
}
if menu == 1:
    key = int(input("What is your key?  "))
    encrypted = ""
    phrase = input("What is your phrase?  ")
    for i in range(len(phrase)):
        if phrase[i] == " ":
            encrypted += phrase[i]
        else:
            val = letterdict.get(str(phrase[i]))
            encrypted_val = (val + key) % 26
            letter = {j for j in letterdict if letterdict[j] == encrypted_val}
            encrypted += list(letter)[0]
    print(encrypted)

elif menu == 2:
    key = int(input("What is your key?  "))
    decrypted = ""
    phrase = input("What is your encrypted phrase?  ")
    for i in range(len(phrase)):
        if phrase[i] == " ":
            decrypted += phrase[i]
        else:
            val = letterdict.get(str(phrase[i]))
            decrypted_val = (val - key + 26) % 26
            letter = {j for j in letterdict if letterdict[j] == decrypted_val}
            decrypted += list(letter)[0]
    print(decrypted)
