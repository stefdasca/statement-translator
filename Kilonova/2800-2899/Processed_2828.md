RAU-Gigel and Vlad are good friends and always like to challenge each other. This time, RAU-Gigel has invented an interesting math problem.

He has a secret tree with $N$ nodes (numbered from $1$ to $N$), in which each node is associated with a value (in addition to its sequence number in the tree), which is a natural number, and he tells Vlad information about some paths in this tree. An information item has the form $x$, $y$, $val$ and represents the fact that the chain in the tree from node $x$ to node $y$ has the greatest common divisor of the values associated with these nodes equal to $val$, where $val$ is a non-zero natural number.

# Task

Vlad knows that RAU-Gigel sometimes lies and that some of the given constraints might be wrong, so he wants to first find out, using the information at hand, if a tree could exist that meets all the constraints given by his friend.

Since he knows what a skilled programmer you are, Vlad would be very grateful if you could help him with this problem by writing a program that solves it as efficiently as possible.

# Input data

The input file `gcd_tree.in` contains on the first line the number $T$, which represents the number of test scenarios that need to be solved.

For each test, the first line contains 2 numbers $N$ and $M$, representing the length of the secret sequence and the number of constraints it must meet.

The second line contains $N - 1$ natural numbers, the $i$-th number representing the parent of node $i + 1$ in the tree (it is assumed that the tree has nodes indexed from $1$ and the root in node $1$).

Each of the next $M$ lines in the test contains 3 numbers $x$, $y$, $val$, the ends of the chain in the tree to which the constraint applies, as well as the value of this constraint.

# Output data

The program must display in the output file `gcd_tree.out`, on a single line, without spaces, a string of length $T$, consisting of the values $0$ or $1$, where the element at position $i$ is $1$ if the test scenario with number $i$ in the input admits a possible tree that satisfies all the constraints, or $0$ otherwise.

# Constraints and clarifications

* $1 \leq T \leq 10$
* $1 \leq N, M \leq 100\ 000$
* $1 \leq x,y \leq N$
* $1 \leq val \leq 20$
* Let $SN$ be the sum of the values $N$ from all test scenarios in one input file, and $SM$ be the sum of the values $M$ from all test scenarios in one input file.
* $1 \leq SN \leq 300\ 000$
* $1 \leq SM \leq 300\ 000$
* For tests worth 13 points, the tree is a simple chain in the form $1 - 2 - \dots - N$; $1 \leq N, M \leq 1\ 000$; $1 \leq SN, SM \leq 3\ 000$ and $val \in \{2, 4, 8, 16\}$.
* For other tests worth 19 points, the tree is a simple chain in the form $1 - 2 - \dots - N$; $1 \leq N, M \leq 1\ 000$; $1 \leq SN, SM \leq 3\ 000$ and $1 \leq val \leq 20$.
* For other tests worth 17 points, the tree is a simple chain in the form $1 - 2 - \dots - N$ and $val \in \{2, 4, 8, 16\}$.
* For other tests worth 24 points, the tree is a simple chain in the form $1 - 2 - \dots - N$.
* For other tests worth 8 points, $1 \leq N, M \leq 1\ 000$; $1 \leq SN, SM \leq 3\ 000$ and $val \in \{2, 4, 8, 16\}$.
* For other tests worth 6 points, $1 \leq N, M \leq 1\ 000$; $1 \leq SN, SM \leq 3\ 000$ and $1 \leq val \leq 20$.
* For other tests worth 9 points, $val \in \{2, 4, 8, 16\}$.
* For the rest of the tests, there are no additional restrictions, meaning only the initial conditions are kept.

# Example

`gcd_tree.in`
```
2
4 2
3 1 3
1 4 11
2 4 12
3 2
1 2
1 3 4
3 2 3
```

`gcd_tree.out`
```
10
```

## Explanation

For the first test scenario in the example, the secret tree might have the values $11$, $12$, $132$, $132$ associated with its nodes (written in order, from the node numbered $1$ to the node numbered $4$).

For the second test scenario, it can be easily shown mathematically that there is no solution.