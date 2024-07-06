# Izumi is the unluckiest person in the universe — every day countless problems befall him that you couldn't even imagine. His great fortune is Shikimori, who daily protects him from all misfortunes. The misfortune from which Izumi needs protection today is a math test!

The math test consists of a single question, encoded by a natural number `N`. The answer to the question is any *true expression with exclusive "or"s and equals*, which contains `N` symbols.

**Expressions with exclusive "or"s and equals.** An expression with exclusive "or"s and equals is a sequence of two or more *terms* separated by an equal sign. The expression is considered true if all the terms from which it is formed are equal. A term is a sequence of *binary numbers* separated by the `^` character. The value of a term is considered the bitwise exclusive "or" of the binary numbers from which it is formed. A binary number is a sequence of binary digits — a binary number is allowed to start with the digit `0`. **The expression must contain at least one equal sign**.

# Input data
The first line contains the numbers `N` and `M` separated by a space, with the significance from the statement.

# Output data 
It will contain the required result, modulo `M`.

# Constraints
* The bitwise exclusive "or" is represented in C/C++ by the `^` operator.
* `1 \ \leq N \ \leq 500`
* `1 \ \leq M \ \leq 1000000009`
* `M` is a prime number

## Subtask 1 (10 points)
* `1 \ \leq N \ \leq 11`
## Subtask 2 (15 points)
* `1 \ \leq N \ \leq 20`
## Subtask 3 (10 points)
* `1 \ \leq N \ \leq 50`
## Subtask 4 (25 points)
* `1 \ \leq N \ \leq 100`
## Subtask 5 (40 points)
* `1 \ \leq N \ \leq 500`

# Examples
`stdin`

```
5 71
```

`stdout`

```
18
```

`stdin`

```
123 1000000007
```

`stdout`

```
275843270
```

Explanation
---

For the first example, the true expressions are `000=0, 001=1, 00=00, 01=01, 0^0=0, 0^1=1, 0=000, 0=0^0, 0=0=0, 0=1^1, 10=10, 11=11, 1^0=1, 1^1=0, 1=001, 1=0^1, 1=1^0, 1=1=1`.

~[image.png]