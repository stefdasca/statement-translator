```markdown
Zizi will spend her holiday this summer in a beautiful seaside resort on the Black Sea. She will stay there for $N$ days. The days are numbered from $1$ to $N$. During each of the $N$ vacation days, she plans to sunbathe for as many time units as possible. However, she must consider the weather forecast, which is unfavorable on $K$ of the $N$ days, specifically on days $z_1$, $z_2$, $\\dots$, $z_k$. On each of these $K$ days, it will either rain or be too sunny, and Zizi will need to limit her sunbathing times to at most $t_1$, $t_2$, $\\dots$, $t_k$ time units. Additionally, for physical comfort reasons, Zizi wants the absolute difference in sunbathing times between any two consecutive days to not exceed $T$.

# Task

Knowing the days $z_1$, $z_2$, $\\dots$, $z_k$ on which there are limitations $t_1$, $t_2$, $\\dots$, $t_k$ for sunbathing time and the value $T$, determine the maximum number of time units Zizi can spend sunbathing on a single day of the $N$ vacation days.

# Input data

The file `plaja.in` contains on the first line three natural numbers $N$, $K$ and $T$ separated by a space, representing the number of vacation days, the number of days with sunbathing time limitations, and the maximum allowed difference in sunbathing times between any two consecutive days. Each of the following $K$ lines contains two numbers $z$ and $t$, separated by a space, representing the ordinal number of a day with a sunbathing time limitation and the time limit for that day respectively. The values $z_1$, $z_2$, $\\dots$, $z_k$ are in strictly increasing order.

# Output data

The file `plaja.out` will contain on the first line a single natural number tmax, representing the maximum number of time units Zizi can spend sunbathing on any of the $N$ vacation days.

# Constraints and clarifications

* $1 \\leq N \\leq 1 \\ 000 \\ 000 \\ 000$
* $1 \\leq K \\leq 100 \\ 000$
* $1 \\leq t_1, t_2, \\dots, t_k \\leq 100 \\ 000$
* $1 \\leq z_1 < z_2 < \\dots < z_k \\leq N$
* $2 \\leq T \\leq 1 \\ 000 \\ 000$
* For $20$% of the total score there are tests with $1 \\leq N, K \\leq 1 \\ 000$
* For $65$% of the total score there are tests with $1 \\leq N, K \\leq 100 \\ 000$

# Example 1

`plaja.in`
```
3 1 3
1 2
```

`plaja.out`
```
8
```

## Explanation

On day $1$, the sunbathing time is limited to $2$ time units. On the second day, the maximum sunbathing time is $2 + 3$, and on the third day, the maximum time is $2 + 3 + 3 = 8$ time units.

# Example 2

`plaja.in`
```
5 2 11
2 2
4 5
```

`plaja.out`
```
16
```

## Explanation

On day $2$, the sunbathing time is limited to $2$ time units, and on days $1$ and $3$ there are no limitations. Thus, the maximum sunbathing time for days $1$ or $3$ is $2 + 11 = 13$. On day $4$, the sunbathing time is limited to $5$ time units, and on day $5$ there is no limitation. Therefore, on day $5$, the maximum sunbathing time is $5 + 11 = 16$.
```