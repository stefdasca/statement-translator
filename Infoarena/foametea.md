# Hunger

Our favorite hungry person lives in a country with $N$ cities connected by $M$ one-way roads. Each road in his country has a certain length, $L_i$, and a certain difficulty $C_i$, equal to the number of stuffed cabbages that the hungry person must consume at the start of traveling on that road in order to successfully traverse it. He can carry a maximum of $K$ stuffed cabbages in his backpack and, fortunately, in each city he knows an aunt who offers him up to $s_i$ stuffed cabbages each time he visits that city. It is well known that the time required to traverse a road of length $L$ is equal to $L \cdot (S^2 + 1)$, where $S$ is the number of stuffed cabbages remaining in his backpack after consuming the amount needed to traverse that road. The hungry person, because he is too hungry to manage on his own, asks you to tell him how quickly he can get to the festive dinner in city $N$ (where stuffed cabbages will be served), starting from city $1$.

## Task

The input file foametea.in will contain on the first line the numbers $N$ (the number of cities), $M$ (the number of roads), $K$ (the capacity of the hungry person's backpack). The next line will contain the numbers $s_1, s_2, \dots, s_N$ (the maximum number of stuffed cabbages offered by each of the $N$ aunts). The following $M$ lines will each contain 4 integers, $A$, $B$, $L$, $C$ signifying that there is a road that starts from city $A$, reaches city $B$, has length $L$ and can be traversed by the hungry person consuming $C$ stuffed cabbages.

## Input data

The input file foametea.in will contain on the first line the numbers $N$ (the number of cities), $M$ (the number of roads), $K$ (the capacity of the hungry person's backpack). The next line will contain the numbers $s_1, s_2, \dots, s_N$ (the maximum number of stuffed cabbages offered by each of the $N$ aunts). The following $M$ lines will each contain 4 integers, $A, $ B, $L, $ C$ signifying that there is a road that starts from city $A$, reaches city $B$, has length $L$ and can be traversed by the hungry person consuming $C$ stuffed cabbages.

## Output data

The output file foametea.out will contain a single line with the answer to the hungry person's question. If he cannot reach the festive dinner, print the message `Fomistul moare de foame`.

## Constraints

$1 \leq N \leq 5000$

$1 \leq M \leq 25000$

$0 \leq K \leq 30$

$0 \leq s_i \leq K$

$1 \leq A, B \leq N$

$0 \leq L \leq 10000$

$0 \leq C \leq K$

Clarifications

For tests worth 20 points, it is guaranteed that $L = 1$ and that $C = 0$ for all roads.

For other tests worth 20 points, it is guaranteed that $C = 0$ for all roads and that there are no cycles (the resulting graph is a DAG).

For other tests worth 30 points, it is guaranteed that $C = 0$ for all roads.

For other tests worth 30 points, the initial constraints apply.

In each city $i$, the hungry person can choose to put in his backpack any number of stuffed cabbages between $0$ and $s_i$, as long as the total number does not exceed the limit of $K$. The hungry person initially has $0$ stuffed cabbages in his backpack. He will take as many as he deems fit from the aunt in the first city.

## Example

`foametea.in`

```
5 3 5
4 3 0 2 0
1 3 7 2
3 5 8 2
1 3 5 2
```

`foametea.out`

```
43
```

`foametea.in`

```
5 2 3
5 2 3 1 0
1 2 1 5
4 1 5 2
4 5 4 1
```

`foametea.out`

```
Fomistul moare de foame
```

`foametea.in`

```
6 10 24
24 11 15 8 16 23
2 6 2 19
1 3 5 0
5 4 3 12
2 5 4 12
4 2 5 9
3 5 3 21
1 2 5 15
3 2 3 23
3 4 4 20
6 1 3 14
```

`foametea.out`

```
327
```

## Explanation

ex. 1: The hungry person loads 4 stuffed cabbages from the first city into his backpack. He prepares for the road (1, 3) by eating 2 of the stuffed cabbages from his backpack and reaches city 3 in $7 \cdot (1 + 2^2) = 35$ time units. In city 3, no stuffed cabbages are offered. He prepares for the road (3, 5) by eating 2 stuffed cabbages and reaches city 5 after another $8 \cdot (1 + 0^2) = 8$ time units. The final answer is therefore 35 + 8 = 43.

ex. 2: The hungry person cannot reach city 5.