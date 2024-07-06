In every day, the 7 dwarfs work diligently in their mine to collect as many diamonds as possible. The mine can be represented as a square matrix with side length $N$, with each element of the matrix containing a known number of diamonds. The dwarfs have purchased a special machine to assist them in their work. With its help, diamonds can be collected in two ways. The first method, called **primary collection**, involves collecting diamonds on $K$ adjacent diagonals parallel to the main diagonal of the matrix; the second method, called **secondary collection**, involves collecting diamonds on $K$ adjacent diagonals parallel to the secondary diagonal of the matrix. The dwarfs can use the machine only once for one type of collection. After a collection, the affected elements no longer contain diamonds.

Since they do not yet know how to use the machine to its maximum capacity, the dwarfs need your help!

# Task

Write a program to help the dwarfs determine:
1. The maximum number of diamonds that can be collected in a primary collection;
2. The maximum number of diamonds that can be collected in a secondary collection;
3. The maximum number of diamonds the dwarfs can collect from the mine.

# Input data

The input file `diamante.in` contains on the first line the number $C$, which can only be $1$, $2$ or $3$.

The second line of the file contains the natural numbers $N$ and $K$. Each of the following $N$ lines contains $N$ natural numbers, representing the number of diamonds in each cell.

# Output data

If $C=1$, the output file `diamante.out` will contain a natural number representing the maximum number of diamonds that can be collected in a primary collection.

If $C=2$, the output file `diamante.out` will contain a natural number representing the maximum number of diamonds that can be collected in a secondary collection.

If $C=3$, the output file `diamante.out` will contain a natural number representing the maximum number of diamonds that can be collected from the mine using the machine.

# Constraints and clarifications

* $1 \leq N \leq 500$
* $1 \leq K < 2 \cdot N$
* In any cell, there are at most $5\ 000$ diamonds.
* For $15$ points, $C = 1$.
* For another $15$ points, $C = 2$.
* For another $20$ points, $C = 3$ and $K = 1$.

# Example 1

`diamante.in`
```
1
10 3
2 1 6 4 5 8 8 9 3 5
5 8 7 7 3 1 9 3 3 9
5 2 5 6 8 8 1 2 8 3
2 4 8 8 5 3 9 7 4 9
3 2 5 8 7 7 3 4 4 8
1 2 8 3 3 9 3 4 1 8
6 5 5 2 5 6 6 1 1 4
2 1 9 9 1 7 4 4 5 5
1 7 9 4 9 4 5 4 5 3
7 7 7 9 5 5 3 5 8 4
```

`diamante.out`
```
145
```

## Explanation

The maximum number of diamonds obtained after a primary collection is $145$.

~[img1.jpg|width=27em]

# Example 2

`diamante.in`
```
2
10 3
2 1 6 4 5 8 8 9 3 5
5 8 7 7 3 1 9 3 3 9
5 2 5 6 8 8 1 2 8 3
2 4 8 8 5 3 9 7 4 9
3 2 5 8 7 7 3 4 4 8
1 2 8 3 3 9 3 4 1 8
6 5 5 2 5 6 6 1 1 4
2 1 9 9 1 7 4 4 5 5
1 7 9 4 9 4 5 4 5 3
7 7 7 9 5 5 3 5 8 4
```

`diamante.out`
```
152
```

## Explanation

The maximum number of diamonds obtained after a secondary collection is $152$.

~[img2.jpg|width=27em]

# Example 3

`diamante.in`
```
3
10 3
2 1 6 4 5 8 8 9 3 5
5 8 7 7 3 1 9 3 3 9
5 2 5 6 8 8 1 2 8 3
2 4 8 8 5 3 9 7 4 9
3 2 5 8 7 7 3 4 4 8
1 2 8 3 3 9 3 4 1 8
6 5 5 2 5 6 6 1 1 4
2 1 9 9 1 7 4 4 5 5
1 7 9 4 9 4 5 4 5 3
7 7 7 9 5 5 3 5 8 4
```

`diamante.out`
```
274
```

## Explanation

The maximum number of diamonds that can be collected is $274$.

~[img3.jpg|width=27em]