
# Task

A matrix with $n$ rows and $n$ columns, consisting of natural elements, is given. The rows of the matrix are ordered in ascending order. A number of $k$ operations of the following type are applied: Two rows $L_1$ and $L_2$ are given. The elements of row $L_1$ will be replaced with the smallest $n$ values among the $2n$ values of the rows $L_1$ and $L_2$. These elements are placed in ascending order. The task is to display the matrix after applying all the operations.

# Input data

The first line of the file `mins.in` contains the number $n$.  
The next $n$ lines contain $n$ numbers each, arranged in ascending order, separated by spaces, representing the elements of the matrix.  
The following line contains the value $k$.  
The next $k$ lines contain $2$ values separated by space, $L_1$ and $L_2$.

# Output data

The file `mins.out` contains $n$ lines with $n$ values each, separated by spaces, representing the final matrix.

# Constraints and clarifications

* $2 \leq n \leq 1 \ 000$;
* $1 \leq k \leq 10 \ 000$;
* The elements of the matrix are natural numbers with at most $6$ digits;
* $1 \leq L_1, L_2 \leq n$;
* $L_1 \neq L_2$.

# Example

`mins.in`
```
3
1 2 3
1 3 5
3 3 4
1
3 2
```

`mins.out`
```
1 2 3
1 3 5
1 3 3
```
