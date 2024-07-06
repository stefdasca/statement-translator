# Task
Determine the minimum time in which Valorosul României can reach city $A$ from city $B$.

# Input data
The input file `roadtrip.in` contains:
- The first line contains two natural numbers $N$ and $M$, with the meaning from the statement.
- The second line of the file contains $N$ natural numbers representing the time $t$ to fill up the R-mobil's tank for each city.
- The following $M$ lines contain 3 natural numbers $x$, $y$ and $d$ representing a highway of length $d$ between city $x$ and city $y$.
- The last line of the file contains 3 natural numbers $A$, $B$, and $C$ with the meaning from the statement.

# Output data
The output file `roadtrip.out` will contain a single natural number, which represents the minimum time in which Valorosul României reaches city $A$ from city $B$ or $-1$ if this is not possible.

# Constraints and clarifications
- $1 \leq N, C \leq 500; 1 \leq M \leq 1000$;
- $1 \leq x, y, A, B \leq N$;
- $d \leq C$, for any triplet $(x, y, d)$; $t \leq C$;
- For $10\%$ of the tests, the time $t$ to fill up the tank is $0$ for all cities and the length $d$ of all highways is $1$;
- For $30\%$ of the tests, the time to fill up the tank is $0$ for all cities;
- For another $20\%$ of the tests, $M = N-1$ and all $M$ edges are of the form $(x, x+1)$, $x = \overline{1..N-1}$.

# Example 1

`roadtrip.in`
```
4 4 
0 16 8 0 
1 2 5 
1 3 7 
2 4 11 
3 4 15 
1 4 16
```
`roadtrip.out`
```
16
```

# Example 2

`roadtrip.in`
```
4 4 
0 16 8 0 
1 2 5 
1 3 7 
2 4 11 
3 4 15 
1 4 15
```
`roadtrip.out`
```
30
```

# Explanations
**The image below is valid for both examples.**

In the first example, the R-mobil has enough fuel to reach city $1$ from city $4$ without refueling. The minimum time is given by adding the times on the highway $(1,2)$ and the highway $(2,4)$: $5 + 11 = 16$.

In the second example, the R-mobil needs to refuel to reach city $1$ from city $4$. It prefers to refuel in city $3$ because the total time is minimal: $7 + 8 + 15 = 30$. If it had refueled in city $2$, the total time would have been $5 + 16 + 11 = 32$.
~[exemplu.png]