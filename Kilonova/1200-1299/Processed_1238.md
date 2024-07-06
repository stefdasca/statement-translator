On the highway "Soarele Estului", billboards of various companies are placed along the road at equal distances. The same company may have multiple billboards and each billboard may appear in multiple places. Billboards are identified by natural numbers, with the total number of billboards being $N$. The company "X Corporation" has $T$ different types of billboards. The company has received approval to build a large tourist complex near the highway; therefore, for choosing the location, it is also interested in the following aspect: what is the minimum length of road in which all $T$ types of the company's billboards can be found, regardless of their order and irrespective of whether billboards of other companies are interspersed.

# Task

Given $N$ - the total number of billboards along the highway and their order of placement, and the $T$ types of billboards placed by the company, determine the minimum number of intervals between two billboards in which the company "X Corporation" can find all its billboards.

# Input data

The input file `panouri.in` contains on the first line the numbers $N$ and $T$. The next $N$ lines contain $N$ natural numbers, not necessarily different, one number per line, representing the billboards. Starting from line $N + 2$, each line contains one of the $T$ different types of the company's billboards.

# Output data

The output file `panouri.out` will contain on the first line a single positive integer $L$, representing the required number, or $-1$ in case there is no solution.

# Constraints and clarifications

* $1 \leq N \leq 15 \ 000$;
* $1 \leq T \leq 1 \ 000$;
* All numbers representing billboards are natural numbers in the interval $[1 \dots 1000]$.

# Example 1

`panouri.in`
```
6 2
1
2
3
5
3
1
5
1
```

`panouri.out`
```
2
```

## Explanation

There are $N$ = $6$ billboards: $1 \ 2 \ 3 \ 5 \ 3 \ 1$. The company has $T$ = $2$ types of billboards: $5$ and $1$. The shortest interval containing the elements $5$ and $1$ is between the 4th and the 6th billboards and contains $2$ intervals.

# Example 2

`panouri.in`
```
8 3
5
1
3
3
5
4
2
1
3
1
4 
```

`panouri.out`
```
4
```

## Explanation

There are $N$ = $8$ billboards of types: $5 \ 1 \ 3 \ 3 \ 5 \ 4 \ 2 \ 1$. The company has $T$ = $3$ types of billboards: $3$, $1$ and $4$. The shortest interval containing the elements $1$, $3$ and $4$ is between the 2nd and the 6th billboard and contains $4$ intervals.