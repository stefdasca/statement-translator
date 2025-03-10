
# Task

Ana has $N$ strings indexed from $0$ to $N-1$. Each of the $Q$ days (indexed from $0$ to $Q-1$), Bogdan wants to take 2 strings from Ana, concatenate them, and return the resulting string to Ana. As Bogdan is careful, he noted the indices of the concatenated strings each day, but, being forgetful, he no longer remembers which is the last string he returned to Ana. Now, he asks you to help him, and he will reward you with 100 points if you succeed.

# Input data

The first line of the input file `stringuri.in` contains two integers, $N$ and $Q$.
The next $N$ lines contain Ana's initial strings.
The next $Q$ lines contain two natural numbers $a_i$ and $b_i$ which represent the concatenated strings (where $a_i$ is the first and $b_i$ is the second).

# Output data

The first line of the output file `stringuri.out` will contain the last string that Bogdan returns to Ana.

# Constraints and clarifications

* $1 \leq N, Q \leq 300 \ 000$;
* The sum of the lengths of the $N$ strings is $\leq 600 \ 000$;
* Each day, the 2 chosen strings are removed, and a new string is created with index $n+i$ (for the day with index $i$);
* $0 \leq a_i, b_i \leq n+i-1$;
* It is guaranteed that $a_i, b_i$ have not been chosen before day $i$.

|# | Score | Constraints|
| - | - | ------------|
|0|0|Examples.|
|1|23|$N, Q \leq 1 \ 000$, and the sum of the lengths of the $N$ strings is $\leq 2 \ 000$|
|2|19|All strings consist only of the letter $a$|
|3|58|No additional constraints|

# Example 1

`stringuri.in`
```
3
abc
def
ghi
2
0 1
3 2
```

`stringuri.out`
```
abcdefghi
```

## Explanation

First, Bogdan takes `abc` and `def` and makes the string `abcdef` with index 3. Then, he takes `abcdef` and `ghi` and concatenates them.

# Example 2

`stringuri.in`
```
5
k
f
bb
ew
aq
4
3 4
2 5
0 6
7 1
```

`stringuri.out`
```
kbbewaqf
```
