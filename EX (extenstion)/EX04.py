translation = ''
counter = 0
counter2 = 0
array = {"a":'.- ', "b":'-... ', "c":'-.-. ', "d":'-.. ', "e":'. ', "f":'..-. ', "g":'--. ', "h":'.... ', "i":'.. ', "j":'.--- ', "k":'-.- ', "l":'.-.. ', "m":'-- ', "n":'-. ', "o":'--- ', "p":'.--. ', "q":'--.- ', "r":'.-. ', "s":'... ', "t":'- ', "u":'..- ', "v":'...- ', "w":'.-- ', "x":'-..- ', "y":'-.-- ', "z":'--.. '}
holding = [""]
spaceVariable = 0

menu = int(input("Type 1 if you want text to morse code and 2 if you want morse code to text: "))

if menu == 1:
  sentence = str(input("What do you want to translate into morse code: "))
  for i in range(len(sentence)):
    if sentence[i] == " ":
      translation += "/ "
    else: 
      translation += array[sentence[i]]
  

if menu == 2:
  sentence = str(input("What do you want to translate from morse code: "))
  sentence += " "
  for i in range(len(sentence)):
    holding[spaceVariable] += sentence[i]
    if sentence[i] == " ":
      spaceVariable += 1 
      holding.append("")
  for i in range(len(holding)):
    for key in array:
      if holding[i] == array[key]:
        translation += key
      elif holding[i] == "/ ":
        translation += " "
      
print(translation)
