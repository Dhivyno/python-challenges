import random
passphrase = ""
chars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "<", ">", "?", ":", ":", ",", ".", "/", ";", "{", "}", "[", "]", "-", "=", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "|"]

for i in range(18):
  passphrase += random.choice(chars)

print("Your generated password is", passphrase)
