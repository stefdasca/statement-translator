## Task

Recently, Don BJ signed a collaboration contract with a well-known electricity supply company. The first task for Don BJ is to inspect the high voltage poles. After a brief inspection, he observed that there are $N$ poles arranged in a line (numbered from $1$ to $N$), each having a given height $A_i$. Because Don BJ has an aesthetic sense, he now wants to modify the heights of the poles such that, in the end, they form either an increasing or decreasing sequence. In other words, Don BJ wants to create a new sequence $B_1, B_2, \dots, B_n$ where either $B_1 \leq B_2 \leq \dots \leq B_n$ or $B_1 \geq B_2 \geq \dots \geq B_n$. The total cost of transforming the sequence is $|A_1 – B_1| + |A_2 – B_2| + \dots + |A_n – B_n|$. Since Don BJ is a natural businessman, he wants the total cost of arranging the poles to be minimal in the end. Since he promised you a very high percentage of the profits from all his businesses, you need to calculate this minimal cost.

## Input data

The file `profit.in` contains $N$, the number of poles, on the first line. The following $N$ lines contain the heights $A_i$ of the high voltage poles (on line $i+1$ there is $A_i$).

## Output data

The file `profit.out` must contain a single number, the minimal cost to transform the sequence from the input file into an increasing or decreasing sequence.

## Constraints and clarifications

$1 \leq N \leq 2000$

The heights of the poles are natural numbers in the range $[0, 10^9]$

Don BJ is certain that the result fits in a 32-bit integer

## Example

`profit.in`
```
4
1
5
3
10
```

`profit.out`
```
2
```

## Explanation

Don BJ decides to bring pole 2 to height $4$ and pole 3 to height $4$. Thus the total cost is $|5 - 4| + |3 - 4| = 2$. This is also the minimal cost.