```markdown
# Task

LLM gives you a number $n$ and an array $a_1, a_2, \dots a_n$ consisting of $n$ natural numbers. Now, he wants you to find out for each position $i$ in the array if there exists a subsequence with the following properties:

* Its length is greater than or equal to $3$.
* $1 \leq x_1 < x_2 < \dots < x_k \leq n$, where $x_1, x_2, \dots, x_k$ are the positions in the initial array used for the found subsequence.
* One of the chosen positions is $i$ and it is not the first or the last position in the subsequence (in other words, $x_1 \neq i$ and $x_k \neq i$).
* If we consider the values from the $k$ positions, the sequence is a palindrome (for example, the sequence $7 \ 14 \ 14 \ 7$ is a palindrome). A sequence $s_1 \ s_2 \dots s_q$ is a palindrome if and only if $s_1 = s_q, s_2 = s_{q-1}$ and so on.

LLM quickly found the answers for each position in the array, now it's your turn to accomplish what LLM achieved.

# Input data

The first line of the input file `sirpal.in` contains $n$, the length of the array. The next line contains the $n$ values, representing the array values.

# Output data

The first line of the output file `sirpal.out` will contain a binary array of length $n$, where the value at position $i$ is $1$ if we can find such a sequence that contains position $i$ and $0$ otherwise. The values will be displayed without spaces.

# Constraints and clarifications

* $1 \leq n \leq 1 \ 000 \ 000$
* $1 \leq a_i \leq 1 \ 000 \ 000$ for each $i$ from $1$ to $n$

|#|Score|Constraints|
|-|-|--------|
|1|12|$n \leq 3$|
|2|16|$n \leq 300$|
|3|28|$n \leq 2 \ 000$|
|4|44|No other constraints|

# Example 1

`sirpal.in`
```
5
1 2 3 4 3
```

`sirpal.out`
```
00010
```

## Explanation

We observe that position $4$ is the only one that satisfies the conditions. We can choose the subsequence formed by indices $3, 4, 5$. We observe that it satisfies the conditions.

# Example 2

`sirpal.in`
```
17
1 6 2 4 6 3 7 5 9 7 3 8 8 10 10 8 10
```

`sirpal.out`
```
00110011110011110
```

## Explanation

For position $14$ (where the first $10$ is), we can choose the subsequence $12, 14, 15, 16$. We observe that this is not the only option.
```
