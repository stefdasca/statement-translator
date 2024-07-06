# Task

To participate in a concert, $n$ people lined up in a single row, awaiting the opening of the ticket office. The heights of these $n$ people are all distinct. Based on this crucial information, security agents have decided for security reasons that the order of the people waiting in line must be changed according to their heights. Thus, the security agents will pick, one by one, a person and send them to the end of the line. After each such operation, let's call it a "move", the line shrinks, filling the previously free position. The security agents' strategy is this: at the end of all move operations, the minimum security risk is obtained if all the people to the right of the tallest person are taller than those to the left of the tallest person. Furthermore, the heights of the people will be increasing up to position $k$ of the tallest person and decreasing after position $k$.
More precisely: if $h_1, h_2, \ldots, h_n$ are the heights of the people after the move operations, then: there exists a position $k$, with $1 \leq k \leq n$ such that \(h_1 < h_2 < \ldots < h_{k-1} < h_k > h_{k+1} > \ldots > h_{n-1} > h_n \) and moreover \(h_i < h_j\) for any \(i < k\) and \(k < j\). Since such logic is hard to argue with, and the agents do not appear to be joking, the people waiting in line will accept all the moves imposed by them.

# Task

Given the number of people $n$ and their heights $h_1, h_2, \dots, h_n$, write a program that determines:
1. The position of the tallest person in the initial line, in case no move operations are needed.
2. The minimum number of moves required for the line of people to present a minimum security risk.

# Input data

The first line of the input file `risc.in` contains the natural number $p$ whose value can only be 1 or 2. The second line of the input file contains the natural number $n$ with the meaning from the statement. The third line contains $n$ distinct natural numbers: $h_1, h_2, \dots, h_n$, separated by a single space, representing the heights of the people.

# Output data

The output file is `risc.out`.
* If the value of $p$ is 1, then only requirement 1 is solved. In this case, the output file will contain on the first line a natural number $poz$ representing the position of the tallest person in the initial line. If the initial line does not meet the minimum security risk conditions, then $poz$ is $-1$.
* If the value of $p$ is 2, only requirement 2 is solved. In this case, the output file will contain on the first line a natural number $m$, representing the minimum number of moves needed to achieve minimum security risk.

# Constraints and clarifications

* $1 \leq n \leq 100\ 000$
* $1 \leq h_1, h_2, \ldots h_n \leq 100\ 000$
* The tallest person in a minimum security risk configuration can be placed in any of the positions $1, 2, \dots, n$
* For $50\%$ of the tests, $n \leq 2\ 000$, and for another $40\%$ of the tests, $n \leq 10\ 000$
* For the correct resolution of the first requirement, $20$ points are awarded, and for the second requirement, $80$ points are awarded.

# Example 1

`risc.in`
```
1
4
35 20 10 1
```

`risc.out`
```
1
```

## Explanation

$p = 1$, so only requirement 1 is solved. The line meets the minimum security risk conditions. The tallest person is at position $poz = 1$.

# Example 2

`risc.in`
```
1
6
1 8 12 20 15 10
```

`risc.out`
```
-1
```

## Explanation

$p = 1$, so only requirement 1 is solved. The line does NOT meet the minimum security risk conditions. The height sequence does not meet the condition that all height values to the right of the tallest person's position must be taller than all height values to the left of it. Hence $poz = -1$.

# Example 3

`risc.in`
```
2
5
2 8 4 20 16
```

`risc.out`
```
1
```

## Explanation

$p = 2$, so only requirement 2 is solved. Move the person of height $8$ to the end of the line. So $m = 1$.

# Example 4

`risc.in`
```
2
6
3 19 7 30 10 25
```

`risc.out`
```
2
```

## Explanation

$p = 2$, so only requirement 2 is solved. First move: move the person of height $19$ to the end of the line. The line becomes: `3 7 30 10 25 19`. Second move: move the person of height $10$ to the end of the line. The line becomes: `3 7 30 25 19 10`. So $m = 2$.