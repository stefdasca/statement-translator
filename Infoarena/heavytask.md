Heavytask

Petrica has a new hard problem that he wants to solve. He has an array $A$ of length $N$ consisting of strictly positive natural numbers and he wants to obtain an array $B$ of strictly positive natural numbers of length $N$ with the following properties: $B[i]$ divides $A[i]$ for $1 \leq i \leq N$ and the least common multiple of the numbers in array $A$ must be equal to the least common multiple of the numbers in array $B$. In case there are multiple arrays $B$ that satisfy the two properties, Petrica wants to obtain the lexicographically smallest one.

##  Input data

The input file `heavytask.in` contains on the first line a natural number $T$ representing the number of tests. The first line of a test contains a natural number $N$ which represents the length of the array. The next line of a test will contain $N$ numbers separated by a space representing the array $A$.

##  Output data

In the output file `heavytask.out` you will print $T$ lines, each line containing $N$ numbers separated by a space, representing the array $B$ for the corresponding test from the input file.

##  Constraints

$T = 5$  
$1 \leq N \leq 300$  
$1 \leq A[i] \leq 10^{18}$

##  Example

`heavytask.in`  
2  
2  
1 2  
5  
210 2 3 5 7

`heavytask.out`  
1 2  
1 2 3 5 7

##  Explanation

For the first test, the only possible solution is the array $1, 2$. For the second test, there are multiple possible solutions, and the lexicographically smallest one is the array $1, 2, 3, 5, 7$.