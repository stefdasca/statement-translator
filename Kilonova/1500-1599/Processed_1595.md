A transportation company with minibuses in Iași County has adopted its own strategy for routes within the county:

* no route can be longer than $165$ kilometers
* the distance between two consecutive stops is one kilometer
* a passenger can depart from any stop and buy tickets for traveling $1, 2, \ldots, 10$ kilometers
* each of the ten possible distances has distinct ticket prices

For example:

~[microbuz.png|]

Gigel, who travels exactly $N$ kilometers by minibus, can choose one or more distances from the ten established and buy the corresponding tickets. The company allows each passenger to purchase at most $3$ tickets of the same type. Gigel notices that for the same amount of money he can purchase different sets of tickets with distinct prices. For the above example, with $98$ lei he can buy tickets priced at $11, 14, 29, 44$ lei or tickets priced at $45, 53$ lei ($11+14+29+44 = 45+53$).

# Task

Write a program that solves the following tasks:

1. determine the minimum price of a set of tickets that can be purchased for traveling exactly $N$ kilometers;
2. determine the distances chosen by Gigel such that the total price of the trip is minimized;
3. determine two distinct sets of tickets for which the total price of the tickets is the same and is the highest possible. For each set, it is not allowed to choose multiple tickets of the same price and there are no two tickets with the same price in both sets.

# Input data

The input file `microbuz.in` contains three lines. The first line contains a natural number $C$ representing the task ($1, 2$ or $3$). The second line contains ten strictly increasing natural values, separated by spaces, representing the prices for traveling $1, 2, \ldots, 10$ kilometers. The third line contains the value $N$ representing the distance Gigel wants to travel.

# Output data

The output file `microbuz.out` has the following structure:

* if $C = 1$, the first line will contain an integer representing the minimum cost of the journey;
* if $C = 2$, each line will contain two integers, separated by a space, representing the distance traveled and the corresponding ticket price;
* if $C = 3$, the first line will contain the common price of the two sets of tickets, and the next two lines will each contain a set of tickets given by the number of km for the tickets in the set, in strictly increasing order, separated by a space.

# Constraints and clarifications

* $C \in \{1, 2, 3\}$
* $1 \leq N \leq 165$;
* the $10$ prices are natural numbers in the interval [$10, 99$]
* the answer to task $3$ does not depend on the value of $N$
* For $28$ points, $C = 1$
* For $38$ points, $C = 2$
* For $34$ points, $C = 3$

# Example 1

`microbuz.in`
```
1
11 14 18 23 29 36 44 45 53 64
15
```

`microbuz.out`
```
86
```

## Explanation

The task is $1$. The total minimum cost is $86$.

# Example 2


`microbuz.in`
```
2
11 14 18 23 29 36 44 45 53 64
15
```

`microbuz.out`
```
3 18
4 23
8 45
```

## Explanation

The task is $2$. The tickets purchased and their prices are:

$3$ km traveled, price $18$
$4$ km traveled, price $23$
$8$ km traveled, price $45$

# Example 3


`microbuz.in`
```
2
13 17 18 19 21 22 25 28 31 37
39
```

`microbuz.out`
```
7 25
7 25
8 28
8 28
9 31
```

## Explanation

The task is $2$. The tickets purchased and their prices are:

$7$ km traveled, price $25$
$7$ km traveled, price $25$
$8$ km traveled, price $28$
$8$ km traveled, price $28$
$9$ km traveled, price $31$

# Example 4


`microbuz.in`
```
3
11 14 18 23 29 36 44 45 53 64
15
```

`microbuz.out`
```
163
2 3 4 7 10 
5 6 8 9
```

## Explanation

The task is $3$. The highest common price is $163$.
Set $1$: tickets priced at $14 \ 18 \ 23 \ 44 \ 64$.
Set $2$: tickets priced at $29 \ 36 \ 45 \ 53$.