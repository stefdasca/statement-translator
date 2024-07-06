# Task
Given two matrices *șmechere de Calafat* denoted as `A` and `B`, transform matrix `B` into matrix `A` through row and column swaps.

# Input data
The file `transform.in` contains:  
- The first line contains the number `N`, representing the dimension of the matrix.  
- The next `2N` lines contain pairs of natural numbers separated by a space, representing the row and column of an element with value `1` in matrix `A`.  
- The following `2N` lines contain pairs of natural numbers separated by a space, representing the row and column of an element with value `1` in matrix `B`.

# Output data
The file `transform.out` will contain on each line one swap operation of two rows or two columns, encoded as a triplet `ch x y` consisting of a character `ch` and two natural numbers `x` and `y` separated by a space. The value of `ch` can be only `L`, `C` or `0`. If the value of `ch` is equal to `L`, then rows `x` and `y` will be swapped in matrix `B`. If the value of `ch` is equal to `C`, then columns `x` and `y` will be swapped in matrix `B`. The last triplet of values in the output file will be `0 0 0`, indicating the end of operations.

# Constraints and clarifications
* $1 \ \leq N \ \leq 80\ 000$
* For a program that fits within the execution time, the score depends on the number of operations printed to the output file. Let `op` be the number of operations performed. Thus, for each correct output file, the score is awarded as follows:
  * if $1 \ \leq op \ \leq 2N$, `100%` of the score is awarded;
  * if $2N+1 \ \leq op \ \leq 4N$, `75%` of the score is awarded;
  * if `op > 4N`, `50%` of the score is awarded.
* There exists a solution for all input tests.

# Example

`transform.in`
```
4
1 1
2 2
3 3
4 1
3 4
4 4
2 3
1 2
1 3
2 3
1 1
2 2
4 2
4 4
3 4
3 1
```

`transform.out`
```
L 3 4
C 3 2
0 0 0
```

Explanation
---

`N=4`  
Firstly, we read matrix `A`:
```
1 1 0 0
0 1 1 0
0 0 1 1
1 0 0 1
```
then we read matrix `B`:
```
1 0 1 0
0 1 1 0
1 0 0 1
0 1 0 1
```
We apply the operation `L 3 4` swapping rows `3` and `4` in matrix `B`:
```
1 0 1 0
0 1 1 0
**0 1 0 1** 
1 0 0 1
```

We apply the operation `C 3 2` swapping columns `3` and `2` in matrix `B`: 
```
1 **1 0** 0 
0 **1 1** 0
0 **0 1** 1 
1 **0 0** 1
```

Reading the line `0 0 0` we understand that the operations have ended and matrix `A` has been obtained.