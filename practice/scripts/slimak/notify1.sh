#!/bin/sh
files=(/home/janek/practice/scripts/slimak/images/*)
IMAGENAME=(${files[RANDOM % ${#files[@]}]})
echo $IMAGENAME >> /home/janek/practice/scripts/slimak/logs
pqiv -c -c -i $IMAGENAME
#pqiv -c -c -i  /home/janek/practice/scripts/slimak/images/snail-1.png
#echo "dziala" >> /tmp/slimak.txt
