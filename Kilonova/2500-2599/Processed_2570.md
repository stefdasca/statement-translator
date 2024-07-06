Petrică, passionate about algorithms and logical challenges, has a code that represents the access password to a very important database of algorithm problems.

Because he knows you are a skilled programmer, he wants to grant you access to the database if you can find the secret code by solving a riddle from him.

The secret code is represented by an array of integers of length $N$, indexed from $1$. Petrică will communicate $M$ constraints which this array must satisfy **simultaneously**, each in the form $(l, r, v)$, representing the fact that the elements in the array with indices within the interval $[l, r]$ have the property that the value obtained by applying the binary operator `|` ("**or**") between their values is equal to $v$.

# Task

Petrică is, however, cunning and might sometimes communicate constraints that do not allow the array to exist **simultaneously**. All he wants from you is to tell him if an array with the given properties can exist and he will then tell you which is the **correct code**.

# Input data

The first line of the input file contains an integer $T$, representing the number of test scenarios that need to be solved.

The first line of each test contains $2$ numbers $N$ and $M$, representing the length of the secret array and the number of constraints it must respect.

Each of the following $M$ lines in the test contain $3$ numbers $l$, $r$, $v$, representing the ends of the index interval to which the constraint applies, respectively the value of that constraint.

# Output data

The program must print on a single line, without spaces, an array of length $T$ consisting of values `0` or `1`, where the element at position $i$ is `1` if the test scenario with number $i$ from the input admits a possible code or `0` otherwise.

# Constraints and clarifications

* $1 \leq T \leq 100$
* $1 \leq N \leq 200\ 000$
* $1 \leq M \leq 200\ 000$
* $1 \leq l \leq r \leq N$
* $0 \leq v \leq 10^9$
* The sum of the values $N$ in all tests from an input file will always be less than or equal to $200\ 000$.
* The sum of the values $M$ in all tests from an input file will always be less than or equal to $200\ 000$.

|#|Points|Constraints|
|-|-|-|
|1|10|$T = 1$, $N \leq 5$, $M \leq 15$, $0 \leq v \leq 10$|
|2|20|The sum of the values $N \cdot M$ in all scenarios is at most $10^4$.|
|3|20|The sum of the values $N \cdot M$ in all scenarios is at most $10^7$.|
|4|20|$0 \leq v \leq 1$|
|5|20|$0 \leq v \leq 15$|
|6|10|Without additional constraints|

# Example

`codulbun.in`
```
2
5 2
1 3 3
2 5 0
4 2
1 3 1
2 3 4
```

`codulbun.out`
```
10
```

## Explanation

For the first test, an array that respects the given constraints is $3\ 0\ 0\ 0\ 0$.

For the second test, it can be demonstrated that there is no solution that satisfies all constraints simultaneously.