Costel is passionate about logic circuits. He has two types of simple logic circuits available: the `AND` circuit and the `OR` circuit. Simple logic circuits have two inputs and one output.
\
~[logic1.jpg]

At every input of the circuit, one can input a `0` bit or a `1` bit, and the circuit is capable of calculating the respective logical operation (`AND` or `OR`) and sending the obtained result to the output. Costel has learned that he can combine multiple simple circuits to obtain complex circuits as follows: he connects the output of one circuit of any type to one of the inputs of another circuit, thus the result obtained at the output of one circuit is transmitted to the input of the other. This way, complex circuits can be constructed, which have multiple inputs and a single output.

Costel's latest discovery is the pyramidal logic circuit (abbreviated as PLC), which has the following structure:
- A single-level circuit is the simplest type of circuit and consists of an `AND` or an `OR` circuit;
- For a multi-level circuit, we have:
  - at level 1, there is a single circuit (`AND` or `OR`);
  - at level 2, there are two simple circuits of any type; the output of the first circuit is connected to input `1` of the circuit at level 1, and the output of the second circuit is connected to input `2` of the circuit at level 1;
  - at level $N$, there are $2^{N-1}$ simple circuits; the outputs of the first two circuits at line $N$ are connected to the inputs of the first circuit at level $N-1$, the outputs of the next two are connected to the inputs of the second circuit at line $N-1$, etc.

Example of PLC with 2 levels:
\
~[logic2.jpg]

In a PLC with $N$ levels, we have $2^N$ inputs, corresponding to the circuits at level $N$. At each input, one can introduce a `0` bit or a `1` bit, thus a sequence of $2^N$ bits.
\
~[logic3.jpg]

For the circuit in the figure above, let's assume that at the four inputs of the circuits at level 2 we have, in order, the bits `0111`. The value obtained at the circuit's output (the output of the simple circuit at level 1) is $0$, because this circuit is equivalent to the logical expression `((0 AND 1) AND (1 OR 1))`.

## Task 1 (30 points)
For a given PLC with $N$ levels and for $K$ given sequences of bits at the circuit's input, determine, for each sequence, the value calculated at the circuit's output.

## Task 2 (70 points)
For a given PLC with $N$ levels and knowing the value obtained at the output ($0$ or $1$), determine the number of distinct bit sequences that can be given at the input to obtain the specified value at the output. The result can be a very large number, therefore it will be displayed modulo $666013$.

# Input data
The first line of the `logic.in` file contains a natural number $C$ ($C = 1$ for task 1, $C = 2$ for task 2). The second line contains the natural number $N$, representing the number of levels of the circuit.

The next $N$ lines (lines from $3$ to $N+2$) contain the circuit description, with no spaces between characters, as follows:
- on line $3$ a character `&` or `|`, where the character `&` encodes an `AND` circuit, and the character `|` encodes an `OR` circuit;
- on line $4$ two characters from the set `{&, |}`;
- on line $5$ four characters from the set `{&, |}`;
- on line $N+2$ we have $2^{N-1}$ characters from the set `{&, |}`.

For task 1:
- The line $N+3$ contains a natural number $K$, representing the number of bit sequences given at the circuit's input;
- On each of the next $K$ lines, we have a sequence composed of $2^N$ bits (characters `0` or `1`), representing the bit sequence given at the input.

For task 2:
- The line $N+3$ contains a natural number from the set $\\{0, 1\\}$, representing the value that the circuit must output.

# Output data
For task 1, the `logic.out` file will display, on separate lines, $K$ natural numbers from the set ${0, 1}$, with the meaning given in the statement. For task 2, the `logic.out` file will display a natural number with the meaning given in the statement.

# Constraints and clarifications
- $1 \\leq N \\leq 8$
- $1 \\leq K \\leq 10$
- The truth tables of logical operations are:
\
~[logic4.jpg]

# Example 1
`logic.in`
```
1
2
&
&|
3
1101
0100
1000
```

`logic.out`
```
1
0
0
```

Explanation
---
$C = 1$, so we solve task 1. For the bit sequence `1101`, the value obtained at the circuit's output is the result of evaluating the expression: `((1 AND 1) AND (1 OR 0)) = (1 AND 1) = 1`.
For the bit sequence `0100`, the value obtained at the circuit's output is the result of evaluating the expression: `((0 AND 1) AND (0 OR 0)) = (0 AND 0) = 0`.
For the bit sequence `1000`, the value obtained at the circuit's output is the result of evaluating the expression: `((1 AND 0) AND (0 OR 0)) = (0 AND 0) = 0`.

# Example 2
`logic.in`
```
2
2
&
&|
1
```

`logic.out`
```
3
```

Explanation
---
$C = 2$, so we solve task 2. There are $3$ sequences of $4$ bits for which the value $1$ is obtained at the circuit's output: `1101`, `1110`, and `1111`.