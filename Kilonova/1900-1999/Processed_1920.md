Here is the translated problem statement in English:

```markdown
Let $A$, $B$, $C$, $D$ be four natural numbers.

# Task
Write a program that determines the **number** of distinct pairs $N$ of **real** numbers $(X, Y)$ with the properties:
* $0 < X, Y < 1$;
* the numbers $A \cdot X + B \cdot Y$ and $C \cdot X + D \cdot Y$ are simultaneously **natural** numbers.

# Input data

The input file `nperechi.in` contains on the first line the numbers $A$, $B$, $C$, $D$, separated by a space, with the significance described above.

# Output data

The output file `nperechi.out` will contain on the first line the natural number $N$.

# Constraints and clarifications

* $0 < A,B,C,D < 10^9$
* The values $A, B, C, D$ guarantee that there will be a value for $N < 2^{63}$.
* Two pairs of real numbers $(X_1, Y_1)$ and $(X_2, Y_2)$ are distinct if $X_1 \neq X_2$ or $Y_1 \neq Y_2$.

# Example

`nperechi.in`
```
1 2 10 12
```

`nperechi.out`
```
6
```

## Explanation

$A = 1, B = 2, C = 10, D = 12$
There are $6$ distinct pairs of real numbers with the required properties: $(0.25,0.375)$, $(0.5,0.25)$, $(0.75,0.125)$, $(0.25,0.875)$, $(0.5,0.75)$, $(0.75,0.625)$.

$A \cdot X + B \cdot Y  = 1 \cdot 0.25 + 2 \cdot 0.375 = 1$ and $C \cdot X + D \cdot Y = 10 \cdot 0.25 + 12 \cdot 0.375 = 7$
$A \cdot X + B \cdot Y  = 1 \cdot 0.5 + 2 \cdot 0.25 = 1$ and $C \cdot X + D \cdot Y = 10 \cdot 0.5 + 12 \cdot 0.25 = 8$
$A \cdot X + B \cdot Y  = 1 \cdot 0.75 + 2 \cdot 0.125 = 1$ and $C \cdot X + D \cdot Y = 10 \cdot 0.75 + 12 \cdot 0.125 = 9$
$A \cdot X + B \cdot Y  = 1 \cdot 0.25 + 2 \cdot 0.875 =  2$ and $C \cdot X + D \cdot Y = 10 \cdot 0.25 + 12 \cdot 0.875 = 13$
$A \cdot X + B \cdot Y  = 1 \cdot 0.5 + 2 \cdot 0.75 = 2$ and $C \cdot X + D \cdot Y = 10 \cdot 0.5 + 12 \cdot 0.75 = 14$
$A \cdot X + B \cdot Y  = 1 \cdot 0.75 + 2 \cdot 0.625 = 2$ and $C \cdot X + D \cdot Y = 10 \cdot 0.75 + 12 \cdot 0.625 = 15$
```

The problem has been translated with mathematical values, variable names, general syntax, structure, and format preserved. I have also double-checked for potential grammar and/or syntax errors and corrected them according to the rules of the English language.