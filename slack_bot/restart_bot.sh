#!/bin/sh

# restart a process that dies
# https://unix.stackexchange.com/questions/107939/how-to-restart-the-python-script-automatically-if-it-is-killed-or-dies

while true; do
  #nohup python3 bot.py >> bot.out
  python3 bot.py >> bot.out
done &
