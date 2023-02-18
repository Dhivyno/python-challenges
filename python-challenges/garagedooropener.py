current = "CLOSED"

input = ['click', 'cycle_complete', 'click', 'click', 'click', 'click', 'click', 'cycle_complete']

for i in range(len(input)):
    if input[i] == "click":
      print("BUTTON CLICKED")
      if current == "CLOSED":
        current = "OPENING"
      elif current == "CLOSING":
        current = "STOPPED_WHILE_CLOSING"
      elif current == "OPEN":
        current = "CLOSING"
      elif current == "OPENING":
        current = "STOPPED_WHILE_OPENING"
      elif current == "STOPPED_WHILE_CLOSING":
        current = "OPENING"
      elif current == "STOPPED_WHILE_OPENING":
        current = "CLOSING"
    if input[i] == "cycle_complete":
      print("CYCLE COMPLETE")
      if current == "CLOSING":
        current = "CLOSED"
      elif current == "OPENING":
        current = "OPEN"
    print("Door: ", current, "\n")
