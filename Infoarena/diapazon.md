## Diapason

Henceforth, we will use the word "diapason" as a synonym for the term "interval". Why? Because it's fun. You are given $N$ diapasons $[Left[i], Right[i]]$ numbered from 1 to $N$. Diapason $i$ is at height $N - i$. The first diapason, the topmost one, starts to fall. All the others are fixed. If, during its fall, diapason 1 touches another diapason $j$ at least at one point, it will merge with that diapason with a probability of $\frac{P[j]}{Q[j]}$. From the merger of two diapasons $[A, B]$ and $[C, D]$, the resulting diapason is $[\min(A, C), \max(B, D)]$. You are required to find the expected length of diapason number 1 at the end of its fall (i.e., after it has reached a height strictly lower than all the other diapasons).

## Input data

The input file `diapazon.in` contains on the first line the number $N$. Each of the following $N$ lines describes one diapason through four integers: $Left$, $Right$, $P$, $Q$, representing a diapason $[Left, Right]$ which has a probability of $\frac{P}{Q}$ to merge with the falling diapason.

## Output data

The output file `diapazon.out` should contain on the first line a natural number $X < 1.000.000.007$. If the answer is a rational number $\frac{U}{V}$, then $X$ has the property $X * V \equiv U \ (\text{mod} \ 1.000.000.007)$.

## Constraints and clarifications

$0 < P < Q \leq 1.000$

$0 < Left \leq Right \leq 1.000.000$

For tests worth 20 points

$N \leq 200$

For tests worth 60 points

$N \leq 2.000$

For tests worth 100 points

$N \leq 100.000$

## Example

`diapazon.in`
```
5
35 64 58 873
41 70 407 729
18 90 165 628
10 57 33 104
60 69 152 466
```

`diapazon.out`
```
779316733
```

The answer is approximately 49.813963.