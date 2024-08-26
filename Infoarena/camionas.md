# Little Truck

Once upon a time, there was a little truck in a fairy tale. In this fairy tale world, there were $N$ villages, numbered from $1$ to $N$, and $M$ bidirectional roads connecting them. As not even in fairy tales are roads built properly, each of the $M$ roads has a resistance $g_i$. However, our fairy tale is a modern one, and PIZZA is one of its basic elements. Our little truck has a weight $G$ and is initially in village $1$. Its mission is to transport PIZZA from village $1$ to village $N$. Being very considerate, the little truck thinks that it should not travel on roads with resistance strictly less than its weight, as these roads could break. Still, since delivering PIZZA is its life purpose, it wonders what is the minimum number of roads whose resistance must be increased so that it can transport PIZZA from village $1$ to village $N$ without having to travel on roads with resistance strictly less than its weight. Since our little truck is not exactly an expert in graph theory, it thought that you might be able to help it by providing the answer to this question.

## Input data

The input file `camionas.in` contains on the first line three natural numbers $N$ $M$ $G$, with the meaning given in the statement. On the next $M$ lines, there will be pairs of three natural numbers, $x$ $y$ $g$, indicating the existence of a road between villages $x$ and $y$, with resistance $g$.

## Output data

In the output file `camionas.out`, there will be a single natural number, representing the minimum number of roads whose resistance must be increased so that the little truck can complete its mission.

## Constraints and clarifications

$1 \leq N \leq 50\ 000$

$1 \leq M \leq 100\ 000$

$1 \leq G \leq 1\ 000\ 000$

$1 \leq g_i \leq 1\ 000\ 000$

It is guaranteed that there is at least one path between village $1$ and village $N$.

PIZZA is the key element in solving this problem!

## Example

`camionas.in`

```
6 6 7
1 2 8
2 5 6
5 6 5
1 3 7
3 4 11
4 6 3
```

`camionas.out`

```
1
```

## Explanation

The truck, with a weight of $7$, has two routes to choose from: $1 \dots 2 \dots 5 \dots 6$ and $1 \dots 3 \dots 4 \dots 6$. On the first route, there are two roads with resistance less than $7$: roads $2 \dots 5$ and $5 \dots 6$, while on the second route, there is only one road with resistance less than $7$: road $4 \dots 6$.