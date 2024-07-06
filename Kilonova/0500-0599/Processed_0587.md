# Task

Given a non-zero natural number $n$, known. RAU-Gigel chooses an arbitrary number from the closed interval $[1,n]$, let it be $x$. He then calculates the "XOR sum" `S = 1 ^ 2 ^ ... ^ (x-2) ^ (x-1) ^ (x+1) ^ (x+2) ^ ... ^ n` which he communicates to you. Can you guess $x$? RAU-Gigel is rather impatient, he wants a quick answer from you.

We denote the `^` operation as the `XOR` (exclusive disjunction operator).

To make sure you don't accidentally guess the answer, RAU-Gigel tests you multiple times.

# Input data

The input file `ghicitoare.in` contains on the first line a natural number $T$ representing the number of tests / riddles that RAU-Gigel proposes to you, then $T$ lines which contain pairs of the form `n S`, separated by a space, with the above significance. 

# Output data

The output file `ghicitoare.out` will contain $T$ rows, with the answers $x$, in the order requested, one per line, to RAU-Gigel's riddles.

# Constraints and clarifications

* $1 \leq T \leq 10$, $1 \leq n \leq 1 \ 000 \ 000 \ 000$, $0 \leq S \leq 1 \ 000 \ 000 \ 000$, $1 \leq x \leq n$;
* For tests worth $10$ points: $T = 2, n \leq 100$;
* For tests worth another $30$ points: $n \leq 1 \ 000 \ 000$;

# Example

`ghicitoare.in`
```
2
5 2
10 14
```

`ghicitoare.out`
```
3
5
```

## Explanation

RAU-Gigel proposes $2$ riddles.

For the first riddle we have: $n = 5$, $S = 2$. The number sought is $3$. Indeed:
```
S = 1 ^ 2 ^ 4 ^ 5 = 
|001| ^
|010| ^
|100| ^
|101| = 
|010| = 2 (we denote with |a| the binary representation of a)
```

For the second riddle we have: $n = 10$, $S = 14$. The number sought is $5$. Indeed, `S = 1 ^ 2 ^ 3 ^ 4 ^ 6 ^ 7 ^ 8 ^ 9 ^ 10` is $14$.