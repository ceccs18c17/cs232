#!/bin/bash

echo -e "Your username: $USER\n"
echo -e "Your current shell: $SHELL\n"
echo -e "You home directory: $HOME\n"
echo -e "Your operating system type:\n"
uname -o
echo -e "\nYour current path setting: $PATH\n"
echo -e "Your current working directory:"
pwd
echo -e "\n Number of users currently logged in:"
w
