# The Treasure

So far, to find a treasure, a seeker had to go through different tests: they had to escape from huge boulders, dragons, and poisoned arrows. The treasure on the pirates' island is more special because the captain who hid it wanted to ensure that only someone who is perceptive would manage to reach it. Thus, he introduced one final test of perceptiveness, which is found right in front of the treasure entrance. This last test is the test of the vessels. The seekers have at their disposal three vessels. Vessel $1$ has a capacity of $A$, vessel $2$ has a capacity of $B$, and vessel $3$ has a capacity of $C$. The capacities of the vessels satisfy the relations: $A < B < C$ and $A + B = C$. At the beginning of the test, $C$ is always full, and $A$ and $B$ are empty. To successfully pass this test and reach the treasure, the seekers have to make it so that there remain $M$ liters of water in any of the vessels. To achieve this, they can perform one or more moves. A move from vessel $x$ to vessel $y$ consists of pouring the content of vessel $x$ into vessel $y$ until vessel $x$ is empty or vessel $y$ is full. Help the treasure seekers pass this final test, and they will give you a part of the found treasure.

## Input data

The input file contains two lines. The first line contains $3$ natural numbers separated by a space: $A$, $B$, and $C$, with the meanings from the statement. The second line contains a natural number $M$ representing the number of liters of water that must remain in a vessel to pass the test.

## Output data

The output file will contain on the first line a natural number $N$, representing the number of moves performed. On the next $N$ lines, the $N$ moves will be described, one move per line. A move will be described as a pair $x$ $y$ of distinct numbers from the set $\{1, 2, 3\}$, meaning "pour water from vessel $x$ into vessel $y$".

## Constraints and clarifications

$0 < A, B, C < 100 001$

the number of moves does not need to be minimal

however, it must not exceed $200 000$

the used tests will have a solution

partial scores are not awarded

## Example

`comoara.in`

```
3 5 8
4
```

`comoara.out`

```
6
3 2
2 1
1 3
2 1
3 2
2 1
```

## Explanation

In the $3$ vessels, the following quantities remain: $0$ $5$ $3$ $\dots$ $2$ $1$