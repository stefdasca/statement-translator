# Task

Display the two numbers and their product.

# Input data

The first line of the input file `produs.in` contains the phone number.

# Output data

The output file `produs.out` contains in the first two lines the two numbers into which the phone number was divided, and on the third line contains their product.

# Constraints and clarifications

* The phone number is a natural number with at least two digits and less than or equal to $2 \ 100 \ 000 \ 000$.
* If one of the two numbers starts with one or more digits of $0$, then these will not be displayed, except in the case when the number $0$ appears.
* If there are multiple solutions, only one will be displayed.

# Example

`produs.in`
```
2301
```

`produs.out`
```
2
301
602
```

## Explanation

In the example we have the situations $2 \cdot 301=602$ or $23 \cdot 1=23$ or $230 \cdot 1=230$, from which $2 \cdot 301=602$ is chosen.