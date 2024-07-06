Veronel wants to repair the fence that separates his yard from his neighbor's yard. The fence is supported by `n` posts, placed collinearly, numbered in order from left to right: `1, 2, .. , n`. They are at distances of $d_i$ meters `(i=2, 3, ..., n)` from the first post. Posts `2, 3, ... n-1` can be moved to the left or right. Post `1` and post `n` cannot be moved. For simplicity, Veronel calculates the effort of moving a post as equal to the distance of the move. Let `D` be the greatest distance between two consecutive posts after making all the moves.

# Task
Given the maximum total effort `E` that Veronel is willing to make to move the posts, determine the smallest possible value for `D` that can be obtained under the conditions in the statement, such that the effort `E` is not exceeded. The total effort is defined as the sum of the efforts Veronel makes to move the posts.

# Input data
The first line of the input file `stalpi.in` contains two natural numbers `n` and `E` separated by a single space, with the meaning from the statement. The next line contains `n - 1` natural numbers $d_2, d_3, ... d_n$, separated by a single space, representing the initial distances of posts `2, 3, ... n` from post `1`.

# Output data
The output file `stalpi.out` contains a single line which will contain a natural number `D`, with the meaning from the statement.

# Constraints and clarifications
* Posts can only be moved to positions whose distance from post `1` is expressed by natural values.
* $0 \ \leq d_2 \ \leq d_3 \ ... \ \leq d_n \ \leq 10 \ 000$
* `3 \ \leq n \ \leq 50`
* `1 \ \leq E \ \leq 400 \ 000`
* For `20\%` of the tests `n = 3` and $d_n \ \leq 100$
* For `40\%` of the tests `n \ \leq 15` and $d_n \ \leq 200$
* For `70\%` of the tests `n \ \leq 15` and $d_n \ \leq 1 \ 000$
* For `100\%` of the tests `n \ \leq 50` and $d_n \ \leq 10 \ 000$

# Example

`stalpi.in`
```
4 10
10 30 50
```

`stalpi.out`
```
17
```

Explanation
---

Post `2` is moved `7` meters to the right and post `3` is moved `3` meters to the right.