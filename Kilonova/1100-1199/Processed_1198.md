It is considered a two-dimensional array with $m$ rows and $n$ columns. A V-route is defined as a traversal through the elements of the array such that:

- It always starts from an element on the first row of the array and ends at another element on the first row of the array, passing through at least 3 elements, without passing through any element more than once.
- The traversal of the elements of the array is done in the shape of a single letter V as shown in the drawing, being able to move from one element to another only to an immediately adjacent element on the diagonal.

Each element of the array contains integer values. The sum of the elements on the route is calculated during the traversal.

# Task

Determine the V-route that contains the largest sum. If there are multiple routes with the same sum, the route that passes through the fewest cells will be chosen. If there are still multiple solutions, the leftmost route will be chosen (the one with the smallest starting column index).

# Input data

From the input file `v.in` we read:
- The first line contains two natural values $m$ and $n$ separated by a space, representing the number of rows and columns of the array.
- The following $m$ lines contain the values of the elements of the array on each line, values separated on each line, two by two, by a space.

# Output data

The output file `v.out` will contain a single line containing three natural values representing the sum of the values of the elements of the array for the chosen route, the starting column, and the row on which the peak of the V is located.

**Attention!** The data in the output file must be in the order specified above (sum, column, row).

# Constraints and clarifications

* $1 \leq m, n \leq 100$
* $-60\ 000 \leq$ the values of the elements of the array $\leq 60\ 000$

According to the input data, the sum of the values of any route does not exceed $10^9$.

# Example 1

`v.in`

```
5 9
3 4 12 4 6 7 9 5 12
0 4 5 7 9 -5 1 1 5
0 98 34 0 1 7 7 1 1
6 7 8 -9 0 2 3 5 22
47 62 31 55 0 83 23 77 10
```

`v.out`

```
54 1 3
```

## Explanation

Examples of other routes that can be created according to the above data, but which have a smaller sum than the result:

~[pozacvpb.png]

