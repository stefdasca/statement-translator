
## Note: This problem may not have an official correct solution.

Ian is a child passionate about music, so his parents bought him a piano for his birthday. Ian's piano is special; it has $N$ keys. Since the piano is not new, the keys are harder to press, so pressing the $i$-th key takes $t_i$ seconds.

Since Ian is very impatient, he decided to repair the piano keys to make pressing a key as quick as possible. He can select two neighboring keys $i$ and $i+1$ which take $t_i$ and $t_{i+1}$ seconds to press, respectively, and polish them. After polishing, the two keys will take only $gcd(t_i, t_{i+1})$ seconds to press each. Practically, one operation will perform the following transformation on the keys: $t_i$ = $t_{i + 1}$ = $gcd(t_i, t_{i+1})$.

Ian considers the piano to be polished if the pressing time of each key is minimal possible.

# Task

1. Ian wants to make a riff (i.e., press each key once) and wants to know what the duration of a riff on the polished piano would be.
2. Since Ian does not have time to waste polishing, he wants a list of the minimum length of instructions such that after following the instructions the piano is polished.

# Input data

The input file `pian.in` contains:
- The first line contains the number $C$ which represents the task to be solved.
- The next line contains $N$, the number of piano keys.
- The next line contains $N$ numbers separated by a space, the $i$-th number representing the initial duration $t_i$ required to press the key with index $i$.

# Output data

The output file `pian.out` will contain:

If $C = 1$, then the file will contain a single line with a single number $S$, representing the answer for the first task.
If $C = 2$, then the file will contain on the first line a number $M$ which represents the minimum number of operations Ian has to perform, and on the next line $M$ numbers separated by a space, the $i$-th number $x_i$, representing that the $i$-th polishing operation will be done between the keys with indices $x_i$ and $x_i + 1$.

# Constraints and clarifications

* $C \in \{1, 2 \}$
* $1 \leq N \leq 100\ 000$
* $1 \leq v_i \leq 1\ 000\ 000$, for any $i \in \{1, 2, \dots, N \}$
* $1 \leq x_j < N$, for any $j \in \{1, 2, \dots, M \}$
* If for task $2$ there are multiple solutions with the minimum number of operations, any of them will be accepted.
* For tests worth $19$ points: $C = 1$
* For other tests worth $38$ points: $C = 2$ and $1 \leq N \leq 1\ 000$
* For other tests worth $43$ points: $C = 2$ and there are no additional constraints.

# Example 1

`pian.in`
```
1
5
2 4 6 8 10
```

`pian.out`
```
10
```

# Example 2

`pian.in`
```
2
5
2 4 6 8 10
```

`pian.out`
```
2
2 4
```

## Explanation

Ian can polish the piano in just $2$ instructions as follows:

Apply the operation on keys $2$ and $3$. We obtain the array $2\ 2\ 2\ 8\ 10$.
Apply the operation on keys $4$ and $5$. We obtain the array $2\ 2\ 2\ 2\ 2$.

Finally, the array of keys will be $2\ 2\ 2\ 2\ 2$. Thus, the duration of a riff will be $10$ seconds.
