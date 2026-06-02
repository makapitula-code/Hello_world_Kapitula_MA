#!/bin/bash

sed -i '' 's|/var/lib/mysql/data|/mnt/ssd/mysql|g' settings.php

echo "Замена выполнена!"
echo "Проверка результата:"
grep "db_data_path" settings.php
