#! /bin/bash

cd /home
touch info.txt
echo Time: > info.txt
date >> info.txt
echo User: >> info.txt
whoami >> info.txt
echo OS: >> info.txt
uname >> info.txt
echo Num folders: >> info.txt
ls -la | grep ^d | wc -l >> info.txt
echo Num files: >> info.txt
ls -laR | grep "^-" | wc -l >> info.txt
