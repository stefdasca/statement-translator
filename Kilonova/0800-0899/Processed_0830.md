```
# The Hourglass

An **hourglass** is a device used to measure time. The hourglass consists of two glass chambers connected by a thin tube. One chamber is filled with sand, which flows into the second chamber at a constant rate. The hourglass can be inverted to measure another period of time.
Archaeologists have discovered a device, which they named the **hourglass**, consisting of $n$ identical hourglasses stacked on top of each other, numbered from $1$ to $n$, through which sand can flow from one hourglass to another due to gravitational force.
By studying this object, archaeologists have found that:
- The device can be used in both position $1$, where the hourglasses are in the order $1, 2, \ldots, n$ with the hourglass $n$ placed on the ground, and in position $2$, where the hourglasses are in the order $n, n-1, \ldots, 1$ with the hourglass $1$ placed on the ground;
- The sand transfer speed from one chamber to another, within the same hourglass, is **$1$ grain of sand/second**, for all hourglasses, regardless of position;
- Converting the hourglass from one position to another involves inverting it and repositioning the sand grains;
- The time taken for the sand grains to move from one hourglass to another is $0$.

Archaeologists study the behavior of the hourglass by conducting two different experiments, as follows:

1. The hourglass is placed in position $1$, a number $b$ of grains of sand are introduced into the top chamber of hourglass $1$, and it is determined after how many seconds all the grains of sand will reach the bottom chamber of the last hourglass;
2. The hourglass is placed in position $1$, a number $b$ of grains of sand are introduced into the top chamber of hourglass $1$, and then the hourglass is placed in **$k$ consecutive states**, each state being characterized by the values $S_i$ and $P_i$, representing the number of seconds and the position, respectively, where the hourglass remains stationary, and in the end, the number of grains of sand in each hourglass's chambers is determined.

For example, if the hourglass consists of $n=2$ hourglasses, and $b=3$ grains of sand are introduced into the top chamber of the first hourglass, the first experiment will result in the value $4$. In the second experiment, the hourglass is placed in $k=2$ states, characterized by $S_1=3, P_1=1$; $S_2=1, P_2=2$. The number of grains of sand in the hourglasses will evolve as shown in the following figure:

~[clepsidru.png]

# Task

Write a program that reads the values $n$ and $b$, as well as the values $k, S_i, P_i$ and calculates the values obtained by the archaeologists in conducting the two experiments.

# Input data

The first line of the input file `clepsidru.in` contains two positive natural numbers $n$ and $b$, separated by a single space, with the meaning described in the statement; the second line contains the positive natural number $k$ with the meaning described in the statement, and the following $k$ lines each contain a pair of values $S_i$ and $P_i$, separated by a single space, with the meaning described in the statement.

# Output data

The output file `clepsidru.out` will contain on the first line a natural number representing the value obtained in the first experiment, and on the following $n$ lines will contain a pair of natural numbers, separated by a single space, representing the quantities of sand grains in the top and bottom chambers of the $n$ hourglasses, written in the order from $1$ to $n$ of the hourglasses, after completing the second experiment.

# Constraints and clarifications

* $1 \leq n \leq 1\ 000$;
* $1 \leq b \leq 1\ 000\ 000\ 000$;
* $1 \leq k \leq 1\ 000$;
* $1 \leq S_i \leq 1\ 000$;
* $P_i$ belongs to the set $\{1, 2\}$, $1 \leq i \leq k$;
* For the correct solution of the first task, $25\%$ of the score is awarded, and for the correct solution of the second task, $75\%$ of the score is awarded. The score for the second task is awarded only if there is an answer for the first task in the output file, regardless of its correctness.

# Example

`clepsidru.in`
```
2 3
2
3 1
1 2
```

`clepsidru.out`
```
4
1 1
0 1
```

## Explanation

* The hourglass consists of $n=2$ hourglasses and $b=3$ grains of sand are introduced into the top chamber of the first hourglass.
* All the grains of sand will reach the bottom chamber of the last hourglass after $4$ seconds.
* After the hourglass remains $3$ seconds in position $1$ and $1$ second in position $2$, the hourglasses will contain $(1,1), (0,1)$ grains of sand.
```

I have translated the text following the specified instructions, corrected any grammar or syntax errors found, and ensured that all mathematical values, variable names, and image formats are preserved.