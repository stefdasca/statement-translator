The panda bear reserve, viewed from above, has a rectangular shape and is composed of $n$ identical rows, with each row containing $m$ identical square-base enclosures. The enclosures are fenced and come with doors to all $4$ neighboring enclosures. The doors are equipped with access codes, so they automatically open and close. Through this system, some enclosures are accessible to the panda bears, while others are off-limits to them. In $T$ enclosures, food is available for the panda bears.

The panda bears in the reserve carry a microchip that automatically opens the doors of enclosures they can enter and closes the doors of forbidden enclosures. An enclosure is **accessible** to a panda bear if the last $S$ digits of the binary representation of its code are complementary to the last $S$ digits of the binary representation of the code $k$ on the microchip. (Example: for $S=8$, `11101011` and `00010100` are complementary).

A panda bear starts in an enclosure and gets hungry. The panda bear only moves parallel to the sides of the rectangle. Moving from one enclosure to another adjacent one takes one second.

# Task

Knowing the dimensions of the reserve $n$ and $m$, the access codes for each of the $n \cdot m$ enclosures, the coordinates of the $T$ enclosures with food, the coordinates $L$ and $C$ of the initial enclosure where the bear is, the code $k$ of its microchip, and the number $S$, determine:

1. The number $X$ of enclosures that have the property that the last $S$ digits in the binary representation of their code are complementary with the last $S$ digits in the binary representation of the code $k$ carried by the bear, except for the enclosure where it initially is.
2. The minimum number of seconds $Smin$ it takes to reach an enclosure with food as well as the number of food enclosures $nt$ it can reach in this minimum time.

# Input data

The input file `panda.in` contains:

- The first line contains a natural number $p$. For all input tests, the number $p$ can only be $1$ or $2$
- The second line contains three natural numbers $n$, $m$, and $T$ separated by spaces, with the meanings from the statement
- The third line contains four non-zero natural numbers $L$, $C$, $k$, and $S$, separated by spaces, with the meanings from the statement
- The next $T$ lines each contain two natural numbers representing the coordinates of the enclosures with food
- The next $n$ lines each contain $m$ natural numbers, separated by spaces, representing the access codes for the doors of the $n \cdot m$ enclosures of the reserve.

# Output data

If $p$ is $1$, **only solve point 1 of the task**. 

In this case, the output file `panda.out` will contain a single natural number $X$, representing the total number of accessible enclosures for the panda, excluding the enclosure in which it initially is.

If $p$ is $2$, **only solve point 2 of the task**. 

In this case, the output file `panda.out` will contain the natural numbers $Smin$ and $nt$, in this order, separated by a space.

# Constraints and clarifications

* $2 \leq n, m \leq 500$
* $1 \leq S \leq 8$
* $1 \leq T < n \cdot m$
* $0 \leq k < 10\ 000$
* $0 \leq$ value of codes $< 10\ 000$
* There is a solution for all problem tests, meaning that the bear can reach at least one of the enclosures with food.
* Food can also be found in inaccessible areas.
* Correct solution of the first task earns $20$ points, while the second task earns $80$ points.
* For $24\%$ of tests, it is guaranteed that $m \leq 50$ and $n \leq 50$.
* For $20\%$ of tests, it is guaranteed that $S=1$.
* Correct determination of $Smin$ earns $75\%$ of the test points, while correct determination of $nt$ earns $25\%$ of the test points.

# Example 1

`panda.in`
```
1
5 6 4
3 5 1 1
1 2 
5 1 
2 1
4 3
15 1278 3 1278 1278 1 
16 17 18 19 254 20
21 25 26 254 254 254
27 28 29 3 2 254
2 254 4 254 254 254
```

`panda.out`
```
19
```

## Explanation

$k=1$ and since $S=1$, only the last binary digit of $k$ must be different from the last binary digit of the enclosure code.

**Attention! Only task 1 is solved for this test.**

# Example 2

`panda.in`
```
2
5 6 4
3 5 1 1
1 2 
5 1 
2 1
4 3
15 1278 3 1278 1278 1 
16 17 18 19 254 20
21 25 26 254 254 254
27 28 29 3 2 254
2 254 4 254 254 254
```

`panda.out`
```
6 1
```

## Explanation

If we mark accessible enclosures with `1` and inaccessible ones with `0`, we obtain the following matrix:

~[0.png]

The panda is in the enclosure with coordinates $(3, 5)$ and can reach only one enclosure with food after $6$ seconds. This enclosure is at coordinates $(5, 1)$; the path taken is:
$(3, 5) \rightarrow (4, 5) \rightarrow (5, 5) \rightarrow (5, 4) \rightarrow (5, 3) \rightarrow (5, 2) \rightarrow (5, 1)$

**Attention! Only task 2 is solved for this test.**