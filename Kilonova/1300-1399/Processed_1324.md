```markdown
A matrix with $n$ rows and $n$ columns is given. Both the rows and columns are labeled with numbers from $1$ to $2 \cdot n$, using each number exactly once (fig. $1$ – example for $n = 3$). We will denote the sequence of labels associated with the rows of the matrix as $o_1$, $o_2$, $\\dots$, $o_n$, and the sequence of labels associated with the columns of the matrix as $v_1$, $v_2$, $\\dots$, $v_n$ (fig. $4$).

Each element of the matrix must be filled with either the digit $1$ or $9$ (fig. $2$). By concatenating the digits from a row or a column, we obtain a number with $n$ digits. In total, there are $2 \cdot n$ numbers. These numbers must be pairwise distinct and, when arranged in the order of the labels associated with the rows and columns, they must be in ascending order (fig. $3$). We will concatenate the $2 \cdot n$ numbers in the order of the labels to obtain a single number with $2 \cdot n^2$ digits. This number will be called the _magic key_. For the example in fig. $3$, we obtain the magic key $111 \\colorbox{blue}{191} \\ 199 \\colorbox{blue}{911} \\ 919 \\ \\colorbox{blue}{991}$. 

~[magic.png]

# Task

Given $x$ a natural number, the dimension $n$ of the matrix, and the two sequences of labels $o_1$, $o_2$, $\\dots$, $o_n$ and $v_1$, $v_2$, $\\dots$, $v_n$, print the number of distinct magic keys (if $x = 1$) **or** the smallest magic key that can be associated with the matrix (if $x = 2$).

# Input data

The input file `magic.in` contains four lines. The first line contains the natural number $x$ ($1$ or $2$). The second line contains the natural number $n$. The third line contains $n$ distinct natural numbers separated by spaces representing the sequence $o_1$, $o_2$, $\\dots$, $o_n$ and the fourth line contains $n$ distinct natural numbers separated by spaces representing the sequence $v_1$, $v_2$, $\\dots$, $v_n$.

# Output data

The output file `magic.out` will contain a single line on which a natural number will be written which represents:

- if $x=1$, the number of distinct magic keys;
- if $x=2$, the smallest magic key.

# Constraints and clarifications

* $3 \leq n \leq 5$
* For each test file, there is at least one solution.
* For $50\%$ of the tests, $x=1$ (finding the number of magic keys), and for $50\%$, $x=2$ (finding the smallest magic key).
* For $20\%$ of the tests, $n=3$, $30\%$ of the tests $n=4$, and $50\%$ of the tests $n=5$.

# Example 1

`magic.in`
```
1
3
2 4 6
3 5 1
```

`magic.out`
```
3
```

# Example 2

`magic.in`
```
2
3
2 4 6
3 5 1
```

`magic.out`
```
111191199911919991
```

## Explanations

We have two solutions:

```
1 9 1
9 1 1 
9 9 1
```

```
1 9 1
9 1 1
9 9 9
```

The numbers obtained in the order of the labels: ($111$, $191$, $199$, $911$, $919$, $991$) respectively ($119$, $191$, $199$, $911$, $919$, $999$).

The two magic keys are $111191199911919991$ and $119191199911919999$, of which the first is smaller.
```