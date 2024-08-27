# Intersection

On a circle, there are $N$ equidistant points labeled in clockwise direction as $1,2,3,\dots,N$. You are given $M$ intervals in the form $[a;b]$ and $T$ queries in the form $P Q$.

## Task

For each query $[P;Q]$, check if it is true or false that the intersection of all intervals that have common points with $[P;Q]$ includes the interval $[P;Q]$.

## Input data

The input file `intersectie.in` contains on the first line the numbers $N$, $M$, and $T$. On the next $M$ lines, two natural numbers $a$ $b$, separated by space, are written, representing the endpoints of the $M$ intervals given. On the next $T$ lines, two natural numbers $P$ $Q$, separated by space, are written, representing the endpoints of the $T$ query intervals given.

## Output data

The output file `intersectie.out` contains in the first $T$ lines a natural number: $1$ if the answer to the query is true, and $0$ if the answer is false.

## Constraints and clarifications

$2 \leq N \leq 10^9$  
$1 \leq M \leq 10^5$  
$1 \leq T \leq 10^5$  
$1 \leq P \leq N$  
$1 \leq Q \leq N$  
$P$ and $Q$ are labels given in the clockwise direction  
$1 \leq a \leq N$  
$1 \leq b \leq N$  
$a$ and $b$ are labels given in the clockwise direction  
If $x=y$, then $[x;y]$ is an interval that contains only the number $x$  
For $30\%$ of tests $1 \leq M \leq 1000$  
and $1 \leq T \leq 10\,000$  
For $30\%$ of tests $1 \leq N \leq 10^6$  

## Example

`intersectie.in`  
`5 3 3`  
`2 3`  
`5 1`  
`5 5`  
`4 4`  
`3 5`  
`1 1`  

`intersectie.out`  
`0`  
`0`  
`1`  

## Explanation

The interval $[4;4]$ from query 1 does not intersect with any of the three given intervals $[2;3]$, $[5;1]$, $[5;5]$. Answer $0$. The interval $[3;5]$ from query 2 intersects with $[2;3]$, $[5;1]$, $[5;5]$. The intersection of these is empty. Answer $0$. The interval $[1;1]$ from query 3 intersects only with $[5;1]$. The intersection of the intervals containing $[1;1]$ is $[5;1]$. Answer $1$.