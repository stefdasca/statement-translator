# Temple

Tassadar wants to explore a Xel'Naga temple, but to be able to enter, he needs to enter a secret code. After some mathematical calculations, he made some observations that can help him discover the secret code. Given a constant $K$ and an array $V$ of $N$ integers. Each position $i$ in the array has an associated cost $C_i$. We define $Next_i = \max(i, \min(j | i < j, V_i < V_j))$, and $Next_i^P = Next_{Next_i^{P-1}}$. Let the array $S$ of $N$ integers, $S_i = \max(C_i, C_{Next_i}, C_{Next_i^2}, \dots, C_{Next_i^{K-1}})$. The secret code is the array $S$! Tassadar managed to get inside the Xel'Naga temple. Can you?

## Input data

The input file `temple.in` contains on the first line two integers $N$ and $K$ as per the statement. The second line contains $N$ integers $V_i$ representing the array $V$. The next line contains $N$ integers $C_i$ representing the costs of the positions in the array $V$.

## Output data

In the output file `temple.out` you will print on the first line $N$ integers $S_i$ representing the secret code. 

## Constraints and clarifications

$1 \leq K \leq N \leq 10^5$  

$-10^9 \leq V_i \leq 10^9$  

$-10^{15} \leq C_i \leq 10^{15}$

## Example

`temple.in`  
4 2  
2 3 1 4  
5 6 1 2  

`temple.out`  
6 6 2 2

## Explanation

The array $Next$ is $\{2, 4, 4, 4\}$, and the array $S$ is $\{\max(5, 6), \max(6, 2), \max(1, 2), \max(2)\} = \{6, 6, 2, 2\}$.