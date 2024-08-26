# Twinperms

Tell me what you choose: either we cover our backs or we stab them Georgian and Ștefan, searching in 3 rooms of the house, found two twin permutations, $p$ and $q$, of size $N$. Whenever someone swaps the elements on positions $i$ and $j$ in one permutation, the elements on the same positions in the other permutation are also swapped simultaneously. For example, if the two permutations are: $p = [2, 1, 3]$ and $q = [3, 2, 1]$, then by swapping the elements on positions $1$ and $3$, the permutations become $p = [3, 1, 2]$ and $q = [1, 2, 3]$. They can perform any number of such swaps. Both Georgian and Ștefan want to minimize the number of inversions in their respective permutations, but since every time someone changes something in one permutation, it also changes in the other, they decided to make the total number of inversions in both permutations as small as possible.

## Task

Given two permutations of size $N$, calculate the minimum sum of the number of inversions in the two permutations after applying the described swap operation any number of times.

## Input data

The input file `twinperms.in` contains the number $N$ on the first line, representing the sizes of the two permutations. On the next two lines are $N$ elements each, representing the two permutations $p$ and $q$.

## Output data

The output file `twinperms.out` should contain a single number representing the minimum sum of the number of inversions in the two permutations.

## Constraints and clarifications

The permutations are indexed from $1$ to $N$.  
$1 \leq N \leq 100000$.

For $10$ points, we have $p_i = q_i$ for all $i$, where $1 \leq i \leq N$.  
For another $10$ points, we have $p_i + q_i = N + 1$ for all $i$, where $1 \leq i \leq N$.  
For another $10$ points, we have $1 \leq N \leq 9$.  
For another $15$ points, we have $1 \leq N \leq 16$.  
For another $35$ points, we have $1 \leq N \leq 3000$. 

A permutation of size $N$ is an array of $N$ elements where each number from $1$ to $N$ appears exactly once. The number of inversions in a permutation $p$ is the number of pairs $i, j$, where $1 \leq i < j \leq N$, with the property that $p_i > p_j$.

## Example

`twinperms.in` 
```
4 
3 4 1 2 
1 4 2 3 
```

`twinperms.out` 
```
2 
```

## Explanation

We can swap the elements on positions $1$ and $3$, thus the permutations become: $p = [1, 4, 3, 2]$ and $q = [2, 4, 1, 3]$. After that, we can swap the elements on positions $2$ and $3$, thus the permutations become: $p = [1, 3, 4, 2]$ and $q = [2, 1, 4, 3]$. In the end, we can swap the elements on positions $3$ and $4$. The permutations will finally reach: $p = [1, 3, 2, 4]$ and $q = [2, 1, 3, 4]$. Since the first permutation has one inversion, namely on positions $2$ and $3$, and the second permutation also has one inversion, namely on positions $1$ and $2$, the total number of inversions will be $2$. This sum is minimal.