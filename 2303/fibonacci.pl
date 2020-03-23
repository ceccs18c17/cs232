#!/usr/bin/perl

print "Enter limit: ";
$limit=<>;
$a=0;
$b=1;
print "Fibbonacci series:\n";
print "$a\n$b\n";
while ($c < $limit)
{
$c=$a+$b;
print "$c\n";
$a=$b;
$b=$c;
}


