# Permking

The King of Permutations has made an announcement throughout the land, proclaiming his immense power: "I fear nothing but my own power!" Given a permutation $P$ of length $N$, $M$ operations of the type $a$, $b$ are executed on this permutation: sort all elements in the interval $[a, b]$ in ascending order. After the $M$ operations, the permutation is considered sorted if all elements appear in strictly ascending order (imagine how a sorted permutation looks). Given $M$ and the $M$ operations, respond with $1$ if the operations are sufficient to sort ANY existing permutation $P$ of length $N$, and with $0$ if they are not.

## Input data

The input file `permking.in` will contain a natural number $T$ representing the number of tests. The following lines contain the $T$ tests in the following format: the first line contains $2$ natural numbers $N$ and $M$. The next $M$ lines contain $2$ natural numbers $a$, $b$ representing the $M$ operations.

## Output data

The output file `permking.out` will contain $T$ lines, where line $x$ contains the answer for test $i$ ($0$ or $1$).

## Constraints and clarifications

$1 \leq T \leq 20$  
$1 \leq N$, $M \leq 1000$  
$1 \leq a \leq b \leq N$  

## Example

`permking.in` `permking.out`  
$2$  
$2$ $1$  
$1$ $2$  
$3$ $1$  
$1$ $2$  
$1$  
$0$  

## Explanation

In the first case, both the permutation $(1, 2)$ and the permutation $(2, 1)$ are sorted correctly. In the second case, the permutation $(2, 3, 1)$ is not sorted correctly.