Maricelu has just discovered how to color and write. His parents propose the following problem to help him deepen his new discoveries:

They give him a word represented as a string of characters $s$ consisting of $n$ lowercase letters of the alphabet. He has to color all characters with a minimum number of different colors. After coloring, he can swap any $2$ neighboring characters in the string that are of different colors. This operation can be performed any number of times (including $0$). The objective is to sort the string of characters in ascending order.

Maricelu needs to solve his parents' problem as quickly as possible!

# Task

Given $n$ and $s$, find the minimum number of colors needed to color the string, so that there exists a sequence of operations, of any length, that sorts it.

# Input data

The input file `ucf.in` contains:

- The first line contains $n$, the number of characters.
- The second line contains $s$, the string of characters.

# Output data

The output file `ucf.out` will contain a single integer, the minimum number of colors used.

# Constraints and clarifications

* $1 \leq n \leq 200\ 000$;
* For $20$ points, $n \leq 5\ 000$.
* Identical letters can be colored the same or different colors.

# Example 1

`ucf.in`
```
9
abacbecfd
```

`ucf.out`
```
2
```

## Explanation

The coloring in the first example can be: $ 1 1 2 1 2 1 2 1 2 $.
This can be sorted using swaps: $2-3$, $4-5$, $6-7$, $8-9$, $7-8$.

# Example 2

`ucf.in`
```
7
abcdedc
```

`ucf.out`
```
3
```

