#!/bin/bash

if [ $# -lt 2 ]; then
    echo "Ошибка! Недостаточно входящих данных."
    echo "Использование: ./impulse.sh [имя гена] [уровень экспрессии]"
    exit 1
fi

GENE_NAME=$1
EXPRESSION=$2

echo "Экспрессия гена $GENE_NAME составляет $EXPRESSION единиц"
