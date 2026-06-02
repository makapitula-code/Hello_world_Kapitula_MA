print("=== Анализ последовательности ДНК ===\n")

dna = input("Введите последовательность ДНК: ")

# Приводим строку к верхнему регистру
dna = dna.upper()

print("\nПоследовательность в верхнем регистре:", dna)

# Подсчёт нуклеотидов
count_a = dna.count("A")
count_t = dna.count("T")
count_g = dna.count("G")
count_c = dna.count("C")

length = len(dna)

print("\nПодсчёт нуклеотидов:")
print("A:", count_a)
print("T:", count_t)
print("G:", count_g)
print("C:", count_c)

print(f"\nОбщая длина: {length} нуклеотидов.")

# Процентное содержание
if length > 0:
    print("\nПроцентное содержание:")
    print(f"A: {count_a / length * 100:.2f}%")
    print(f"T: {count_t / length * 100:.2f}%")
    print(f"G: {count_g / length * 100:.2f}%")
    print(f"C: {count_c / length * 100:.2f}%")
else:
    print("\nНевозможно вычислить проценты для пустой строки.")