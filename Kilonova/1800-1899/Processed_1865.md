![anticip.png|align=right]

A one-bit adder is a small device with $3$ inputs and $2$ outputs. It receives at the input $X_1$, $X_2$, and $T_i$. $X_1$ and $X_2$ are the bits that need to be added, and $T_i$ is the previous carry (as input). The outputs are $Y$ and $T_o$. $Y$ is the sum, and $T_o$ is the next carry (as output). To formalize these things, we can write:

$Y = (X_1 + X_2 + T_i) \ mod \ 2$ (mod is the remainder of the integer division)  
$T_o = (X_1 + X_2 + T_i) \ div \ 2$ (div is the quotient of the integer division)

To add numbers on $N$ bits, $N$ such adders are used. They are connected as shown in the figure below, meaning the carry output of one adder is the carry input for the next one.

![anticip2.png]

The problem with these multi-bit adders is that an adder needs to wait for the carry from the previous unit (except for the first adder).  
If a one-bit adder performs the calculation in one second, then for an $N$-bit adder (consisting of $N$ one-bit adders), $N$ seconds will be required.  
To improve the performance of these $N$-bit adders, units capable of anticipating the carry, i.e., the $T_i$ input, have been introduced. These units check the previous input data $X_1 (i-1)$ and $X_2 (i-1)$. If both are $0$, then $T_i$ will be $0$, regardless of what that unit receives as carry input. Similarly, if both are $1$, then $T_i$ will be $1$. All adders using anticipation can calculate the carry from the previous adder and start the calculation simultaneously with the first adder. The communication of the carry from one adder to the next is instantaneous.  
Researchers who invented these carry units want to know how much the system performance improves, and they decided to make all possible additions to compare with the old system. By all possible additions, it means adding any $N$-bit number to any other $N$-bit number exactly once (a total of $4 \cdot N$ additions). They want to know how long these operations took, i.e., the sum of all times for each addition.

# Task

Write a program that determines the total number of seconds required for all additions, using the anticipation devices.

# Input data

The input file `anticip.in` contains a single line that contains the natural number $N$ representing the number of bits.

# Output data

The output file `anticip.out` will contain a single line that will contain a natural number representing the number of seconds required for all possible additions.

# Constraints and clarifications

- $0 < N < 51$
- This problem has nothing to do with any dragons.

# Example

`anticip.in`
```
3
```

`anticip.out`
```
128
```

## Explanation

$16$ additions are performed in one second; $32$ additions are performed in two seconds; $16$ additions are performed in three seconds.  
For example, adding $010 + 001$ takes $3$ seconds. Adding $010 + 000$ takes $2$ seconds. Adding $010 + 110$ takes one second (the first adder adds the rightmost bits).