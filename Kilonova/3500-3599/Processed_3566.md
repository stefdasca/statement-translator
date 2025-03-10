Here is the translated text:

# Task

We have a matrix where we imagine each cell as a box that can hold paint. There are $k$ operations in which paint is added to the boxes. An operation specifies a submatrix of boxes. In each box in the submatrix, a unit of paint of the same color is added. Thus, there is a possibility to end up putting paint in a box multiple times. The paint used in a specific operation is of a totally different color from all types used so far. When paint is added to a box again, it mixes with the paint already existing there. Practically, the type of paint obtained in a box in the end is given by the types of paint used in each operation that affected that box. By mixing, a paint type is always obtained that is different from all types of paint used in individual operations and from other types of paint obtained by mixing with a different color structure. We need to determine how many distinct types of paint are obtained.

# Input data

The file `color.in` contains on the first line the number $n$ representing the size of the matrix and the number $k$ representing the number of operations. Each of the next $k$ lines contains four numbers, describing an operation, with the structure: $L_1 \\ C_1 \\ L_2 \\ C_2$. These numbers represent, in order: the row and column of the top-left corner of the affected submatrix and the row and column of the bottom-right corner.

# Output data

The file `color.out` contains the number of distinct colors found at the end in the matrix boxes.

# Constraints and clarifications

* $1 \leq k \leq 150$;
* $1 \leq L_1 \leq L_2 \leq n$;
* $1 \leq C_1 \leq C_2 \leq n$;
* $1 \leq n \leq 1000$;
* It is guaranteed that each box is affected by at most $6$ operations;
* Initially, all boxes are empty;

# Example

`color.in`
```
3 4
1 1 2 2
2 2 3 3
3 1 3 3
2 3 2 3
```

`color.out`
```
5
```

## Explanation

The distinct colors obtained in the boxes are: $(a)$, $(a,b)$, $(b,e)$, $(c)$, $(b,c)$.

| | | |
|-|-|-|
|$(a)$|$(a)$| |
|$(a)$|$(a, b)$|$(b, e)$|
|$(c)$|$(b, c)$|$(b, c)$|