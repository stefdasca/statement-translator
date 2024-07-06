```markdown
# Problem Statement

We consider a sequence of $n$ natural numbers $a_1, a_2, ..., a_n$. This sequence is used for encoding messages consisting of $n$ bits. Specifically, if the message is $t_1t_2...t_n$ (where $t_i$ can be $0$ or $1$, for any $1 \leq i \leq n$) then the encoded message is: $S = t_1a_1 + t_2a_2 + ... + t_na_n$

# Task
You will have [10 test files](https://kilonova.ro/assets/problem/2396/attachment/tests.zip), containing $a_1, a_2, ..., a_n$ and the encoded message. Generate 10 output files that contain the decoded message corresponding to each input file.

# Input data
Each file contains the natural number $n$ on the first line. The following $n$ lines contain the natural numbers $a_1, a_2, ..., a_n$, one number per line. The last line of the file contains the encoded message $S$.

# Output data
Each output file will contain a single line that will print a sequence of $n$ binary digits (without spaces between them) representing the decoded message.

# Constraints and clarifications

* $5 \leq n \leq 50$;
* $0 \leq S \leq a_1 + a_2 + ... + a_n \leq 2 \times 10^9$;
* For the test data, the solution is uniquely determined.

# Example

`cifru.in`
```
24
19226985
123697
67356296
19721773
1113273
69335448
23680077
9029881
85168664
93676782
5253843
77616588
78572630
13375812
17199980
101508862
59248276
3505733
35790095
62028546
85726819
56462819
103373994
91757169
667509506
```

`cifru.out`
```
110001000101101100010101
```
```
```