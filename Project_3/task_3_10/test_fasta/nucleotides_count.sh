#!/bin/bash

echo "========================================="
echo "ПОДСЧЁТ НУКЛЕОТИДОВ В FASTA-ФАЙЛАХ"
echo "========================================="
echo ""

echo "Файл                      A       T       G       C"
echo "--------------------------------------------------------"


for file in *.fasta; do

    if [ ! -f "$file" ]; then
        continue
    fi
    
  
    if [ ! -s "$file" ]; then
        echo "Пропуск пустого файла: $file"
        continue
    fi
    

    SEQUENCE=$(grep -v "^>" "$file" | tr -d '\n')
    
   
    A_COUNT=$(echo "$SEQUENCE" | grep -o "A" | wc -l | xargs)
    T_COUNT=$(echo "$SEQUENCE" | grep -o "T" | wc -l | xargs)
    G_COUNT=$(echo "$SEQUENCE" | grep -o "G" | wc -l | xargs)
    C_COUNT=$(echo "$SEQUENCE" | grep -o "C" | wc -l | xargs)
    
    if [ -z "$A_COUNT" ]; then A_COUNT=0; fi
    if [ -z "$T_COUNT" ]; then T_COUNT=0; fi
    if [ -z "$G_COUNT" ]; then G_COUNT=0; fi
    if [ -z "$C_COUNT" ]; then C_COUNT=0; fi
    
 
    echo "$file                  $A_COUNT    $T_COUNT    $G_COUNT    $C_COUNT"
done

echo ""
echo "Подсчётик завершён"
