Aurora has just become a teacher at the local school. On the first day of school, she lined up all the `N` children in a single row and numbered them from `1` to `N`, from left to right. Now, Aurora asks `M` questions of the type: "are there two children `x` and `y` `(x \le y)` such that the difference between the number of boys and the number of girls situated in the sequence between child `x` and child `y` (including `x` and `y`) is exactly `K`; if yes, give an example!"?

# Task
Write a program that answers Aurora's questions.

# Input data
The first line of the input file `diff.in` will contain the natural numbers `N` and `M`, separated by a space, representing the number of children and respectively the number of Aurora's questions. The next line will contain `N` numbers `0` or `1` separated by a space; the `i`-th number on the line will be `0` if child `i` is a girl, and `1` if child `i` is a boy. The following `M` lines will contain the `M` questions, one question per line. On the `i`-th line among the `M` lines, there will be the natural number $K_i$, specified in Aurora's `i`-th question.

# Output data
In the output file `diff.out` you will write `M` lines. On the `i`-th line `(1 \leq i \leq M)`, you will write two natural numbers `x` and `y` `(1 \leq x \leq y \leq N)`, meaning that the difference between the number of boys and the number of girls situated in the sequence between child `x` and child `y` (including `x` and `y`) is exactly $K_i$, or `-1` if there is no solution.

# Constraints and clarifications
* `1 \leq N \leq 100 000`
* `1 \leq M \leq 200 000`
* $-1\ 000\ 000\ 000 \le K_i \le 1\ 000\ 000\ 000$, for `1 \leq i \leq M`
* There may be multiple correct answers to a question; display any of them.
* In the answer to a question `x` can be equal to `y`, in which case it is about a single child.
* For `20%` of tests `N \leq 300` and `M \leq 300`
* For `40%` of tests `N \leq 100 000` and `M \leq 500`
* For `40%` of tests `N \leq 3 000` and `M \leq 200 000`

# Example

`diff.in`
```
10 4
0 0 1 0 0 1 1 0 1 1
3
-3
10
0
```

`diff.out`
```
6 10
1 5
-1
2 3
```

Explanation
---

There are `10` children. Aurora asks `4` questions.

For the first question, two children `x` and `y` must be determined such that the difference between the number of boys and the number of girls situated between `x` and `y` is `3`. A possible solution is `x=6` and `y=10` (between `6` and `10` there are `4` boys and one girl).

For the second question, two children `x` and `y` must be determined such that the difference between the number of boys and the number of girls situated between `x` and `y` is `-3`. A possible solution is `x=1` and `y=5` (between `1` and `5` there are `4` girls and one boy).

For the third question, two children `x` and `y` must be determined such that the difference between the number of boys and the number of girls situated between `x` and `y` is `10`. There is no solution in this case.

For the fourth question, two children `x` and `y` must be determined such that the difference between the number of boys and the number of girls situated between `x` and `y` is `0`. A possible solution is `x=2` and `y=3` (between `2` and `3` there is one girl and one boy).