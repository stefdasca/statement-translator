# Bacterii2

On a distant planet, there are two bacterial populations with $N$ and $M$ individuals, respectively. For each individual, their resistance to external factors is known. We also know that when an individual from the first population, with resistance $r1$, mates with an individual from the second population, with resistance $r2$, a new mutant individual results, having resistance $r1 + r2$. Knowing that over time, each individual from the first population mates exactly once with every individual from the second population, determine the resulting mutant population. 

## Input Data

The input file `bacterii2.in` contains on the first line a natural number $T$, the number of tests. Each test contains the value of $N$ on the first line. The next line contains $N$ values, the $i$-th value $(R_i)$ being the resistance of the $i$-th individual from the first population. The next line contains the value of $M$. Similarly, the following line will contain $M$ values, the $i$-th value $(R_i)$ being the resistance of the $i$-th individual from the second population. 

## Output Data

In the output file `bacterii2.out` for each test, the resulting population will be displayed as pairs of positive numbers $(resistance, number\_of\_individuals)$, each on a separate line and sorted in ascending order by resistance. A blank line will be left between two consecutive tests.

## Constraints and Clarifications

$1 \leq T \leq 5$  
$1 \leq N, M \leq 30\, 000$  
$1 \leq R_i \leq 30\, 000$  

## Example

`bacterii2.in`  
```
2
1
1
1
2
2
1
2
2
1
1
3
1
2
2
3
2
```

`bacterii2.out`
```
2 1
3 1

2 2
3 2
4 1
5 1
```

## Explanation

For the 2nd test, the following mating occurs:  
$1 + 1 = 2$  
$1 + 1 = 2$  
$2 + 1 = 3$  
$2 + 1 = 3$  