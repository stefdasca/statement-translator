
A natural number $n$ is called a power if there exist two natural numbers $a$, $b$, $a \geq 1$, $b \geq 2$ such that $n = a^b$. For example, the numbers $32$, $169$, $1$ are powers ($32=2^5$, $169=13^2$, $1=1^2$), while $72$, $2000$, and $31$ are not powers.
We read the natural numbers $N$, $M$ and a sequence of $N$ natural numbers $x_1, x_2, \dots, x_N$ from the interval $[1,M]$.

# Task
For each of the $N$ numbers $x_i$ determine a natural number $r_i$ from the interval $[1,M]$, with the property that $r_i$ is a power and for any other power $p$ from the interval $[1,M]$ the condition $|x_i – r_i| \leq |x_i – p|$ is fulfilled, where $|x|$ represents the absolute value of $x$ (the module).
If there are two powers equidistant from $x_i$, the smallest power will be chosen. For example for the number $26$, between the powers $25$ and $27$, the number $25$ will be chosen.

# Input data
The input file `abx.in` contains on the first line two numbers $N$ and $M$, and on each of the following $N$ lines contains a natural number $x_i$ ($1 \leq i \leq N$), with the meaning described above.
The numbers on the same line of the file are separated by a space.

# Output data
The output file `abx.out` will contain $N$ lines, on each line $i$ ($1 \leq i \leq N$) will be the natural number $r_i$ with the meaning described in the statement.

# Constraints and clarifications
- $1 \leq N \leq 5\ 000$
- $10 \leq M \leq 10^{18}$
- For tests worth 40 points, $M \leq 5\ 000$.
- For tests worth 70 points, $M \leq 10^9$.

# Example
`abx.in`
```
8 1000
345
99
999
500
123
124
99
256
```
`abx.out`
```
343
100
1000
512
121
125
100
256
```

## Explanation
$343 = 7^3$
$100 = 10^2$
$1\ 000 = 10^3$
$512 = 2^9$
$121 = 11^2$
$125 = 5^3$
$100 = 10^2$
$256 = 2^8$
