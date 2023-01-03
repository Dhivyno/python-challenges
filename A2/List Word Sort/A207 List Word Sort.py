words = ['wendwas',
'incipientwas',
'natchwas',
'curiowas',
'klugewas',
'modicumwas',
'ornerywas',
'warblewas',
'peepwas',
'styxwas',
'vestigewas', 
'wealdwas',
'botchwas',
'squelchwas',
'withewas',
'epithetwas',
'littoralwas',
'paludalwas',
'berthwas',
'pabulumwas', 
'alluviumwas', 
'pelagicwas',
'insularwas',
'perfunctory',
'sashaywas']

words.sort()

with open("wordsort.txt", "w") as file:
  for i in range(len(words)):
    file.write(words[i] + "\n")
    
