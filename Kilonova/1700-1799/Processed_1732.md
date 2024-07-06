### Translated Problem Statement

The Prodigal Son receives a sum of $S$ lei for his birthday. Starting from that day (considered as day $1$), each day one of the following events happens:

* If $S$ gives a remainder of $0$ when divided by $3$, he spends two-thirds of the sum.
* If $S$ gives a remainder of $1$ when divided by $3$, he receives $3 \cdot A + 2$ lei from his father.
* If $S$ gives a remainder of $2$ when divided by $3$, he receives $3 \cdot B + 1$ lei from his mother.

### Task

Given $S$ – the initial sum, $A$, and $B$ – numbers with the meaning from the statement, determine the first two days in chronological order in which the prodigal son will have the same sum as that respective amount.

### Input data

The input file `risipa.in` contains on the first line the natural number $S$ representing the amount the prodigal son has on the first day, and on the second line the two natural values $A$ and $B$ separated by a space.

### Output data

The output file `risipa.out` will contain on the first line a natural value representing the first sum that repeats, and on the second line the two natural values, separated by a space, representing the first and the second day respectively when that sum was obtained.

### Constraints and clarifications

* $1 \leq S \leq 10^{100}$
* $1 \leq A, B \leq 1\ 000$
* The sum of a day is considered the one from the beginning of the day, before the prodigal son spends money or receives money from his mother or father.

### Example

`risipa.in`
```
7
1 1
```

`risipa.out`
```
6
7 9
```

#### Explanation

If the sum gives a remainder of $1$, he receives $5$ lei.
If the sum gives a remainder of $2$, he receives $4$ lei.
Day $1$: sum $7 \ rest = 1$ gains $5$ lei  
Day $2$: sum $12 \ rest = 0$ loses $8$ lei  
Day $3$: sum $4 \ rest = 1$ gains $5$ lei  
Day $4$: sum $9 \ rest = 0$ loses $6$ lei  
Day $5$: sum $3 \ rest = 0$ loses $2$ lei  
Day $6$: sum $1 \ rest = 1$ gains $5$ lei  
Day $7$: sum $6 \ rest = 0$ loses $4$ lei  
Day $8$: sum $2 \ rest = 2$ gains $4$ lei  
Day $9$: sum $6$ same as on day $7$