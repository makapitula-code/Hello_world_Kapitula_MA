#!/bin/bash

sed -i '' 's/ /\t/g' sequences.txt

echo "Замена выполнена!"
echo ""
echo "Результат:"
cat sequences.txt
