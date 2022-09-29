translation = ''
array1 = ['.- ', '-... ', '-.-. ', '-.. ', '. ', '..-. ', '--. ', '.... ', '.. ', '.--- ', '-.- ', '.-.. ', '-- ', '-. ', '--- ', '.--. ', '--.- ', '.-. ', '... ', '- ', '..- ', '...- ', '.-- ', '-..- ', '-.-- ', '--.. ']
array2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


sentence = str(input("What do you want to translate into morse code: "))
for i in range(len(sentence)):
  if sentence[i] == " ":
    translation += "/"
  for j in range(26):
    if array2[j] == sentence[i]:
      translation += array1[j]
print(translation)
