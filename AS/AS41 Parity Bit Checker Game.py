import random
def quiz():
    while True:
      binary = ""
      counter = 0
      for i in range(8):
        binary += str(random.randint(0, 1))
      answer = input(f'Is {binary} an odd or even parity? ')
      for j in range(8):
        if binary[j] == "1":
          counter += 1
      if counter % 2 == 0:
        parity = "even"
      else:
        parity = "odd"
      if answer == parity:
          print('Correct!')
      else:
          print(f'Incorrect. {binary} is {parity}.')
quiz()
