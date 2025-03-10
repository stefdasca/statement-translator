Dealul Bucium is known for its centuries-old tradition of vine cultivation. Long ago, noble and hybrid vine stocks were planted there on a rectangular-shaped land. Unfortunately, during rainy years, the vines are attacked by a fungal disease called plasmopara, which only affects hybrid varieties. Each new rainy day, plasmopara attacks the neighboring stocks (to the north, east, south, and west) of already infected stocks. The stocks attacked on the first rainy day are those in the corners of the land, being the most exposed.

# Task

Knowing the number of rows of vines and the number of stocks on each row, knowing the number of rainy days and the layout of the varieties on the land, determine:

1. The number of hybrid stocks that remain unaffected by plasmopara.
2. The day on which the most stocks were affected (if no stock was affected, the result will be $0$; if there are multiple days with the maximum number of affected stocks, the first of these will be determined).

# Input Data

The input file `plasmopara.in` contains on the first line the number $C$ representing the task ($1$ or $2$), on the second line the numbers $n$, $m$, and $z$, separated by a space, representing the number of rows of vines, the number of stocks on each row, and the number of rainy days, respectively. The next $n$ lines each contain $m$ numbers, where the character `-` represents a hybrid stock and the character $N$ represents a noble stock.

# Output Data

On the first line of the output file `plasmopara.out`, for task $C = 1$, write the number of stocks unaffected by the disease, and for task $C = 2$, a number representing the day on which the most stocks were affected.

# Constraints and Clarifications

* $1 \leq n, m, z \leq 200$;
* For tests worth $50$ points, the task will be $C=1$, and for tests worth $40$ points, the task will be $C=2$;
* $10$ points are awarded by default.

# Example 1

`plasmopara.in`
```
1
4 5 4
----N
-N---
-----
-N--N
```

`plasmopara.out`
```
6
```

## Explanation

The task is $1$. We have marked the stocks affected by plasmopara with numbers, corresponding to the day on which they were affected:

```
1234N
2N4--
234--
1N--N
```

# Example 2

`plasmopara.in`
```
2
4 5 4
----N
-N---
-----
-N--N
```

`plasmopara.out`
```
2
```

## Explanation

The task is $2$. The days with the maximum number of affected stocks are $2$ and $4$, so the first one is displayed.

```
1234N
2N4--
234--
1N--N
```

# Example 3

`plasmopara.in`
```
1
2 3 1
N-N
N--
```

`plasmopara.out`
```
2
```

## Explanation

The task is $1$. Only the stock in the bottom right corner is affected.

```
N-N
N-1
