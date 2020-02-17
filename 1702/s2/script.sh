#!/bin/bash

# Clears current screen
clear

# Coverts .pdf to .txt
pdftotext -layout result_CHN.pdf result_CHN.txt

#Seperates the results of CS students
grep --no-group-separator -A3 "CHN18CS" result_CHN.txt > result_cs.txt 

#Arrange the data in organised manner
tr  '\n' ' ' < result_cs.txt > result_cs1.txt
sed 's/\t//g' result_cs1.txt > result_cs2.txt
awk '{$1=$1;print}' result_cs2.txt > result_cs3.txt
sed 's/CHN/\nCHN/g' result_cs3.txt > result_cs4.txt
tr  ',' ' ' < result_cs4.txt > result.txt

#Converts grade to gradepoints
sed -i 's/(O)/ 10/g' result.txt
sed -i 's/(A+)/ 9/g' result.txt
sed -i 's/(A)/ 8.5/g' result.txt
sed -i 's/(B+)/ 8/g' result.txt
sed -i 's/(B)/ 7/g' result.txt
sed -i 's/(C)/ 6/g' result.txt
sed -i 's/(P)/ 5/g' result.txt
sed -i 's/(F)/ 0/g' result.txt
sed -i 's/(FE)/ 0/g' result.txt
sed -i 's/(I)/ 0/g' result.txt
sed -i 's/(Absent)/ 0/g' result.txt

# Seperates gradepoints
awk  '{
	print $1,$3,$5,$7,$9,$11,$13,$15,$17,$19
 }' result.txt > gp.txt

# Computes CGPA and counts subjects failed in
awk '{
	sum = 0
	flag = 0
	fails = 0
	for(var =2; var<=NF; var++)
	{
		if($var == 0)
		{
			flag = 1
			fails = fails + 1
		}
		sum += $var
	}
	cgpa = sum/9
	if (flag == 0) {
	 	printf("%s %0.2f\n",$1,cgpa)
	}
	if (flag == 1) {
		printf("%s failed in %d\n",$1,fails)
	}
}' gp.txt > cgpa_raw.txt

#adds name and rollno
join students.txt cgpa_raw.txt > cgpa.txt


