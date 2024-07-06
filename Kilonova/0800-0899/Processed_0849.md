We have four natural numbers $N, A, B, C$, as well as three digits $c1, c2, c3$ that are distinct in pairs.

# Task

Determine the smallest natural number strictly greater than $N$, which has exactly $A$ digits $c1$, $B$ digits $c2$, $C$ digits $c3$, and does not contain any other digits.

# Input data

The input file `tcif.in` contains on the first line, separated by spaces, the natural numbers $A \ B \ C \ c1 \ c2 \ c3$. The second line contains the natural number $N$.

# Output data

The output file `tcif.out` will contain a single line which will print the smallest natural number strictly greater than $N$ that contains exactly $A$ digits $c1$, exactly $B$ digits $c2$, and exactly $C$ digits $c3$, and does not contain any other digits.

# Constraints and clarifications

* $N$ will have at least one digit and at most $1 \ 000$ digits.
* For 10% of the tests, $N \leq 30 \ 000$;
* For another 40% of the tests, $N$ will have at most $14$ digits.
* $0 \leq c1, c2, c3 \leq 9$; $c1, c2$ and $c3$ are distinct in pairs.
* $1 \leq A, B, C$; $ A + B + C \leq 1 \ 000$;
* The input data are chosen such that there will always be a solution.

# Example 1

`tcif.in`
```
2 2 2 3 2 4
293187
```

`tcif.out`
```
322344
```

## Explanation

The smallest number strictly greater than $293187$ that contains two digits $3$, two digits $2$, and two digits $4$ is $322344$.

# Example 2

`tcif.in`
```
2 3 1 1 0 6
44589
```

`tcif.out`
```
100016
```

## Explanation

The smallest number strictly greater than $44589$ that contains two digits $1$, three digits $0$, and one digit $6$ is $100016$.