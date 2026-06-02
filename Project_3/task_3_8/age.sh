#!/bin/bash

CURRENT_YEAR=2026

read -p "Введите ваше имя: " NAME
read -p "Введите год рождения: " BIRTH_YEAR

AGE=$((CURRENT_YEAR - BIRTH_YEAR))

echo "Привет, $NAME!"
echo "Ваш возраст: $AGE лет"

