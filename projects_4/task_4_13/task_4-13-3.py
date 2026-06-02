N = int(input("ВВЕДИТЕ N: "))
if N < 0:
    print("ОШИБКА N должно быть > 0")
else:
    fact = 1
    i = 1
    while i <= N:
        fact = fact * i
        i = i + 1
    print(fact)