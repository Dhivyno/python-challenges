dict = ['01','1000','1010','100','0','0010','110','0000','00','0111','101','0100','11','10','111','0110','1101','010','000','1','001','0001','011','1001','1011','1100','11111','01111','00111','00011','00001','00000','10000','11000','11100','11110']

text = list(str(input("Write your sentence, seperate your letters by 1 space and seperate your words by 2 spaces.   ")))
print(text)
for i in range(len(text)):
  for j in range(36):
    print(len(dict[j]))
    a = *text[0: len(dict[j])], sep = ""
    a = str(a)
    if a == dict[j]:
      print("yes")
