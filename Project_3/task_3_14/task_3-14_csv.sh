#!/bin/bash

echo "     АНАЛИЗ ФАЙЛА data.csv"

echo "1. Названия товаров:"
echo "-------------------"
awk -F "," '{print $2}' data.csv

echo ""
echo "2. Товары дороже 20:"
echo "-------------------"
awk -F "," '$3 > 20 {print $2 " - " $3}' data.csv

echo ""
echo "3. Общая стоимость:"
echo "------------------"
SUM=$(awk -F "," '{sum += $3} END {print sum}' data.csv)
echo "Общая стоимость всех товаров: $SUM"
