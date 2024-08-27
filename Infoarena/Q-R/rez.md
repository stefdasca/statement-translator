## Task

In a reserve, there are $n$ banana trees coded with the numbers $1$, $2$, $\dots$, $n$, and $\frac{n}{2}$ monkeys. To make the monkeys' lives more enjoyable, the caretakers of the reserve tie the banana trees together with wires, such that any two banana trees are connected by a single wire. After this operation, disputes arise among the monkeys in the reserve because when two monkeys traveling in opposite directions meet on the same wire, neither wants to back down. After many hours of study, the reserve director finds a saving solution by which any monkey can travel to any banana tree (regardless of the banana tree where it starts) in such a way that the wires it uses will not be used by any other monkey. To implement his idea, the director tasks his subordinates with painting the wires in such a way that each monkey travels only on its color. Write a program to determine a way to paint the wires along which the monkeys will travel, according to the director's solution.

## Input data

The input file `rez.in` contains a single natural number $n$ on the first line.

## Output data

The output file `rez.out` will contain $\frac{(n-1)}{2}$ lines, each line containing $n+1$ numbers separated by spaces, representing the order of the trees that a monkey can visit, after which it returns to the tree from which it left.

## Constraints and clarifications

$3 \leq n \leq 4001$

$n$ is an odd number.

The solution is not unique. Only one solution is required.

## Example

`rez.in`
```
5
```

`rez.out`
```
1 2 3 4 5
1 3 5 2 4 1
```