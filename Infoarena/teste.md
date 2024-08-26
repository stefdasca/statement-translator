## Tests

After years of resentment towards the committee experienced as a contestant, you decided to change things according to your views and join those who create the problems. As a new member of the committee, your first task, before you get to propose problems, is to create tests. The problem you are given for this task is the following: Given a number $S$, initially equal to $0$. For $3$ values $n$, $k$ and $mod$, we take every sequence of natural numbers of length $n$ with values from $1$ to $k$, and add all its elements to $S$. Display $S$ modulo $mod$. For $n$ and $k$, a colleague from the committee managed to find suitable values (birthdays, phone numbers, card PINs, values irrelevant to you). Now, your task is to find a suitable value for $mod$ (you already know this is a non-negative non-zero number). A value is considered suitable if the answer to the initial problem ($S$ modulo $mod$) is different from $0$ (let's be serious, there will surely be contestants who will display only $0$ hoping to score points). The first thing you will do is write a program that determines how many values are not suitable for $mod$ (among non-zero natural numbers). However, this number can be extremely large, so you are satisfied with the remainder of dividing the number by $1\ 000\ 000\ 007$. (why be more demanding than the rest of the committee?)

## Input data

The input file `teste.in` contains the values $n$ and $k$.

## Output data

The output file `teste.out` will contain the number of values of $mod$ for which $S$ modulo $mod$ is equal to $0$, modulo $1\ 000\ 000\ 007$.

## Constraints and clarifications

$1 \leq n, k \leq 1\ 000\ 000\ 000$

The tests are grouped! Each of the following sets of tests represents a group.
The rest of the tests (those that do not meet other specific conditions) are also grouped.

For $10$ points, $1 \leq n, k \leq 3$

For another $10$ points, $1 \leq S \leq 30\ 000\ 000$
$1 \leq n, k \leq 10$

For another $20$ points, $1 \leq S \leq 20\ 000\ 000\ 000$
$1 \leq n, k \leq 20$

We do not recommend displaying $0$ regardless of input for this problem.

## Example

`teste.in`
```
2  
2
```

`teste.out`
```
6
```

`4`
```
5
```

`30`

## Explanation

For the first example, $S$ is $12$, so the unsuitable values for $mod$ are $1, 2, 3, 4, 6, 12$. For the second example, $S$ is $7500$, so there are $30$ mod values that are not suitable.