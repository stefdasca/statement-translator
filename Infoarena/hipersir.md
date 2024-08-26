## Task

Consider a sequence of digits $s$, and let $S(s)$ be the set of non-empty subsequences of $s$ (for example, if $s = 123$ then $S(s) = \{1, 2, 3, 12, 13, 23, 123\}$). Let the hypervalue $h(s)$ of $s$ be the sum of the elements of $S(s)$, considered as numbers in base 10 (for example, $h(123) = 1 + 2 + 3 + 12 + 13 + 23 + 123 = 177$). Given a sequence of digits $c[1] \dots c[N]$, and $Q$ operations of two types: $1 \ a \ x$, where $c[a]$ takes the value $x$. $2 \ a \ b$, where $h(c[a], c[a+1], \dots, c[b]) \% 1.000.000.007$ is required. Perform all these operations.

## Input data

The input file `hipersir.in` contains on the first line the numbers $N$, $Q$. The second line contains the sequence of digits $c$. The following $Q$ lines contain the operations to be performed.

## Output data

The output file `hipersir.out` will contain the results of the operations, on different lines.

## Constraints and clarifications

$1 \leq N \leq 300,000$

$1 \leq Q \leq 300,000$

For 20 points

$1 \leq N \leq 15$, $1 \leq Q \leq 100$.

For another 20 points

$1 \leq N \leq 1,000$, $1 \leq Q \leq 1,000$.

## Example

`hipersir.in`
```
3 4
000
1 1 1
1 2 2
1 3 3
2 1 3
```

`hipersir.out`
```
177
```

`hipersir.in`
```
10 10
1373429614
1 7 1
2 7 8
1 8 8
1 3 0
1 5 3
1 2 8
2 1 9
2 5 8
1 1 2
1 3 8
```

`hipersir.out`
```
23
530826057
4585
```