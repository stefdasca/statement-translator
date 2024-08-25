## Task

An array with $N$ natural numbers is given. Additionally, $M$ operations are provided, which can be of two types:

$0\ x\ y\ z$: The values at positions within the interval $[x,\ y]$ increase by the value $z$.  
$1\ x\ y$: The sum of the form $a[x]*1 + a[x+1]*2 + \dots + a[y]*(y-x+1)$ is required. 

## Input data

The input file `suma5.in` contains on the first line a natural number $N$, which represents the size of the array, followed by a natural number $M$, which represents the number of operations. The second line contains the $N$ values. The next $M$ lines contain the operations, in the form described in the statement.

## Output data

The output file `suma5.out` will contain the answers for the operations of type $1$ in the order they appear in the input file.

## Constraints and clarifications

$1 \leq N \leq 10^5$  
$1 \leq M \leq 10^5$  
$1 \leq a[i] \leq 10^5$  
$1 \leq z \leq 10^3$  
$1 \leq x \leq y \leq N$  

## Example

`suma5.in`  
`10 7`  
`3 1 7 8 6 5 4 2 9 10`  
`1 5 10`  
`0 6 10 1`  
`1 7 7`  
`0 10 10 9`  
`0 1 6 6`  
`1 4 7`  
`1 7 10`  
`suma5.out`  
`141`  
`5`  
`94`  
`121`