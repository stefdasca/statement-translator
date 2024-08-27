## Task

Ofelia has $N$ magic beanstalks in her garden, each with a certain height $H_i$. The problem is that the beanstalks have started to grow, so each plant $i$ will grow by $P_i$ daily. Ofelia knows that the beanstalks will only grow for the next $K$ days and then they will stop, and she wants the sum of the heights of all the beanstalks at the end of the $K$ days to be at most $S$. For this, she has a magic scissors with which, at the end of each day, she can reduce the height of each beanstalk $i$ by $x_i$. However, the magic scissors are not easy to use, so to cut a certain value $x_i$ from beanstalk $i$ the effort required is $x_i^2$ Joules (Ofelia is good at physics but, of course, not at computer science). Ofelia wants to determine the minimum total effort $J$ (the sum of all the efforts spent in the cutting processes) that she can make so that the sum of the heights of the beanstalks at the end of the $K$ days is at most $S$.

## Input data

The input file `vrejuri.in` will contain on the first line the numbers $N$, $K$ and $S$. The next $N$ lines will each contain two numbers $H_i$ and $P_i$ representing the initial height of the beanstalk $i$ and respectively the rate at which it grows.

## Output data

In the output file `vrejuri.out` you will print a single number $J$ the minimum effort that Ofelia can make.

## Constraints and clarifications

$1 \leq N, K \leq 100 \, 000$

$0 \leq S \leq 10^{18}$

$1 \leq H_i, P_i \leq 10^9$

It is guaranteed that the result $J$ will not exceed $10^{18}$

It is guaranteed that the sum of the heights of all undisturbed beanstalks at the end of the $K$ days will not exceed $10^{18}$

Attention: Ofelia can cut only after the first day ends. That is, the beanstalks grow on the first day and only then can Ofelia cut them

Attention: At the end of each day Ofelia can cut any value from any number of plants. She can cut different values from different plants on different days. Even if a plant is cut down to a height of $0$, it will still grow the next day (the root is not removed).

## Example

`vrejuri.in` 
```
2 
2 
1 
1 
1 
2 
2 
``` 

`vrejuri.out` 
```
18
```

## Explanation

Ofelia can cut $1$ from the first beanstalk and $2$ from the second on the first day, and $2$ from the first and $3$ from the second on the second day. The total cost is $18$.