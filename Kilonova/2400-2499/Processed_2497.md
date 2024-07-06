> ~~Money~~ Gold medals cannot buy happiness ~ Surely not for a programmer

Seby the little square recently heard about the newest attraction at the Info(1)cup festival: the wheel of parentheses! The wheel consists of $n$ parentheses, positioned circularly, which can be seen as a string of $n$ characters, each of which being either `(` or `)`. Rotating the wheel is equivalent to transforming it into one of its circular permutations.

Now, circular permutations of a string $a_1, \dots , a_n$ are defined as follows: the string $a_1, \dots , a_n$ has $n$ circular permutations: $n \minus 1$ of the form $a_i, \dots , a_n, a_1, \dots , a_{i\minus1}$ when $1 < i \leq n$, and one circular permutation that coincides with the original string $a_1, \dots , a_n$. For example, the string of parentheses `()(())` has the following circular permutations:

1. `()(())`
2. `)(())(`
3. `(())()`
4. `())()(`
5. `))()((`
6. `)()(()`

We call a string of parentheses _balanced_ if we can insert `1` and `+` into the string so that it becomes a valid mathematical expression. For example, `(())()` is balanced, as we can insert `1` and `+` to form `((1 + 1) + 1) + (1 + 1)`, but `)(()` or `(()` are not. Formally, a string $a$ is balanced if and only if it is empty or of the form `(b)c`, where `b` and `c` are balanced.

# Task

Given a string of parentheses $s$, define the _value_ of $s$, denoted by $val(s)$, as the number of circular permutations of $s$ that are balanced. For example, if $s =$ `()(())`, then $val(s) = 2$, due to the circular permutations `()(())` and `(())()`.

The rules of the game are simple. The player is given $k$ Gold Medals. He can use a gold medal to swap two parentheses on the wheel. The player's score is the number of circular permutations of the string on the wheel that are balanced. Thus, if $s$ is a string on the wheel, then the score is $val(s)$. Can you help Seby use the $k$ Gold Medals to maximize his score?

Formally, given a string $s$ of $n$ parentheses, and the ability to swap $k$ pairs of parentheses within the string $s$, find a way to maximize the value of the obtained string.

# Input data

The first line of the input contains the integers $n$ and $k$. The second line of the input contains the string $s$ of parentheses.

# Output data

The output contains the maximum value that can be obtained after the swaps.

# Constraints

* $1 \leq n \leq 50\ 000$
* $1 \leq k \leq 9$
* $s$ contains only parentheses, e.g., `(` and `)`. It is guaranteed that the number of `(` in $s$ is equal to the number of `)`.
* The number of Gold Medals Seby has won is significantly larger, but his instinct tells him that he might need to use them again in the near future.

| # | Points | Constraints          |
| - | ------ | ------------------- |
| 1 | 7      | $n \leq 500, k = 0$ |
| 2 | 9      | $n \leq 20, k = 1$  |
| 3 | 13     | $n \leq 500, k = 1$ |
| 4 | 17     | $k = 0$             |
| 5 | 18     | $n \leq 2\ 000, k = 1$ |
| 6 | 19     | $k = 1$             |
| 7 | 17     | No additional constraints. |

# Example

`stdin`
```
6 1
)(())(
```

`stdout`
```
3
```

## Explanation

In this case, we can swap the parentheses at positions $3$ and $4$. The resulting string `)()()(` has the following circular permutations:

1. `)()()(`
2. `()()()`
3. `)()()(`
4. `()()()`
5. `)()()(`
6. `()()()`

Of these, only 3 strings are balanced.