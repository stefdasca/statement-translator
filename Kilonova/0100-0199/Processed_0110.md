Sure, here is the translated and reviewed competitive programming problem statement:

----

A singly linked list `(L1)` containing integers from `1` to `N` (in any random order) is given. The task is to construct another singly linked list `(L2)` which contains the numbers from list `L1` in ascending order. To obtain the list `L2`, elements will be removed from `L1` and added to `L2` as described below: initially, the list `L2` is empty. At the first step, we can remove any element from `L1` and add it to `L2`. Then, in the next `N - 1` steps, we can remove any element from `L1`, but it can only be added either at the beginning or at the end of `L2`. At the end, `L1` will no longer contain any elements, and `L2` must contain the numbers from `1` to `N` in ascending order. Since there are multiple ways to construct `L2`, we will define the construction cost of `L2` and aim to determine a possible construction of `L2` that has the minimum cost.

The construction algorithm of `L2` consists of `N` steps, at each step removing an element from `L1` and adding this element to `L2` (following the specified restrictions). At step `i` (`1 <= i <= N`), list `L1` contains `N - i + 1` elements and list `L2` contains `i - 1` elements. If the element from position `k` in `L1` is moved to `L2` at step `i` (`1 <= k <= N - i + 1`), the cost of this move is equal to `k * i`. After moving the element, list `L1` will have one less element (all elements at positions greater than `k` will advance one position forward) and list `L2` will have one more element. The total construction cost of `L2` is equal to the sum of the costs of moves made at each of the `N` steps.

# Input data
The input file `lsort.in` contains:
- The first line contains the number `N`, representing the number of elements in `L1`.
- The next line contains the integers from `1` to `N`, separated by at least one space, in the order in which they are positioned in list `L1` (the first number is at position `1` in `L1`, the second number at position `2`, and so on).

# Output data
The output file `lsort.out` must contain:
- On the first line, print the minimum construction cost of `L2`.
- On the next line, print the construction method of `L2`. This line will display the order in which the elements are moved from list `L1` to list `L2`. The first number printed will represent the number moved from `L1` to `L2` at the first step; the second number will represent the number moved at step `2`, and so on. The numbers printed must be separated by at least one space. If there are multiple ways to construct the list `L2` with the minimum cost, any of them can be printed.

# Constraints and clarifications
- `1 <= N <= 1000`

# Example

`lsort.in`
```
4
4 1 3 2
```

`lsort.out`    
```
15
3 4 2 1
```

`lsort.in`    
```
7
6 3 5 4 1 7 2
```

`lsort.out`
```
43
6 5 4 3 2 1 7
```

Explanations
---

For example 1:
* At step `1`, `L1 = [4, 1, 3, 2]` and `L2 = []`. Remove element `3` from `L1` (which is at position `3`) and add it to `L2`. The cost of this move is `3 * 1 = 3`.
* At step `2`, `L1 = [4, 1, 2]` and `L2 = [3]`. Remove element `4` from `L1` (which is at position `1`) and add it to `L2` (it is evident that this element must be added at the end of list `L2` and not at its beginning; otherwise, list `L2` would no longer be sorted). The cost of this move is `1 * 2 = 2`.
* At step `3`, `L1 = [1, 2]` and `L2 = [3, 4]`. Remove element `2` from `L1` (which is at position `2`) and add it to `L2` (again, the position where the element must be added is evident: at the beginning of list `L2`). The cost of this move is `2 * 3 = 6`.
* At step `4`, `L1 = [1]` and `L2 = [2, 3, 4]`. Remove element `1` from `L1` (which is at position `1`) and add it to `L2`. The cost of this move is `1 * 4 = 4`.
* The total construction cost of list `L2` is `3 + 2 + 6 + 4 = 15`.

