#!/bin/bash

check_root() {
    if [ $EUID -ne 0 ]; then
        echo "Ошибка: Скрипт должен быть запущен от имени суперпользователя (root)!"
        echo "Пожалуйста, используйте: sudo $0"
        exit 1
    else
        echo "Успешно: Скрипт запущен от имени root."
    fi
}

check_root


echo ""
echo "Выполняем основные операции..."
echo "Текущий пользователь: $(whoami)"
echo "Ваш UID: $EUID"
