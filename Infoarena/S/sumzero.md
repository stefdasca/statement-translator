Sumzero

Roxy, the space traveler, is facing a very abstract problem. Since she has no idea how to solve it, you, as her best friend, need to help her. She receives an array $c_1, c_2, \dots, c_N$ containing $N$ integers and $Q$ pairs of endpoints $(L_i, R_i)$, each representing the subarray $c_{L_i}, c_{L_i + 1}, \dots, c_{R_i}$, where $1 \leq i \leq Q$. For each pair $(L_i, R_i)$, Roxy is asked what is the maximum number of disjoint subsequences with sum $0$ that she can choose from the subarray $c_{L_i}, c_{L_i + 1}, \dots, c_{R_i}$. Two subsequences are considered disjoint if they have no elements in common; however, they can have adjacent endpoints. Note that there may be elements in the queried array that are not part of any chosen subsequences.

## Input data

The input file `sumzero.in` contains a single integer $N$ on the first line. The second line contains $N$ integers separated by spaces $c_1, c_2, \dots, c_N$. The third line contains the number of queries $Q$. The next $Q$ lines each contain two numbers $(L_i \; R_i)$, representing the $i$-th query.

## Output data

The output file `sumzero.out` will contain $Q$ lines, with line $i$ containing the answer to the $i$-th query.

## Constraints

$1 \leq N \leq 400\ 000$  
$1 \leq Q \leq 400\ 000$  
$-10^9 \leq c_i \leq 10^9$  
$1 \leq L_i \leq R_i \leq N$

For 20 points, $1 \leq N, Q \leq 5\ 000$

For another 40 points, $1 \leq N, Q \leq 100\ 000$

## Example

`sumzero.in`  
```
10  
1 2 -3 0 1 -4 3 2 -1 1  
3  
1 10  
1 5  
2 9  
```

`sumzero.out`  
```
2  
1  
2  
```