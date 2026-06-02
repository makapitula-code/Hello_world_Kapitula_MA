N = int(input("ВВЕДИТЕ N: "))
if N <= 0:
    print("Ошибка! N должно быть больше 0")
else:
    max_val = float(input("ВВЕДИТЕ ЧИСЛО : "))
    i = 2
    while i <= N:
        x = float(input("ВВЕДИТЕ ЧИСЛО: "))
        if x > max_val:
            max_val = x
        i = i + 1
    print(max_val)