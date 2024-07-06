Boris is a successful businessman with contracts that bring both income (interest, commissions, etc.) and tax obligations (taxes, rates, etc.).

Boris decided to visit an office building. The building has a single level where the offices are adjacent to each other, forming a square grid of size $N \times N$. The office plan can be represented as a square matrix where the offices are elements of the matrix with rows and columns numbered from $1$ to $N$. Specifically, at row $i$ and column $j$ there is the office $(i, j)$.

Boris will enter the building through office $(1, 1)$ and pass through a series of offices. The route will end in office $(N, N)$. Moving from one office to another is allowed:
* on the same row only from left to right: $(i, j) \rightarrow (i, j + 1)$;
* on the same column only from top to bottom: $(i, j) \rightarrow (i + 1, j)$;
* diagonally in the following two directions:
  - $(i, j) \rightarrow (i + 1, j − 1)$, but also
  - $(i, j) \rightarrow (i − 1, j + 1)$.

However, **Boris will never return to an office he has left.**

Each time Boris visits office $(i, j)$ he signs a contract worth $B(i, j)$ lei. If $B(i, j) > 0$, he receives $B(i, j)$ lei, and if $B(i, j) < 0$, he pays $−B(i, j)$ lei. Boris's goal is to leave the building with the maximum total profit. The profit is defined as the total money received minus the total money paid on the route.

**Attention!** The profit can also be negative if Boris pays more than he receives.

# Task

Knowing the office plan and the values $B(i, j)$ for $1 \leq i, j \leq N$ awaiting Boris in each office, help him calculate the maximum profit he can have upon leaving the building.

# Input data

The input file `birocratie.in` contains on the first line the number $N$, and on the following $N$ lines $N$ integers separated by spaces, representing the values $B(i, j)$ for $1 \leq i, j \leq N$.

# Output data

The output file `birocratie.out` will contain a single line with a single integer representing the maximum possible profit.

# Constraints and clarifications

* $5 \leq N \leq 1 \ 000$;
* $-1 \ 000 \leq B(i, j) \leq 1 \ 000$ for $1 \leq i, j \leq N$.

|# | Points | Constraints|
| - | - | ------------|
|1|12|$B$ has all positive elements, $N \leq 300$.|
|2|12|$B$ has all equal and negative elements, $N \leq 300$.|
|3|15|On each diagonal parallel to the secondary diagonal the elements in $B$ are equal, $N \leq 300$.|
|4|13|The elements on the border of $B$ are negative, and the other elements are positive, $N \leq 300$.|
|5|13|All elements in $B$ are equal in absolute value (modulus), the elements on the border are positive, and the other elements are negative, $N \leq 300$.|
|6|16|$N \leq 300$|
|7|19|Without additional constraints.|

Above, by *border* of $B$ we mean the elements that are on the first/last row and the first/last column.

# Example

`birocratie.in`
```
5
1 2 5 8 2
1 3 -10 2 1
0 9 1 -7 3
-2 3 4 -1 2
3 -4 2 3 1
```

`birocratie.out`
```
42
```

## Explanation

The maximum profit is 42, obtained by summing the highlighted elements in the route illustrated below.

~[birocratie_ex.png|width=25em]