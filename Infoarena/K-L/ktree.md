# Ktree

Miruna reached the Wonderland. This enchanted land is made up of $N$ cities connected by $N-1$ roads, such that you can travel from any city to any other city using the existing road network. Because she's tired of being treated as a nice princess, Miruna wants to detonate exactly $M$ roads. Some roads are better constructed than others, so Miruna needs more explosives to achieve her malicious goal. For each road, the cost to acquire the necessary explosives for its detonation is known. After the chosen roads are destroyed, Miruna still wants to be able to travel from city $1$ to exactly $K$ cities using what remains of the road network to rob the merchants coming from distant lands. Help the girl who arrived in Wonderland spend as little as possible!

## Input data

The first line of the input file `ktree.in` will contain 3 integers $N, M, \text{and } K$ corresponding to the statement. On the next $N-1$ lines, there will be 3 numbers $A, B, \text{and } C$, signifying that there is a bidirectional road between city $A$ and city $B$ with a detonation cost of $C$.

## Output data

The file `ktree.out` will contain a single integer representing the minimum required cost or $-1$ if there is no solution.

## Constraints and clarifications

$1 < N < 75$

$1 \leq M < N$

$1 \leq K < N$

The costs of the roads will be less than $1000$.

## Examples

`ktree.in`
```
2 1 1 
1 2 3 
```
`ktree.out`
```
3
```
`ktree.in`
```
10 4 3 
1 2 10 
1 3 21 
1 4 4 
2 7 2 
3 5 5 
3 6 12 
6 8 7 
6 9 6 
6 10 3 
```
`ktree.out`
```
23
```

## Explanation

In the first example, Miruna will detonate the only road, which has a cost of 3. In the second example, she will destroy the roads between the following pairs of cities: $(2, 7)$, $(3, 5)$, $(3, 6)$, $(1, 4)$.