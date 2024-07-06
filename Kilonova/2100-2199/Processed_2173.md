Tractorel thought for a bit, a bit about a problem while it was raining addresses on a morning. He is seriously thinking about an array of $N$ integers having dollars on the left and heavy lions on the right.

Because Tractorel gains supernatural powers, he can perform the following operations on the array.

* `Insert (X Y)` – inserts the element with value $Y$ into the array after the element at position $X$ (if $X$ is $0$, $Y$ is inserted at the beginning of the array)
* `Delete K` – removes the element at position $K$ from the array
* `Query`

Tractorel considers an array to have the Wonder property if all elements of the array of partial sums starting from the first element are non-negative.
For the Query operation, Tractorel kindly asks you to determine a circular permutation of the array so that it has the Wonder property. For example, if we have the array $S = [1, -1, 2, 5]$, it can be permuted circularly into the arrays $S_0 = [1, -1, 2, 5]$, $S_1 = [-1, 2, 5, 1]$, $S_2 = [2, 5, 1, -1]$, $S_3 = [5, 1, -1, 2]$ and the array of partial sums associated with these arrays will be: $S_0^{'} = [1, 0, 2, 7]$, $S_1^{'} = [-1, 1, 6, 7]$, $S_2^{'} = [2, 7, 8, 7]$, $S_3^{'} = [5, 6, 5, 7]$. It is observed that the arrays $S_0, S_2, S_3$ have the Wonder property.

Tractorel, being modest, only wishes to display a single number for the Query operation, specifically how many positions the array $S$ needs to be circularly permuted to the left for it to have the Wonder property. A correct answer to a Query operation on $S = [1, -1, 2, 5]$ is $3$ because the array obtained by circularly permuting $S$ three times to the left is $S_3$, which is a Wonder array.
**If there is no Wonder array among all circular permutations of the array, $-1$ will be displayed.**

# Task
For an array initially containing $N$ integers and $M$ operations of the types `Insert (X Y)`, `Delete K`, `Query`, the main character wishes to display the answer to all Query questions.

# Input data

In the input file `rotatii.in`, the first line contains $2$ integers $N$ and $M$, and the second line contains $N$ integers. After the second line, there are $M$ lines, representing the operations encoded as follows:

* `0 X Y` - `Insert (X, Y)`
* `1 K` - `Delete`
* `2` - `Query`

# Output data

In the output file `rotatii.out`, the answer to each query will be displayed, one number on a line representing the number of positions needed to rotate the array or $-1$ if there is no solution.

# Constraints and clarifications

* $1 \leq N \leq 100\ 000$
* $1 \leq M \leq 100\ 000$
* $0 \leq X, K \leq$ the current number of elements in the array
* The array contains integers in the range $[-10^9, 10^9]$

# Example

`rotatii.in`
```
4 6
2 -3 5 2
0 4 -100
2
1 5
2
0 1 -4
2
```

`rotatii.out`
```
-1
3
3
```

## Explanation

At the first query, the array has the form $2\ -3\ 5\ 2\ -100$ and for no circular permutation do we have the Wonder property. Continue the analysis :)