#v^2 = u^2 + 2as

print("Physics calculator for v^2 = u^2 + 2as")
unknown = input("Which variable is unknown: v, u, a, or s?  ")

if unknown in ["v", "V"]:
    u = float(input("What is your initial velocity? "))
    a = float(input("What is your acceleration? "))
    s = float(input("What is the distance travelled? "))
    print("v =", (u**2 + 2 * a * s)**0.5)
elif unknown in ["u", "U"]:
    v = float(input("What is your final velocity? "))
    a = float(input("What is your acceleration? "))
    s = float(input("What is the distance travelled? "))
    print("u =", (v**2 - 2 * a * s)**0.5)
elif unknown in ["a", "A"]:
    v = float(input("What is your final velocity? "))
    u = float(input("What is your initial velocity? "))
    s = float(input("What is the distance travelled? "))
    print("a =", (v**2 - u**2) / (2 * s))
elif unknown in ["s", "S"]:
    v = float(input("What is your final velocity? "))
    a = float(input("What is your acceleration? "))
    u = float(input("What is the initial velocity? "))
    print("s =", (v**2 - u**2) / (2 * a))
