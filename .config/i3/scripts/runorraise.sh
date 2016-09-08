#!/bin/shi
#simple script to run or raise a proces if it is already running.
#usage: runorraise.sh [process name--that works with pgrep {lowercase}] [classame {from xprop}]

if [ $(pgrep $1 | wc -w) -gt 0 ]; then
    i3-msg "[class=$2] focus"
else
    $2 &
fi
