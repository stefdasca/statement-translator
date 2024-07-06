# Task

Little Gates went to the jewelry store to make a mărțișor. He has $n$ beads which he wants to arrange in the shape of a triangle such that each row $i$ of the triangle (starting with $1$) contains exactly $i$ beads, _all of the same value_. It is known how much each of the beads he has is worth and he wants the mărțișor to also meet the following condition: the value of any bead must be equal to the sum of the values of the two below it.

Determine if it is possible to create a mărțișor using all the given beads. If so, display their values, in the order of the triangle, from top to bottom. Otherwise, display the sum of the values of the beads on a mărțișor that can be formed with some of them and that has this sum of values (denoted by us further as $S$) maximally.

# Input data

The file `martisor.in` contains on the first line a number $n$. The second line contains $n$ numbers separated by space, representing the values of the beads.

# Output data

The file `martisor.out` contains the result as follows: if a mărțișor can be formed with all the given values, the file will contain on line $i$ the components of line $i$ of the triangle (numbers separated by space). In the other case, the output file will contain a single number, $S$.

# Constraints and clarifications

* $2 \\leq N \\leq 1 \\ 000 \\ 000$;
* The values of the numbers are between $1$ and $1 \\ 000 \\ 000$, inclusive.
* For $41$ points, $n \\leq 1 \\ 000$;
* A mărțișor must consist of at least two lines. It is guaranteed that the input data ensures the creation of such a mărțișor.

# Example 1

`martisor.in`
```
6
3 6 3 12 6 3
```

`martisor.out`
```
12
6 6
3 3 3
```

## Explanation

We imagine the numbers arranged one below the other as follows:
```
   12
  6   6
3   3   3
```

# Example 2

`martisor.in`
```
14
1 1 1 2 2 4 4 3 3 6 6 6 1 18
```

`martisor.out`
```
12
```

## Explanation

It is not possible to form a mărțișor with all the numbers. Several mărțișors can be formed with some of the numbers. Some of them are:
```
 2
1 1
```
or
```
  4
 2 2
1 1 1
```
or
```
 6
3 3
```
The last solution seen above has the maximum sum, $12$.