seq = ["ЧАОКАКАО", "ЧАО"]
# Вывод последовательностей целиком
print("Последовательности целиком:")
for s in seq:
    print(s)
print("\nПострочный вывод:")
# Построчный вывод (по символам)
for s in seq:
    for nucleotide in s:
        print(nucleotide)
print("\nЦикл выполнен")