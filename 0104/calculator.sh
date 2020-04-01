#!/bin/bash

clear
n=0
i="y"
echo "Enter first number:"
read n1
echo "Enter second number:"
read n2
while [ $i = "y" ]
do
echo -e "\n-----MENU-----"
echo " 1.Addition"
echo " 2.Subtraction"
echo " 3.Multiplication"
echo " 4.Division"
echo " Enter your choice:"
read ch
case $ch in 
       1)n=`expr $n1 + $n2`
         echo "Sum of two numbers = "$n;;
       2)n=`expr $n1 - $n2`
         echo "Difference between two numbers = "$n;;
       3)n=`expr $n1 \* $n2`
         echo "Product of two numbers = "$n;;
       4)n=`expr $n1 / $n2`
         echo "Quotient of two numbers = "$n;;
       *)echo "Invalid Choice";;
esac
echo "Do you want to continue?"
read i
if [ $i != "y" ]
then
    exit
fi
done
