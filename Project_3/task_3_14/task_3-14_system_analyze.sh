#!/bin/bash

echo "     АНАЛИЗ ИСПОЛЬЗОВАНИЯ ДИСКА"

echo "Файловая система          Заполнение"
echo "----------------------------------------"

df -h | awk 'NR > 1 {
    filesystem = $1
    use = $5
    gsub(/%/, "", use)
    
    if (use > 90) {
        printf "%-25s %s%% -> ВНИМАНИЕ! ЗАПОЛНЕНИЕ > 90%%\n", filesystem, $5
    } else {
        printf "%-25s %s\n", filesystem, $5
    }
}'

echo ""
