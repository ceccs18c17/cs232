@array = (2, 3, 4, 5, 6, 7); 
$n = $#array; 
print "The original array is : "; 
for $i (0 .. $#array) 
{ 
    print $array[$i], "   "; 
} 
for my $i (0 .. $#array/2) 
{ 
    $temp = $array[$i]; 
    $array[$i] = $array[$n-$i]; 
    $array[$n-$i] = $temp; 
} 
print "\nThe reversed array is : "; 
for $i (0 .. $#array) 
{ 
    print $array[$i], "   "; 
} 

