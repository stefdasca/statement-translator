## Task

You are the sentinel of a guild of merchants. This morning, $n$ merchants (numbered from $1$ to $n$) have lined up to enter the city's commercial alley. Along the alley, there are $n$ locations where merchants can park their carts to later sell their goods. Starting with merchant number $1$, each merchant, one after another, enters the alley with their cart, heads towards the assigned location, and if it is free, occupies it. Otherwise, the merchant continues towards the next free spot and occupies it. If all subsequent locations are occupied, they leave the city without selling their goods. Merchants cannot turn their carts around due to the narrowness of the alley. Your task as a sentinel is to allocate the merchants to the locations along the alley. Local merchants are given priority in the sense that they are allocated to their favorite location, whereas foreign merchants will have to accept any location you designate. Given the preferred locations of the local merchants, you need to decide if there exists an allocation of foreign merchants to the locations on the alley such that each merchant (both local and foreign) finds a free spot. If such an allocation exists, you need to find the number of valid allocations modulo a given integer $M$. Let's consider an example. Suppose there are four merchants. The first three are local merchants with favorite spots $2$, $1$, and $1$ respectively. The last merchant is foreign. Each merchant finds a free spot in each of the following four cases: $(2, 1, 1, 1)$, $(2, 1, 1, 2)$, $(2, 1, 1, 3)$, $(2, 1, 1, 4)$, where, for example, $(2, 1, 1, 3)$ means that the first merchant is allocated position $2$, $\dots$, and the last merchant position $3$. This example shows that different local merchants can have identical favorite spots, a foreign merchant can be allocated a location desired by a local merchant, and the final location of a local merchant can be far from their favorite location.

## Input data

The input file `negustori.in` contains on the first line three integers $n$, $m$, $M$, separated by space, where $m$ represents the number of local merchants among all $n$ merchants. On the next line will be $m$ pairs of numbers $a_1$, $b_1$, $\dots$, $a_m$, $b_m$, with $1 \leq a_i$, $b_i \leq n$ and all $a_i$ being distinct, where $a_i$ is the position of the $i$-th local merchant in the queue and $b_i$ is their favorite spot. If there are no local merchants, this line will be empty.

## Output data

The output file `negustori.out` will contain a single line, containing either NO if it is impossible for each merchant to get a free location, or YES followed by the total number of allocations modulo $M$ (separated by a space).

## Constraints and clarifications

$1 \leq n \leq 300$

$0 \leq m \leq n$

$2 \leq M \leq 10^9$

## Example

`negustori.in` 

```
4 3 10 
1 2 
2 1 
3 1
```

`negustori.out` 

```
YES 4
```

## Explanation

This is the example from the task.