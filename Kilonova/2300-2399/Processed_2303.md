In the wake of a shady deal with the mobster Ivan, Lunasorab suffered a suspicious car accident. As a result, he is facing temporary memory loss. This is very unfortunate because he needed to inventory his chicken farms. These have the shape of a right isosceles triangle, with the legs parallel to the coordinate axes. More precisely, the area where Lunasorab's farms are located can be modeled as a square matrix of $N$ rows and $N$ columns (with rows and columns numbered from $1$ to $N$) of natural numbers, representing the intelligence coefficient of a chicken. A right isosceles triangle with legs of length $L$ with the origin at row $x$ and column $y$ will contain all cells in the matrix from row $a$ and column $b$ with $a \leq x$ and $b \geq y$ and with $|a - x| + |b - y| < L$.

For Lunasorab, the risk degree of a farm (represented as a right isosceles triangle defined as above) is given by the minimum value of the intelligence coefficient of a chicken on that farm.

Since Lunasorab is currently not doing well with his memory, he asks you to find the sum of the risk degrees of all the farms modulo $1 \ 000 \ 000 \ 007$.

# Task

Help Lunasorab quickly find the sum of the risk degrees of all his farms.

# Input data

The first line of the input file `nomem.in` contains the numbers $N$ and $Q$, separated by a single space, representing the dimensions of the matrix, respectively the number of Lunasorab's farms. The next $N$ lines, each containing $N$ elements, contain the elements of the matrix, separated by a single space. The next $Q$ lines contain $3$ numbers $L \ x \ y$, separated by a single space representing the farm with the origin at $x \ y$, with a leg length of $L$.

# Output data

The output file `nomem.out` will contain a natural number, representing the sum of the risk degrees of all the farms modulo $1 \ 000 \ 000 \ 007$.

# Constraints and clarifications

* $1 \leq N \leq 1 \ 000$
* $1 \leq Q \leq 1 \ 000 \ 000$
* $1 \leq x, y, L \leq N$
* A farm is entirely located within the matrix
* $0 \leq$ intelligence coefficient of a chicken $< 1 \ 010 \ 010 \ 010$
* In the input file, the queries will be sorted in ascending order by $L$
* There may be chickens that do not belong to any of Lunasorab's farms
* For $20\%$ of the tests $N = 200$ and $Q = 100\ 000$
* For another $20\%$ of the tests $N = 300$ and $Q = 400 \ 000$
* For another $20\%$ of the tests $N = 700$ and $Q = 1 \ 000 \ 000$
* Lunasorab recommends parsing the input quickly to have more time to help him

# Example

`nomem.in`
```
3 3
1 2 3
4 5 6
7 8 9
1 2 3
2 3 2
3 3 1
```

`nomem.out`
```
12
```

## Explanation

For the first query, the answer is $6$, for the second $5$, and for the last $1$. If we add them up and take the remainder modulo $1 \ 000 \ 000 \ 007$, we get $12$.