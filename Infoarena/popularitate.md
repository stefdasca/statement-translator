## Task

Given $K$ and $M$ groups of numbers. Each of the $M$ groups contains $N_i$ numbers. Let $G_i$ be the product of the numbers in group $i$. We define the popularity of a group as $P$ if $K^P$ divides $G_i$ and $K^{P+1}$ does not divide $G_i$, or equivalently, the number of times $G_i$ is divisible by $K$. The task is to determine the group with the maximum popularity.

## Input data

The input file `popularitate.in` contains on the first line $K$, and on the second line $M$. On the next $M$ lines, the descriptions of the groups are found. On line $i+2$, the first value represents $N_i$. It is followed by the $N_i$ numbers associated with group $i$.

## Output data

In the output file `popularitate.out` you will print 2 values representing the highest popularity and the group that has this popularity. If there are multiple groups with maximum popularity, print the group with the smallest index.

## Constraints

$2 \leq K \leq 10000000$ (10 million)  
$1 \leq M \leq 100$  
$1 \leq N_i \leq 2000$  
The groups are formed from natural numbers in the interval $[1, 100000000]$ (100 million)  
For 30% of the tests $K$ is prime.  
For 30% of the tests $N_i \leq 100$.

## Example

`popularitate.in`  
```
6  
3  
6 2 3 5 8 12 9  
4 5 7 64 11  
3 4 9 81  
```

`popularitate.out`  
```
4 1  
```

## Explanation

Group 1 has popularity $4$, $2 \times 3 \times 5 \times 8 \times 12 \times 9 = 25920 = 6^4 \times 20$  
Group 2 has popularity $0$, $5 \times 7 \times 64 \times 11 = 24640$ is not divisible by $6$  
Group 3 has popularity $2$, $4 \times 9 \times 81 = 2916 = 6^2 \times 81$