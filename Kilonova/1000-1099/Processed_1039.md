
Tomi is the elected mayor of Bittown. In the town, there are $N$ inhabitants, each with a fence made up of exactly 60 boards, each painted either white or black. Each fence is encoded by Tomi using a natural number whose binary representation reproduces the configuration of the fence from left to right, with black boards represented by the bit $1$ and white boards by the bit $0$. Thus, for example, a fence with only the last 2 boards painted in black will be encoded by Tomi with the number 3. Tomi decides to build a fence that is **representative** for Bittown, meaning it must satisfy all of the following rules:

1. Mayor Tomi's fence must have exactly 60 boards;
2. At least $K$ inhabitants in Bittown must find that for all the black boards in their own fence, the boards in the same positions on Mayor Tomi's fence are also painted black;
3. The number representing the code of Mayor Tomi's fence must be as minimal as possible.

# Input data

The input file `tomi.in` contains on the first line two natural numbers $N$ and $K$. The second line contains $N$ numbers, representing the codes of the fences of the inhabitants of Bittown.

# Output data

The output file `tomi.out` contains a single number, representing the code of the fence built by Mayor Tomi.

# Constraints and clarifications

* $1 \leq N \leq 100 \ 000$.
* Each code $< 2^{60}$
* For 19 points, all children will have only the codes $1$, $2$ or $3$.
* For other 38 points, the children's codes will be less than $60$

# Example

`tomi.in`
```
6 3
1 1 5 8 10 8
```

`tomi.out`
```
5
```

## Explanation

The answer is $5$ which has a binary configuration of $101$. This is representative for the first three fences $(1\ 1\ 5)$, because it includes their binary configurations thus respecting rule $2$.
