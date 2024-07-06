_Cif-Oji6_ is a dot matrix printer also known as a pin printer because printing is done by the impact of the print head pins on an ink ribbon. The pins are arranged in a rectangular grid consisting of $5$ rows of pins, each row containing $3$ equally spaced pins, as seen in the following figure.

~[imprimanta-1.png]

By activating different combinations of pins from the grid, the shape of each digit is defined, allowing it to be printed by dots, as follows:

~[imprimanta-2.png]

For example, the digit $2$ will be printed with $11$ dots as a result of activating $11$ pins from the grid: from the first row of pins, all $3$ pins are activated, from the next row only the right pin, then from the next row all $3$ pins again, then the left pin from the penultimate row and from the last row all $3$ pins.

# Task

1. Given that the Cif-Oji6 printer has printed the number $N$, determine the largest digit of the number $N$ for which a minimal number of pins from the grid were activated.
2. Given that the printer only has ink on the ribbon for printing $K$ dots, determine the **largest natural number** that can be printed with **exactly $K$ dots**.

# Input data

The input file `imprimanta.in` contains on the first line two natural numbers $N$ and $K$ separated by a space, where $N$ represents the number printed by the printer and $K$ represents the number of dots for which the printer still has ink.

# Output data

The output file `imprimanta.out` will contain:

* on the first line a single natural number representing the largest digit of the number $N$ for which a minimal number of pins from the grid were activated.
* on the second line of the file, it will contain **the largest natural number** that can be printed with $K$ dots.

# Constraints and clarifications

* $10 \leq N \leq 10^{15}$;
* $14 \leq K \leq 100\ 000$;
* For correctly solving task $1$, $30$% of each test's score is awarded, and for correctly solving task $2$, $70$% of each test's score is awarded.

# Example 1

`imprimanta.in`
```
2852 16
```

`imprimanta.out`
```
5
74
```

## Explanation

For printing the digit $2$, $11$ pins were activated, for the digit $8$, $13$ pins were activated, and for the digit $5$, also $11$ pins were activated. The minimal number of pins for printing a digit is $11$.

$5$ is the largest digit of the number $2852$ that was printed with $11$ pins. The largest natural number that can be printed with $16$ dots is $74$: $7$ dots (for the digit $7$) + $9$ dots (for the digit $4$) = $16$ dots.

# Example 2

`imprimanta.in`
```
88 25
```

`imprimanta.out`
```
8
11111
```

## Explanation

For printing the digit $8$, $13$ pins were activated.
The largest natural number that can be printed with $25$ dots is $11111$: $5 \cdot$ ($5$ dots for the digit $1$) = $25$ dots.