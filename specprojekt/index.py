i = 0
# While loopen repeteras för alltid
while i < 1:
    # a är första numret
    print("enter 1st number:")
    a = float(input())

    # x är räknesättet
    print("enter operation ( + - * / ^ ):")
    x = input()

    # b är andra numret
    print("2nd number:")
    b = float(input())

    r = float()

    # Beroende på vad x är så räknas resultatet, r, ut
    if x == "+":
        r = a + b

    if x == "-":
        r = a - b

    if x == "*":
        r = a * b

    if x == "/":
        r = a / b

    if x == "^":
        r = a**b

    # Efter r har beräknats skrivs det ut
    print(r)

    # Oanvänd input så att man kan se svaret innan loopen startar om
    c = input() 
