
"""
This code snippet shows you how you can directly access a list in Python.
Making it much easier to create a ticketing system.
In this example we choose the bus going out.
"""

#Lists used in this code
bus_time = ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00"]
bus_capacity = [40, 40, 40, 40, 40, 40, 40, 64]
bus_money = [0, 0, 0, 0, 0, 0, 0, 0]
charge=15

bus_choice = int(input("\nChoose your Bus. Please enter 09:00 [0], 10:00 [1], 11:00 [2], 12:00 [3], 13:00 [4], 14:00 [5],  15:00 [6] or 16:00 [7]: "))
# Generates an integer which we can then use to access the correct data.
print("Bus time chosen:",bus_time[bus_choice])

bus_capacity[bus_choice]= bus_capacity[bus_choice] - 1
bus_money[bus_choice] += charge
#Adjusts lists to take ticket away.

print("\nUpdated Lists")
print("Bus Times",bus_time)
print("Bus capacity", bus_capacity)
print("Bus money", bus_money)
# Printed to show you how the lists have changed.