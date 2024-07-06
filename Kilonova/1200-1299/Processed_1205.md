Gigel is an amateur electronics enthusiast. He claims to have invented a new electronic component called a resistoron. Strangely enough, resistorons have some properties that sound very familiar to us:
1. Any resistoron is characterized by a physical quantity called resistorness. This can only have natural number values.
2. Resistorons can be connected in series or in parallel, thus forming circuits.
3. Let there be two resistorons having resistornesses $R_1$ and $R_2$, respectively. The connection of resistorons in **series** is done as follows:

~[rez1.png]

The resistorness of this circuit will be $R_1$ + $R_2$.
4. The connection of the two resistorons in **parallel** is done as follows:

~[rez2.png]

The resistorness of this circuit will be $\\frac{R_1 \\cdot R_2}{R_1 + R_2}$. Since resistornesses can only be natural numbers, the division is integer (that is, the result is the integer quotient of ($R_1 \\cdot R_2$) divided by ($R_1 + R_2$)).
5. By connecting any number of resistorons in series and parallel, circuits are obtained. Circuits can be connected in series and/or in parallel following the same rules. The resistorness of a circuit is calculated by applying the above rules.

A circuit will be encoded by a string of characters constructed according to the following rules:

1. If circuit $C$ consists of a single resistoron and it has a resistorness value $x$, then the encoding of circuit $C$ is $R_x$. The resistorness of circuit $C$ will be $x$.
2. If circuit $C$ is obtained by connecting two or more circuits in series, encoded $C_1$, $C_2$, $\\dots$, $C_k$, then the encoding of circuit $C$ is obtained by concatenating in order the encodings of circuits $C_1$, $C_2$, $\\dots$, $C_k$. The resistorness of circuit $C$ is obtained by summing the resistornesses of circuits $C_1$, $C_2$, $\\dots$, $C_k$.
3. If circuit $C$ is obtained by connecting two or more circuits in parallel, then the encoding of circuit $C$ is obtained by enclosing in parentheses the encodings of the circuits it consists of and separating these encodings by a comma: ($C_1$, $C_2$, $\\dots$, $C_k$), $k > 1$. The resistorness of circuit $C$ is equal to the integer quotient of the product of the resistornesses of $C_1$, $C_2$, $\\dots$, $C_k$ and the sum of the resistornesses of circuits $C_1$, $C_2$, $\\dots$, $C_k$.

# Task

Write a program to determine the resistorness of a circuit.

# Input data

The input file `rez.in` contains on the first line a string of characters representing the encoding of a circuit according to the above rules.

# Output data

The output file `rez.out` contains a single line that prints the resistorness of the circuit specified in the input file.

# Constraints and clarifications

* $0$ < length of the encoding of a circuit $\\leq 1 \ 000$
* $0$ < resistorness of any resistoron < $100$
* $0$ < resistorness of any circuit < $2 \ 000 \ 000 \ 000$ (two billion)
* The string encoding a circuit does not contain spaces.
* For the test data, there will be no divisions by $0$.

# Example 1

`rez.in`
```
R12
```

`rez.out`
```
12
```

# Example 2

`rez.in`
```
R42R33R3
```

`rez.out`
```
78
```

# Example 3

`rez.in`
```
R2(R5,R69,R12)R80
```

`rez.out`
```
130
```

# Example 4

`rez.in`
```
(R5,R3(R12,R4),R3)
```

`rez.out`
```
6
```