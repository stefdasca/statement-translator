In the country of Utopia, a digital revolution recently took place, as a result of which it was decided to interrupt mobile phone services. Fortunately, Miruna infiltrated the headquarters of the main telephony provider in Utopia. To restore the network, Miruna needs to pass an authentication filter: in front of her, there is a square matrix of dimension `N` with elements from the set `{0, 1}`. The following operations can be performed on this matrix:
- Two rows are chosen and swapped;
- Two columns are chosen and swapped.

To pass the authentication filter, Miruna needs to obtain values equal to 1 on the main diagonal (all elements of the form `A[i][i]`).

# Task
Determine for Miruna a sequence of at most `4*N` operations so that she manages to pass the authentication filter.

# Input data
The input file `revolutie.in` will contain the number `N` on the first line, representing the dimension of the matrix. The next `N` lines contain `N` values from the set `{0, 1}` representing the values of the matrix.

# Output data
The output file `revolutie.out` will contain a single integer `T` on the first line representing the number of operations performed. Each of the following `T` lines will describe an operation: the first character on the line will be `L` if an operation on the rows was applied and `C` if an operation on the columns was applied. There will be two values between `1` and `N` representing the indices of the swapped rows/columns. If there is no solution, the value `-1` will be displayed.

# Constraints and clarifications
* `1 \leq N \leq 127`
* Rows and columns are numbered from `1` to `N`
* `T` must belong to the interval `[0, 4*N]`
* `30%` of the test files will have `1 \leq N \leq 10`
* If there are multiple solutions, any of them will be displayed
* Miruna opposes the phenomenon of "politically correctness"

# Example

`revolutie.in`
```
2
0 1
1 0  
```

`revolutie.out`
```
1
L 1 2  
```

Explanation
---

By swapping the first two rows we obtain the matrix:
```
1 0
0 1
```