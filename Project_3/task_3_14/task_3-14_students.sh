#!/bin/bash

echo "     АНАЛИЗ ФАЙЛА students.txt"

echo "1. Имена студентов:"
echo "-------------------"
awk '{print $1}' students.txt

echo ""
echo "2. Оценки студентов:"
echo "-------------------"
awk '{print $2}' students.txt

echo ""
echo "3. Номер строки и имя студента:"
echo "-------------------------------"
awk '{print NR, $1}' students.txt
