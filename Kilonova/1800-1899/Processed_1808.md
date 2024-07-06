~[lego.png|align=right]

Crina and Rareș embark on an imaginary journey to Deva, each constructing a bus out of lego pieces. To avoid traffic jams, the entry of the buses into the city is managed by a signal displaying a natural number $S$. Thus, each bus that reaches the signal must wait a number of minutes equal to the absolute value of the difference between $S$ and the bus's identification number.

The two children equally share the lego pieces, which have digits written on them (each child has the same number of pieces with every digit), using these to form the identification numbers of the two buses. Crina arranges all her pieces and forms the identification number $N_1$ for her bus digit by digit, while Rareș does the same and forms the number $N_2$ for his bus. To ensure the two numbers are not identical, the children decide that $N_1$ must be strictly less than the signal number $S$ and $N_2$ must be strictly greater than $S$. If either of the two numbers can't be constructed from the shared pieces, the respective bus will have the identifier $0$ and will wait at the signal until the other bus passes.

# Task:

1. Determine the numbers $N_1$ and $N_2$ such that each child's bus waits as few minutes as possible at the signal.
2. Knowing that the two children's buses reached the signal at the same time, determine the minimum number of waiting minutes for the bus that will pass the signal first.

# Input data

The input file `lego.in` contains:
- The first line contains the natural number $C$, which can be either $1$ or $2$, representing the task number;
- The second line contains a single natural number $S$ with the meaning from the problem statement;
- The following lines contain pairs of natural numbers $n_i$ and $c_i$, separated by a space, with the following meaning: $n_i$ represents the number of pieces with the digit $c_i$ that each child has.

# Output data

For $C = 1$, the output file `lego.out` will contain on the first line two natural numbers $N_1$ and $N_2$, in that order, separated by a space, determined according to task $1$. 
For $C = 2$, the output file `lego.out` will contain on the first line a single natural number determined according to task $2$.

# Constraints and clarifications

* $1 \leq S \leq 10^{18}$;
* Each child has at most $19$ pieces;
* The digits $c_i$ are distinct;
* Correct resolution of task $1$ will yield $60$ points, while correct resolution of task $2$ will yield $40$ points.

# Example 1

`lego.in`
```
1
153
1 7
3 4
```

`lego.out`
```
0 4447
```

## Explanation

Only task $1$ is resolved. The signal displays the number $153$. Each child has $3$ pieces with the digit $4$ and one piece with the digit $7$. Crina cannot construct a number less than $153$ with these pieces, so her bus is identified with the number $0$. Rareș constructs the number $N_2 = 4447$.

# Example 2

`lego.in`
```
2
42
1 3
1 5
```

`lego.out`
```
7
```

## Explanation

Only task $2$ is resolved. The signal displays the number $42$. Each child has one piece with the digit $3$ and one piece with the digit $5$. Crina constructs the number $N_1 = 35$ and waits at the signal for $42 - 35 = 7$ minutes. Rareș constructs the number $N_2 = 53$ and waits at the signal for $53 - 42 = 11$ minutes. The minimum number of waiting minutes is $7$.