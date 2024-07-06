Ion has a stack with `N` elements and wants to sort them in ascending order from the base to the top. To achieve this, he can purchase `M` additional stacks and perform `K` operations. An operation consists of taking an element from the top of one stack and inserting it into the top of another stack. Ion can conveniently choose the values of `M` and `K`. Help Ion sort the elements such that `M*K` has the smallest possible value and all values end up on the initial stack in ascending order from the base to the top.

# Task

Display a sequence of `K` operations using `M` additional stacks such that the elements on the initial stack are sorted in ascending order from the base to the top.

# Input data

The input file `aranjare.in` will contain:
1. The first line contains a non-zero natural number `N`.
2. The second line contains a permutation of the set `{1, 2, ..., N}` which represents the initial values on Ion's stack. The last element in the permutation is the one at the top of the stack.

# Output data

The output file `aranjare.out` will contain:
1. The first line contains the natural numbers `M` and `K`.
2. The next `K` lines will contain pairs of numbers `s t` (one pair per line) representing the move of the element from the top of stack `s` to the top of stack `t`. It is considered that Ion's initial stack has the index `0`, and the `M` additional stacks have indices `1, 2, ..., M`.

To qualify for points, after executing all the indicated operations in the output file, the elements in stack `0` must be ordered in ascending order from the base to the top.

# Constraints and clarifications

* For tests worth `25` points, we have `N = 980`. For the other tests, we have `N = 10000`.

$$

* For tests with `N = 980`, the points are awarded as follows:

$$

* If `M * K \leq 60\ 000`, `100%` of the test's points are awarded
* If `60\ 000 < M * K \leq 200\ 000`, `60%` of the test's points are awarded
* If `200\ 000 < M * K \leq 3\ 000\ 000` `20%` of the test's points are awarded
* For tests with `N = 10\ 000`, the points are awarded as follows:

$$

* If `M * K \leq 800\ 000`, `100%` of the test's points are awarded
* If `800\ 000 < M * K \leq 6\ 000\ 000`, `60%` of the test's points are awarded
* If `6\ 000\ 000 < M * K \leq 300\ 000\ 000` `20%` of the test's points are awarded

# Example

`aranjare.in`
```
3
3 2 1
```

`aranjare.out`
```
2 9
0 1
0 1
0 1
1 2
1 2
1 2
2 0
2 0
2 0
```
Two additional stacks were purchased, and 9 operations were performed. 
The first three operations move the elements from stack 0 to stack 1.
\ 
~[aranjare1.png]
\ 
The next three operations move the elements from stack `1` to stack `2`.
\ 
~[aranjare2.png]
\ 
The last three operations move the elements back to stack `0`, in sorted order.
\ 
~[aranjare3.png]