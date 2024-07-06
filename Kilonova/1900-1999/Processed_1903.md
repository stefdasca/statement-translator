Given a string of length $n$ composed **only of lowercase letters**. The following operations can be performed on the string:
* $1 \ l \ r \ c$: all characters in the substring $[l,r]$ become equal to $c$.
* $2 \ l \ r$: print `1` if the substring $[l,r]$ is a palindrome, otherwise print `0`.

# Task
Write a program that reads a string of length $n$ and $q$ operations and executes these operations.

# Input data

The first line will contain $n$ and $q$, the length of the string and the number of operations, respectively. The second line will contain the string. The next $q$ lines will contain the operations to be performed on the string.

# Output data

For operations of type $2$, print the response, without any additional spaces.

# Constraints and clarifications

* The string is indexed starting from $1$.
* $1 \leq n, q \leq 200\ 000$
* It is recommended to use the following line of code at the beginning of the `main` function to reduce the reading time of input data: `cin.tie(0)->sync_with_stdio(0);`.

|#|Score|Constraints|
|-|-|-|
|0|0|Examples|
|1|20|$1 \leq n, q \leq 10\ 000$; The string and operations are random.|
|2|30|$1 \leq n, q \leq 200\ 000$; Operations are only of type $2$.|
|3|50|No additional constraints|

# Example 1

`stdin`
```
7 4
abbaaaa
2 1 4
2 1 3
1 5 6 b
2 1 7
```

`stdout`
```
101
```

## Explanation

For the first operation, the substring `abba` is a palindrome.
For the second operation, the substring `abb` is not a palindrome.
At this point, we modify the string; it becomes `abbabba`.
For the third operation, the substring `abbabba` is a palindrome.

# Example 2

`stdin`
```
15 12
ajhsajdjadnggsk
2 5 9
2 6 8
1 6 11 r
2 5 9
1 13 15 a
2 11 13
1 1 3 a
2 1 15
1 4 5 g
2 1 15
1 5 5 r
2 1 15
```

`stdout`
```
1100001
```