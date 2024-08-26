# Elections

Since this year there are presidential elections, the leaders of the country have decided to repair some highways in $Wonderland$ so that it is possible to travel from any city to any other city, using only highways that are not broken. Given the list of highways, as well as the list of broken highways, you need to tell the $President$ what is the minimum amount of money that needs to be spent to make everyone happy and win the elections, knowing that the $N$ cities in $Wonderland$ are encoded with natural numbers between $1$ and $N$ .

## Input data

The input file `$alegeri.in$` contains on the first line $T$, representing the number of tests. A test contains on the first line $N$ and $M$ representing the number of cities and respectively the number of highways in $Wonderland$. On the following $M$ lines, the highways are described, in one of the following forms: $0$ $a$ $b$ - which means that there is a highway between cities $a$ and $b$ $1$ $a$ $b$ $c$ - which means that between $a$ and $b$ there is a highway whose repair costs $c$ lei.

## Output data

In the output file `$alegeri.out$` will contain $T$ numbers, representing the response for the $T$ tests. If there is no solution for a test, it will print $-1$ .

## Constraints

$T = 7$

$1 \leq N \leq 100\ 000$

$1 \leq M \leq 200\ 000$

The cost of a road is a positive number and does not exceed $5000$

Attention! Highways are two-way roads with at least two lanes in each direction.

## Example

`alegeri.in`

```
2
2 1
1 1 2 10
2 2
0 1 2
1 1 2 10
```

`alegeri.out`

```
10
0
```

## Explanation

In the first example in $Wonderland$ there are only two cities, and a broken highway between them. Thus, the repair cost is $10$.

In the second example, there is a functional highway and a broken highway between the two cities. Thus, the $President$ does not need to allocate any money, as people have a way to travel and are happy.