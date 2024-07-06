```markdown
# Statement
A pipeline is formed from a set of $N$ pipes. Through a pipe, a limited amount of water can pass, with each pipe having the capacity $C_i$. In other words, through pipe $i$, at most $C_i$ liters of water can pass.
# Task
Knowing that you can change the capacity of at most one pipe, find the maximum number of liters of water that can be transmitted between the two ends of the pipeline before and after the change.
# Input data
The input file `conducta.in` contains:
- The first line contains the natural number $P$ representing the task.
- The second line contains the natural number $N$ representing the number of pipes forming the pipeline.
- The third line contains $N$ natural numbers, $C_i$, representing the capacity of pipe $i$.
# Output data
The output file `conducta.out` contains:
- The first line contains a natural number, representing the answer to the task. If $P = 1$, print the amount of water that can be transmitted between the two ends without making any changes. If $P = 2$, print the amount of water that can be transmitted between the two ends by modifying the capacity of at most one pipe.
# Constraints and clarifications
* $2 \leq N \leq 10^5$
* $1 \leq C_i \leq 10^5$
* For $50$ points, $P = 1$, and for the other $50$ points, $P = 2$
# Examples
`conducta.in`
```
1
10
3 6 11 40 11 3 8 8 10 4
```
`conducta.out`
```
3
```
`conducta.in`
```
2
10
3 9 3 15 1 26 2 7 12 4
```
`conducta.out`
```
2
```
```
