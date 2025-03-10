# Task

The map of an island is encoded in the form of a matrix with $n$ rows and $m$ columns containing natural number values. The $n \times m$ cells represent land, and the sea surrounds the matrix. Any cell is identified by a pair $(i,j)$ indicating the row and column it occupies. The rows are numbered from $1$ to $n$, and the columns from $1$ to $m$. Two cells are considered neighbors if they are next to each other on the same row or the same column.

We define a *country* as a maximal group of cells that have the same value and between which you can move from one cell to another neighboring cell once or more times.

An "enclave" is a country that has only one neighbor. If the country is also a neighbor with the sea, it is no longer considered an enclave. A country that contains an enclave is called an "enclosing country".

If two or more countries, by joining, form an enclave, the country that surrounds them is also considered an enclosing country (by joining, we imagine that all the cells of the countries that unite receive the same value, one of them).

The problem asks us to answer queries specifying a country (through one of its cells) and asking if it is enclosing or not.

# Input data

The file `enclava.in` contains on the first line two natural numbers $n$ and $m$ as described above.  
On the next $n$ lines are $m$ numbers, separated by spaces, describing the island.  
The next line contains a value $k$ representing the number of queries.  
On each of the following lines are two values representing, respectively, the row and column of a cell.

# Output data

The file `enclava.out` contains on the first line, $k$ values of $0$ and $1$, unseparated by space, representing the result of the query for the country containing the corresponding cell given in the input file.

# Constraints and clarifications

* $3 \leq n \leq 100$;
* $3 \leq m \leq 100$;
* $1 \leq k \leq 1 \ 000$;
* The matrix values are single-digit natural numbers.

# Example

`enclava.in`
```
6 7
0 0 0 0 0 0 0
0 1 1 1 1 1 0
0 1 2 3 3 1 1
0 1 2 2 1 1 0
0 1 1 1 1 4 4
0 0 0 0 0 4 3
6
2 3
3 3
3 4
5 3
6 6
6 7
```

`enclava.out`
```
100100
```

## Explanation

We have two countries coded with the value $0$, one country coded with the value $1$, one coded with the value $2$, one coded with the value $4$, and two coded with the value $3$.

The country coded with $1$ is an enclosing country (the countries coded with $2$ and $3$ (the one above) by joining form an enclave surrounded by it). The country coded with $4$, the country coded with $3$ in the bottom right, and those coded with $0$ are not enclosing.