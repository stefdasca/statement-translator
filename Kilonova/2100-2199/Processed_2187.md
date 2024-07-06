## Task

~[chipskylark.jpg|align=right|width=180px]

$N$ people are standing on the $Ox$ axis, for each person you have at your disposal two arrays of $N$ elements $d$ and $f$, where

$\displaystyle d_i = \text{distance of person } i \text{ from the origin} \\newline
f_i = \text{"beauty" of person } i$

The people are labeled such that the array $d$ is sorted in ascending order.

Each person wants to find their soulmate, so a compatibility index was created. Person $i$ is willing to travel at most $depmax_i$ meters to another person (including themselves), but for each meter traveled, the compatibility decreases by a global coefficient. Formally, the compatibility between two people is defined as follows:

$$
comp(i, j) = dist(i, j) \cdot (-coef) + f_j \text{ for } dist(i, j) \leq depmax_i \\newline
\text{where } dist(i, j) = \text{distance between person } i \text{ and person } j
$$

Display for each person who the suitable person is (the index of the person where the compatibility is maximized).

**Note**: It is guaranteed that the positions where they will move the most $^1$ (see constraints) are in ascending order. We can think that, the further away people are from the origin, the less motivated they are to travel that much.

## Input data

The first line of the input file `pofta.in` contains two natural numbers $N$ and $coef$. On the next $3$ lines are the arrays $d$, $f$, and respectively $depmax$, all with the meaning described in the task.

## Output data

The first line of the output file `pofta.out` will contain an array of $N$ natural numbers $c$ with the property that $comp(i, c_i)$ is maximum for each $i$ ($1 \leq i \leq N$ of course).

## Constraints and clarifications

* $1 \leq N \leq 1 \ 000 \ 000$;
* $0 \leq d_i, depmax_i, f_i \leq 10^{10}$
* $1 \leq coef \leq 1 \ 000$
* $^1$ Let $l_i$ and $r_i$ be the leftmost and rightmost positions that person $i$ will reach respectively: $l_i \leq l_{i+1}$ and $r_i \leq r_{i+1}$ for each $1 \leq i \lt N$
* For each $i$, $c_i$ is unique

## Example 1

`pofta.in`
```
5 1
2 6 9 13 14
9 14 10 7 14
5 3 1 2 3
```

`pofta.out`
```
2 2 3 5 5
```

## Explanation

The 5 people on the $Ox$ axis and their accessibility:

~[axa.png|align=center|width=min(700px,80%)]

The values $comp(i, j)$ are written in the table below, we leave the cells empty where $dist(i, j) > depmax_i$

|$_{i} \diagdown ^{j}$|1|2|3|4|5|
|---|-|-|-|-|-|
|1|9|10| | | |
|2| |14|7| | |
|3| | |10| | |
|4| | | |7|13|
|5| | | |6|14|

