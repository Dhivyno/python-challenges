def crack(ciphertext):
  for i in range(26):
    plaintext = ""
    for j in range(len(ciphertext)):
      if ciphertext[j].isalpha():
        plaintext += chr((ord(ciphertext[j])-ord("a")+i)%26+ord("a"))
    print("Shift ", i, ":", plaintext)

crack("khoor")