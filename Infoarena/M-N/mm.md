Mm

Consider an $N \times N$ matrix (with $N$ rows and $N$ columns, numbered from $1$ to $N$). Inside this matrix, there are $P$ rectangular zones. For each such zone $i$ ($1 \leq i \leq P$), the following $5$ parameters are known: $l_{sus}(i)$, $c_{stanga}(i)$, $l_{jos}(i)$, $c_{dreapta}(i)$, and $cost(i)$. The rectangular zone $i$ covers all matrix cells at coordinates (row, column), for which $l_{sus}(i) \leq row \leq l_{jos}(i)$ and $c_{stanga}(i) \leq column \leq c_{dreapta}(i)$. $cost(i)$ represents the cost of rectangular zone $i$. The goal is to place a square with side $L$ strictly inside the given matrix. A square with side $L$ occupies an area inside the matrix having $L$ rows and $L$ columns. The cost of placing the square is equal to the maximum cost of the rectangular zones it intersects (if it does not intersect any zone, its cost is $0$). Determine the minimum cost of placing a square with the given side $L$ strictly inside the matrix.

## Input data

The input file `mm.in` contains on the first line $3$ integers, separated by spaces: $N$, $L$, and $P$. The next $P$ lines describe a rectangular zone. The $i$-th of these lines contains $5$ integers, separated by spaces: $l_{sus}(i)$, $c_{stanga}(i)$, $l_{jos}(i)$, $c_{dreapta}(i)$, and $cost(i)$.

## Output data

The output file `mm.out` will contain a single number, representing the minimum cost of placing the square inside the matrix.

## Constraints and clarifications

$1 \leq N \leq 250\ 000$  
$1 \leq L \leq N$  
$1 \leq P \leq 100\ 000$  
$1 \leq l_{sus}(i) \leq l_{jos}(i) \leq N$  
$1 \leq c_{stanga}(i) \leq c_{dreapta}(i) \leq N$  
$1 \leq cost(i) \leq 2\ 000\ 000\ 000$  

## Example

`mm.in`  
```
10 5 3  
2 2 7 7 10  
6 7 9 7 20  
3 4 6 10 13  
```

`mm.out`  
```
13  
```

## Explanation

The square can be placed with its top-left corner at cell $(1, 1)$. Thus, it intersects rectangular zones $1$ and $3$, with its cost being $max(10, 13) = 13$.