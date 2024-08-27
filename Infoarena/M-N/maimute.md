Monkeys

With the emergence of the antidote against the mad monkey, the mortality rate among monkeys has significantly decreased, thus making the family tree of these monkeys well known. Unfortunately, their advanced age has taken a toll on their memory and reaction speed, leading to occasional disputes over the structure of the family tree. The cause of these disputes is the descendant relationship, as some monkeys are smarter, while other monkeys want to know if they are descendants of those monkeys or not.

## Task

The monkeys have retrieved an old document from their library containing the family tree of the $N$ monkeys who are part of the problematic tribe and have also handed you $M$ questions such as "Is there a descendant-ancestor relationship between monkey $X$ and monkey $Y$?". You must answer these questions as quickly as possible, otherwise, the monkeys will start fighting and violence doesn't lead to anything good. 

## Input data

In the input file `maimute.in`, the first line will contain the number $N$ as described in the problem. On the next $N-1$ lines, there will be 2 numbers $X$ and $Y$ representing the fact that there is a direct relationship between monkey $X$ and monkey $Y$. On line $N+1$, the number $M$ as described in the problem will be found. On the following $M$ lines, there will be the monkeys' questions described by two numbers $X$ and $Y$.

## Output data

In the output file `maimute.out`, there will be $M$ lines. Line $i$ will contain the word "**DA**" if the answer to question $i$ is yes, otherwise line $i$ will contain the word "**NU**".

## Constraints

$1 \leq N \leq 100000$

$1 \leq M \leq 500000$

Monkey 1 is the oldest and wisest monkey in the whole tribe, and all other monkeys are descendants of it. The descendant-ancestor relationship is not necessarily direct (see example).

## Example

`maimute.in` `maimute.out`
```
7
6
4 4
7 3
1 2
5 1
2 4
1 6
4 6
3 5
6 7
7 1
4 6
6 4
```
```
DA
NU
NU
DA
DA
DA
```