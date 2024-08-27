## Task

The Stars have arrived and it's time for Algorel to make a comeback in the social scene. The newspapers have been reporting that instead of preparing for the Stars, Algorel has been fervently watching an animated series. And indeed, it is true... He just got hold of a new season that has $N$ episodes, and Algorel wants to know in what order he could watch them (because he doesn't like the original order). He has received from a friend an expression that describes how the episodes are related to each other. The given expression follows certain rules: numbers from $1$ to $N$ may appear in an expression, as well as the characters $\left(\right)>#$ each number between $1$ and $N$ appears only once in the expression; each episode uniquely corresponds to a number a group of episodes is defined as a single episode or a subexpression that describes relationships between multiple episodes $>$ and $#$ are operators on groups of episodes and have the following properties: ge $1 >$ ge $2$- the group of episodes ge $2$ must be watched immediately after the group of episodes ge $1$ ge $1 #$ ge $2 # \dots #$ ge $k$ - the groups of episodes can be watched in any order but without interleaving $>$ has higher priority than $# the$ parentheses can appear anywhere in the expression as long as they are properly closed 

## Examples:

Expression Possible orders $1#2>3>4$ 
`1 2 3 4`
`2 3 4 1`
$((3>(4#5)>(1#(2>6))))$ 
`3 4 5 1 2 6`
`3 4 5 2 6 1`
`3 5 4 1 2 6`
`3 5 4 2 6 1`
$1>2#3>4#5>6$
`1 2 3 4 5 6`
`1 2 5 6 3 4`
`3 4 1 2 5 6`
`3 4 5 6 1 2`
`5 6 1 2 3 4`
`5 6 3 4 1 2$`

Algorel has some orders in which he would like to watch the episodes. He wants to know which of these orders are possible considering the rules described by the expression. Since he has been watching shows a lot lately, he doesn’t really know how to solve the problem and proposed it to the contest.

## Input data

The input file `episoade.in` will contain:
- The first line contains the expression that describes the relationship between episodes.
- The second line contains two numbers: $T$ - the number of preferred orders of Algorel and $N$ - the number of episodes.
- Each of the following $T$ lines describe a certain order: each line contains a permutation of the numbers from $1$ to $N$; the numbers are separated by spaces.

## Output data

The output file `episoade.out` will contain $T$ lines:
- On line $i$, print $1$ if the $i$-th order from the input file is possible according to the rules of the expression, or $0$ otherwise.

## Constraints

$1 \leq N \leq 100$

$1 \leq T \leq 20$

The length of the expression does not exceed $1000$ characters

The expression contains no spaces

For $50\%$ of the tests, parentheses will not appear in the expression

## Example

`episoade.in`

```
1#2>3>4
3 4
1 2 3 4
2 1 3 4
2 3 4 1
```

`episoade.out`

```
1
0
1
```

`episoade.in`

```
((3>(4#5)>(1#(2>6))))
3 6
1 2 3 4 5 6
3 5 4 1 2 6
3 5 1 4 2 6
```

`episoade.out`

```
0
1
0
```

`episoade.in`

```
3#(2#1)
4 3
1 2 3
3 2 1
3 1 2
1 3 2
```

`episoade.out`

```
1
1
0
1
```