#!/bin/bash

echo -e "Your OS and version, release number:"
lsb_release -a
echo -e "\nYour linux kernel version:"
uname -r
echo -e "\nAll available shells:"
cat /etc/shells
echo -e "\nCPU information:"
cat /proc/cpuinfo
echo -e "\nMemory information:"
cat /proc/meminfo
echo -e "\nHard disk information:"
fdisk -l
echo -e "\nFile system (Mounted):"
mount -l
