timeline = input('Is it am or pm?  ')
time_hour = int(input('what hour is it?  '))
time_minute = int(input('what minute is it?  '))

if timeline in ["am", "AM"]:
  if time_hour == 12:
    print('it is midnight or 00:00')
  elif 0 < time_hour < 12:
    print('it is', time_hour,':',time_minute)
elif timeline in ["pm", "PM"]:
  if time_hour == 12:
    print('it is noon or 12:00')
  elif 0 < time_hour < 12:
    print(print('it is', time_hour + 12,':',time_minute))
