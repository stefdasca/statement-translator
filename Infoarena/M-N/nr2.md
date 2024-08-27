# Nr 2

Zaharel made a list of all numbers with $L$ digits in base $B$ for which the sum of the digits leaves a remainder of $M$ when divided by $N$. To check if the list is complete, Zaharel will convert each such number to base 10 and sum them all. Then he will verify the sum with a computer program. Write a program that determines the sum of the numbers with $L$ digits in base $B$ for which the sum of the digits leaves a remainder of $M$ when divided by $N$, when each such number is converted to base 10. Since the sum can be very large, the result will be displayed modulo $P$.

## Input data

The first line of the input file `nr2.in` will contain the natural numbers $L$ $B$ $N$ $M$ $P$, in this order, separated by spaces.

## Output data

The first line of the output file `nr2.out` will contain a natural number representing the sought sum.

## Constraints and clarifications

$$1 \leq L \leq 10$$ 
$$16$$ 
$$0 \leq M < N$$
$$N \leq 60$$
$$2 \leq B \leq 10\ 000$$
$$2 \leq P \leq 1\ 000$$

## Example

`nr2.in`
```
2 3 2 0 1000
```

`nr2.out`
```
18
```

## Explanation

The numbers with $2$ digits in base $3$ for which the sum of the digits leaves a remainder of $0$ when divided by $2$ are $11$, $20$, $22$. Converting these numbers to base $10$ gives $4+6+8=18$.