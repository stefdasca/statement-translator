# Cabins

On Anurim Street, there are $N$ phone booths arranged side by side. We will number these booths from $1$ to $N$ starting from the leftmost one. At any given moment, some booths are occupied, while others are yet to be occupied. Every second, a new person arrives who wishes to make a phone call. The selection strategy used by each person choosing a booth is as follows: The booth is chosen such that the time spent until both neighboring booths are occupied is maximized. If there are multiple booths satisfying condition $1$, the leftmost booth is chosen. To determine the booths that satisfy condition $1$, each person relies on the fact that those who arrive later will use the same strategy. Given the initial configuration of the booths and a number $K$, you must determine the index of the booth chosen by the $K$-th person.

## Input data

The first line of the input file `cabine.in` contains two natural numbers $N$ and $K$. The second line contains $N$ numbers with values from the set $\{0, 1\}$. If the booth with index $i$ is free, the $i$-th number will be $0$, otherwise it will be $1$.

## Output data

The output file `cabine.out` will contain a single natural number representing the index of the booth chosen by the $K$-th person.

## Constraints and clarifications

$1 \leq N \leq 100000$

$1 \leq K \leq$ number of free booths

For $30\%$ of the tests

$1 \leq N \leq 15$

None of the occupants of the booths will finish their conversation until all booths are occupied.

## Example

`cabine.in`
```
5 3
1 0 0 0 0
```
`cabine.out`
```
2
```

## Explanation

The first person who arrives will choose booth $5$ because it will never be between two occupied booths. If the second person chooses booth $2$, then the third person would choose booth $3$, so it would take one second for booth $2$ to be between two occupied booths. However, if the second person chooses one of the booths $3$ or $4$, the third person will choose booth $2$, so it will take two seconds for the booth chosen by the second person to be between two occupied booths. In conclusion, the second person will choose booth $3$, because it has a smaller index than booth $4$. The third person will have to choose between booths $2$ and $4$, both of which are already between two occupied booths. They will choose the one with the smaller index.