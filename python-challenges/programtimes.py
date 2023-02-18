import datetime


def type_time():
  sentence = ""
  while sentence != "The lazy fox jumped over the brown dog":
    sentence = input("Type 'The lazy fox jumped over the brown dog':  ")

start_time = datetime.datetime.now()  # Starts the timer, by putting the time into start_time variable
type_time()  # Whatever you want to time
time_taken = datetime.datetime.now()-start_time  # Current time - start time
print(time_taken)  # Printing the time it took