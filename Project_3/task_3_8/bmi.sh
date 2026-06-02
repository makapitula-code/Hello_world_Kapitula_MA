#!/bin/bash

echo "     АНАЛИЗАТОР ИНДЕКСА МАССЫ ТЕЛА"

read -p "Введите вашу массу (в кг): " WEIGHT
read -p "Введите ваш рост (в см): " HEIGHT_CM
HEIGHT_M=$(echo "$HEIGHT_CM / 100" | bc -l)
BMI=$(echo "$WEIGHT / ($HEIGHT_M * $HEIGHT_M)" | bc)

echo ""
echo "------------------------"
echo "Ваш ИМТ: $BMI"
echo "------------------------"

if [ $BMI -lt 18 ]; then
    echo "Статус: Недостаточная масса тела"
elif [ $BMI -lt 25 ]; then
    echo "Статус: Нормальная масса тела"
elif [ $BMI -lt 30 ]; then
    echo "Статус: Избыточная масса тела"
else
    echo "Статус: Ожирение"
fi

