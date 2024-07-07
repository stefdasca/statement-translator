File Contents:
```
Recently, Bujorel has started playing with *zlego* pieces like a child. He has a piece made up of `N` parts numbered from `1` to `N`, each with a given height and beauty coefficient. A *zprefix* is defined as a sequence consisting of one or more consecutive parts starting with piece `1`. The goal is to select a *zprefix*, find all its occurrences in the rest of the piece, and sum up the beauty costs of these occurrences. For an occurrence of the chosen *zprefix* corresponding to the sequence formed by parts numbered from `i` to `j` (the height of piece `1` equals the height of piece `i`, the height of piece `2` equals the height of piece `i+1`, etc.), its beauty cost is the beauty coefficient of the last piece, that is, of `j`.

Bujorel is curious about what happens for every *zprefix* and wants to display the sum of beauty costs for all occurrences of each *zprefix*.

# Input data
The file `zlego.in` contains on the first line the number of tests `T`. Each test has the following format: the first line contains a natural number `N` representing the size of the *zlego* piece, on the next line there are `N` integers representing the heights of the pieces, separated by spaces, and on the third line there are also `N` integers, separated by spaces, the `i`-th number representing the beauty coefficient of the `i`-th piece.

# Output data
The file `zlego.out` must contain, for each of the `T` tests, `N` lines, the `i`-th line representing the sum of beauty costs for the occurrences of the *zprefix* `[1,i]`.

# Constraints and clarifications
* `1 \leq N \leq 250000`;
* `1 \leq T \leq 3`;
* The heights and beauty coefficients of the pieces fit in `32` signed bits;
* For `20%` of the tests `N \leq 100`;
* For `50%` of the tests `N \leq 1000`;
* **Attention!** Bujorel recommends using `64`-bit data types for displaying the result.

# Example

`zlego.in`
```
2
3
1 2 1
2 2 2
10
1 1 2 1 1 1 1 2 1 1
1 2 3 4 5 6 7 8 9 10
```

`zlego.out`
```
4
2
2
44
30
11
13
15
6
7
8
9
10
```

Explanation
---

In the second test, for the *zprefix* `[1, 1]`, we obtain the sum of the beauty costs of its occurrences `44 = 1+2+4+5+6+7+9+10`. For `[1, 2]` we have `2+5+6+7+10`, for `[1, 3]` we have `3+8`, for `[1, 4]` we have `4+9`, for `[1, 5]` we have `5 + 10`, for `[1, 6]` we have `6`, for `[1, 7]` we have `7`, for `[1, 8]` we have `8`, for `[1, 9]` we have `9`, and for `[1, 10]` we have `10`.
