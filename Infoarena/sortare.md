## Sorting

QuickSort is a well-known sorting algorithm. The algorithm works as follows:
- An element from the array is chosen, which will be called the $pivot$
- The array is reordered so that all elements with values less than the pivot are placed before the pivot, and elements with values greater than the pivot are placed after the pivot
- The two parts of the $array$ are recursively sorted

The base case of recursion is arrays of size $0$ or $1$.

We can implement this algorithm in pseudocode as follows:
```
function qsort(array[])
    var left[], right[], pivot
    if length(array) <= 1 
        return array
    pivot = an element from array
    for each x in array
        if x < pivot then insert x into left
        if x > pivot then insert x into right
    return concatenate(qsort(left), pivot, qsort(right))
```
Fumeanu implemented this algorithm and believes that his implementation is very efficient. Nargy is wiser and realizes that the performance of the entire algorithm depends on how the pivot is selected.

The method used by Fumeanu is as follows: for an array of length $i$ he chooses the median of the elements at positions $A_i$, $B_i$, and $C_i$ (the median is the middle element in size among the $3$).

Help Nargy find a permutation of the numbers from $1$ to $N$ for which Fumeanu's implementation has the maximum recursion depth.


## Input data

The input file `sortare.in` contains on the first line the number $N$. The next $N-1$ lines contain $3$ natural numbers $A_i$, $B_i$, $C_i$ separated by spaces ($2 \leq i \leq N$).


## Output data

The output file `sortare.out` will contain on the first line $HMax$ representing the maximum recursion depth. The next line will contain $N$ natural numbers representing a permutation of the numbers from $1$ to $N$ which achieves this depth.


## Constraints and clarifications

$1 \leq N \leq 5000$

$1 \leq A_i, B_i, C_i \leq i$

Positions in the array are indexed starting from $1$.

If there are multiple solutions, any of them can be displayed.


## Example

`sortare.in`
```
5
1 2 2
1 2 3
1 3 4
1 3 5
```

`sortare.out`
```
3
1 2 3 4 5
```


## Explanation

For the permutation $1\ 2\ 3\ 4\ 5$ the recursion has $3$ levels, as follows: The bolded elements are those used in determining the pivot, and the underlined ones represent the pivot. There is no permutation of length $5$ that produces a greater depth for the given input data.