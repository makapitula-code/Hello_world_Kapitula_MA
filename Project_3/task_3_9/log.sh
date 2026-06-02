#!/bin/bash

FILE_PATH="./system.log"
ERROR_CODE=1
if [ -f "$FILE_PATH" ]; then
    echo "Логфайл найден."
else
    echo "Ошибка: файл нк существует."
fi

case $ERROR_CODE in
    0)l
        echo "Статус: Ошиок нет." ;;
    1)
        echo "Статус: Критическая ошибка!" ;;
    *)
        echo "Статус: Неизвестный код." ;;
esac
