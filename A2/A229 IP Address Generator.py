import random
ipv6 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
menu = int(input("Enter 1 if you want IPv4 and 2 if you want IPv6: "))
ask = int(input("How many ip addresses do you want? "))
sections = []


if menu == 1:
  for j in range(ask):
    sections = []
    for i in range(4):
      num = random.randint(1, 255)
      sections.append(str(num))
    ip = sections[0]+"."+sections[1]+"."+sections[2]+"."+sections[3]
    print(ip)
elif menu == 2:
  for k in range(ask):
    sections = []
    for i in range(8):
      ipv6sec = ""
      for j in range(4):
        num = random.choice(ipv6)
        ipv6sec += num
      sections.append(ipv6sec)
    ip = sections[0]+":"+sections[1]+":"+sections[2]+":"+sections[3]+":"+sections[4]+":"+sections[5]+":"+sections[6]+":"+sections[7]
    print(ip)
