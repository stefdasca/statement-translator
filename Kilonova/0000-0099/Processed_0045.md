```markdown
A farmer has $N$ rabbits (which he numbered from $1$ to $N$) and a lot of carrots. What is special in this household is that the rabbits are hierarchically organized, based on age, authority, and nutritional needs. Thus, each rabbit has exactly one direct boss (except for Rilă Iepurilă, who is the big boss, the boss of all rabbits). Any rabbit can have 0, 1, or more direct subordinates. Any rabbit-boss will eat at least one carrot less than each of their direct subordinates.

The farmer cannot decide how many carrots to give to each rabbit and would like to know in how many ways he can distribute the carrots among the rabbits, knowing that each rabbit can eat at least one carrot and at most $K$ carrots.

# Task
Write a program that calculates the number of possibilities modulo $30 \ 011$ to distribute the carrots to the $N$ rabbits knowing that any rabbit can eat between $1$ and $K$ carrots and must eat at least one carrot less than each of the rabbits that are its direct subordinates.

# Input data
The input file `iepuri.in` contains:
- The first line contains two natural numbers $N$ and $K$, separated by a space, representing the number of rabbits, respectively the maximum number of carrots that can be eaten by a rabbit.
- Each of the next $N-1$ lines contains two distinct natural numbers $a$ and $b$, located between $1$ and $N$, separated by a space, with the meaning that rabbit $a$ is the direct boss of rabbit $b$.

# Output data
The output file `iepuri.out` will contain the number of ways to distribute the carrots according to the conditions specified in the statement, modulo $30 \ 011$.

# Constraints and clarifications
* $1 \leq N, K \leq 100$
* The number that needs to be written in the output file will be displayed modulo $30 \ 011$.

# Example

`iepuri.in`
```
9 4
7 2
7 3
7 4
3 5
3 6
5 8
5 9
6 1
```

`iepuri.out`
```
9
```
```