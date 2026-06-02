#!/bin/bash

echo " СТАТИСТИКА ОЦЕНОЧЕК СТУДЕНТОВ"

echo "Данные студентов:"
echo "-----------------"
awk '{print NR ". " $1 " - " $2}' students.txt


SUM=$(awk '{sum += $2} END {print sum}' students.txt)
echo "1. Сумма всех оценочек: $SUM"

AVG=$(awk '{sum += $2} END {print sum/NR}' students.txt)
echo "2. Средняя оценочка: $AVG"

MAX=$(awk 'NR==1 {max=$2} $2>max {max=$2} END {print max}' students.txt)
echo "3. Максимальная оценочка: $MAX"


