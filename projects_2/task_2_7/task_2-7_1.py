array = ["seq1", "seq2", "seq3", "seq4"]
date = "2024-01-01"  
# фиксированная дата
for name in array:
    new_name = name + "_" + date + ".fasta"
    print(new_name)
