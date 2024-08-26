## Task

Little Johny relaxes by sorting permutations. Thus, he randomly chooses a permutation with $N$ elements. As long as this permutation is not sorted in increasing order, Johny chooses two numbers from consecutive positions in the permutation and swaps them. After some time, he learns how to sort any permutation by the above procedure using the minimum number of swaps. Once Johny improves his algorithmic skills, instead of swapping only elements from consecutive positions, he will be able to swap any two elements in the permutation. Johny learns to sort permutations using a minimal number of such operations. Obviously, for any permutation, the minimum number of operations to sort it using the second procedure is less than or equal to the minimum number of operations using the first procedure. Determine how many permutations with $N$ elements can be sorted faster by the second procedure than by the first procedure (with the optimal number of swaps being smaller). Since the answer can be very large, only the remainder of its division by $999017$ will be displayed.

## Input data

The input file `sortari2.in` contains the natural number $N$ on the first line, as described in the statement.

## Output data

The output file `sortari2.out` will contain a single line which will contain the remainder of the answer divided by $999017$.

## Constraints and clarifications

$2 \leq N$  
$N \leq 1000$

## Example

`sortari2.in`  
`4`  
`sortari2.out`  
`11`

## Explanation

There are $11$ permutations with the required property:

$1 \, 4 \, 3 \, 2$  
$2 \, 4 \, 3 \, 1$  
$3 \, 2 \, 1 \, 4$  
$3 \, 2 \, 4 \, 1$  
$3 \, 4 \, 1 \, 2$  
$3 \, 4 \, 2 \, 1$  
$4 \, 1 \, 3 \, 2$  
$4 \, 2 \, 1 \, 3$  
$4 \, 2 \, 3 \, 1$  
$4 \, 3 \, 1 \, 2$  
$4 \, 3 \, 2 \, 1$  

For example, the permutation $4 \, 2 \, 1 \, 3$ can be sorted with a minimum number of steps using the first procedure as follows:  
$4 \, 2 \, 1 \, 3 \Rightarrow 2 \, 4 \, 1 \, 3 \Rightarrow 2 \, 1 \, 4 \, 3 \Rightarrow 1 \, 2 \, 4 \, 3 \Rightarrow 1 \, 2 \, 3 \, 4$ .  
A total of $4$ steps were necessary. Using the second procedure, the permutation can be sorted faster as follows:  
$4 \, 2 \, 1 \, 3 \Rightarrow 4 \, 2 \, 3 \, 1 \Rightarrow 1 \, 2 \, 3 \, 4$ .  
Only $2$ steps were necessary.
