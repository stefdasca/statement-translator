# Sequence 5

Zaharel has to solve another problem with sequences! This time, he has an array of $N$ natural numbers and wants to know how many subarrays with between $L$ and $U$ distinct elements exist in that array. 

## Input data

The first line of the input file `secv5.in` contains the natural numbers $N$, $L$, $U$. The next $N$ lines each contain a natural number, each representing an element of the array. 

## Output data

The first line of the file `secv5.out` will contain the number of subarrays that contain between $L$ and $U$ distinct elements. 

## Constraints and clarifications

$1 \leq L$   
$L \leq U$   
$U \leq N$   
$N \leq 2 \cdot 10^2$    

The value of an element in the array is a natural number in the interval $[1 \dots 2^{32} -1]$  

A subarray is a subsequence of elements that appear in consecutive positions in the initial array 

## Example

`secv5.in`
```
5 2 3
13 13 7 9 9
```

`secv5.out`
```
8
```

## Explanation

The $8$ sequences are:  
$13$ $13$ $7$  
$13$ $13$ $7$ $9$  
$13$ $13$ $7$ $9$ $9$  
$13$ $7$  
$13$ $7$ $9$  
$13$ $7$ $9$ $9$  
$7$ $9$  
$7$ $9$ $9$  