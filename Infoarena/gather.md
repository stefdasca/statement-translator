Gather

Our good friend Gigel ended up in prison. The prison has $N$ cells linked together by $M$ corridors that can be traversed in both directions. There are $K$ prisoners in total in the prison. Very intelligent and practical, Gigel already has an escape plan, but he needs all the prisoners for that. Initially, Gigel is in cell $1$, and the way he can gather the prisoners is as follows: he walks through the prison corridors, and when he meets a new prisoner, he tells them the plan, and from then on, the prisoner must follow him (Gigel wants to make sure no prisoner will betray him, therefore, he never lets any prisoner who knows about his plan out of sight). The problem is that if several prisoners are seen walking together in certain corridors, the prison guards will become suspicious, and Gigel's plan will fail. Because he wants everyone to be as rested as possible to maximize the chances of success, Gigel must minimize the total distance traveled by all the prisoners and himself. The prisoners stay put until Gigel comes to them, after which they will always follow him.

## Task

Calculate the minimum sum of the distances traveled by the prisoners and Gigel to gather them all in one cell.

## Input data

The input file `gather.in` contains on the first line three natural numbers $K , N , M$. The next $K$ lines contain one number each, representing the cells where the prisoners are initially located. Following this, there will be $M$ lines each containing four natural numbers $A , B , C , D$ with the following meaning: there is a corridor of length $C$ between cells $A$ and $B$ which can be traversed by a maximum of $D$ prisoners (excluding Gigel).

## Output data

The output file `gather.out` will contain a single line which contains the required minimum distance.

## Constraints and clarifications

$1 \leq N \leq 750$

$1 \leq K \leq 15$

$1 \leq M \leq 1250$

$C$ and $D$ will fit in 32 bits for each edge

The result will fit in 32 bits

There will not be multiple prisoners in the same cell

Gigel can pass through cells with prisoners without telling them the plan at this moment, planning to visit them again later

There will always be a solution

## Example

`gather.in`

```
2 4 5
4
2
1 2 50 1
2 3 75 2
2 4 25 1
3 4 100 2
3 1 10 2
```

`gather.out`

```
100
```

## Explanation

Gigel goes from cell $1$ to cell $2$ covering a distance of $50$. Here he informs prisoner $2$ about his plan. Gigel then goes together with prisoner $2$ to cell $4$, both traveling a distance of $2*25$. Here prisoner $1$ is also informed about the plan.

---

The above translation and formatting should provide you with the competitive programming problem statement in English while preserving the original structure and format, including specific syntax, variable names, and custom image formats. Please review the text for any potential grammar or syntax errors according to English language rules.