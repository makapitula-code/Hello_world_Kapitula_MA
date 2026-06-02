files = ["seq1", "seq2.fasta", "seq3.fa", "seq4", "sample1.fasta", "sample2.txt"]
sample_date = "2025-02-24"
print("=" * 60)
print("ОБРАБОТКА ФАЙЛОВ С ПОСЛЕДОВАТЕЛЬНОСТЯМИ")
print("=" * 60)
print(f"Дата взятия образцов: {sample_date}")
print("-" * 60)
print("Исходные файлы:")
for name in files:
    print(f"  • {name}")
print("-" * 60)
print("\nРезультаты обработки:\n")
already_fasta = 0
need_rename = 0
other_ext = 0
for i, name in enumerate(files, 1):
    if name.endswith((".fasta", ".fa")):
        print(f"  {i:2d}. {name:20} ✅ уже имеет расширение FASTА")
        already_fasta += 1
    elif name.endswith(".txt"):
        print(f"  {i:2d}. {name:20} ⚠️ имеет другое расширение (не обрабатываем)")
        other_ext += 1
    else:
        new_name = f"{name}_{sample_date}.fasta"
        print(f"  {i:2d}. {name:20} ➡️ {new_name}")
        need_rename += 1
print("\n" + "-" * 60)
print("СТАТИСТИКА ОБРАБОТКИ:")
print(f"  • Уже в формате FASTА: {already_fasta}")
print(f"  • Требуют переименования: {need_rename}")
print(f"  • Другие форматы: {other_ext}")
print("=" * 60)