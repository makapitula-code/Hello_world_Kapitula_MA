from datetime import datetime
print("╔════════════════════════════════════════╗")
print("║        ЛОГГЕР ДАТЧИКА ДАВЛЕНИЯ         ║")
print("╚════════════════════════════════════════╝\n")
operator_name = input(" Введите имя оператора: ")
while True:
    try:
        pressure_value = float(input(" Введите текущее значение давления (Па): "))
        break
    except ValueError:
        print(" Ошибка: введите число (например, 101.3)")
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("sensor_log.txt", "a", encoding="utf-8") as file:
    file.seek(0)
    first_line = file.read(1)
    if not first_line:
        file.write("ДАТА И ВРЕМЯ\t\tОПЕРАТОР\tЗНАЧЕНИЕ (Па)\n")
        file.write("-" * 50 + "\n")
    file.write(f"{current_time}\t{operator_name}\t{pressure_value}\n")
print(f"\n Данные успешно сохранены в sensor_log.txt")
print("\n Последняя запись в логе:")
print("-" * 40)
with open("sensor_log.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    if len(lines) > 2:
        print(lines[-2].strip())  
        print(lines[-1].strip())  