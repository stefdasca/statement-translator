## Task

A show named Island Differential is hitting the small screen this year. Romeo, the star of the show, should interact and get familiar with a total of $N$ girls for a certain period of time. At the end of this period, after evaluating both appearance and personality, Romeo reports an individual coefficient $b_i$ for each girl representing their beauty. In the final scene, the ladies are positioned in a line and for each interval of length $K$ $(K \leq N, K \ \text{even})$ in this line, Romeo is supposed to have a total of $K/2$ roses. Evidently, for each such interval, Romeo will give roses to the most beautiful girls, i.e., those in the upper half (the larger half in the sorted order of their beauty coefficients). Given the beauty coefficients, help the show viewers predict how many roses each girl will receive in this final scene.

## Input data

The first line of the input file `romeo.in` contains $T$, the number of tests. Each test will contain two lines. The first line will contain $N$ and $K$. The second line will contain $N$ distinct, strictly positive integers not exceeding $10^9$, representing the beauty coefficient of each girl in line, as seen by Romeo.

## Output data

The output file `romeo.out` will contain the answers to the $T$ tests, each on a separate line. For each test, you will print a list of $N$ numbers representing the number of roses received by each girl.

## Constraints and clarifications

$1 \leq T \leq 10$

$1 \leq N \leq 100,000$

$1 \leq b_i \leq 10^9$

## Example

`romeo.in`
```
1
10 6
3 2 5 7 9 6 10 1 8 4
```

`romeo.out`
```
0 0 0 3 5 1 4 0 2 0
```