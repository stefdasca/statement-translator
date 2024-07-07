
After a full day, three boys play with numbers. Every evening, one of them chooses a number $x$, and another one a number $y$ greater than or equal to $x$. The third one proposes something more interesting. Thus, he chooses to tell them almost instantly the sum of perfect squares from $x$ and $y$.
You have to solve something similar, but you only know what the first and last boy say. To check if they made mistakes in their calculations, however, you need to find the number that the second boy could say.

Formally, for two numbers $x$ and $y$, $SPP(x, y) = x^2+(x+1)^2+...+y^2$ is defined (the sum of perfect squares from $x$ to $y$).

There are $Q$ questions of the form `x p`, and it is required to find **the smallest $y$ greater than or equal** to $x$ for which $SPP(x, y) \geq p^2$.

# Task

Calculate for each question, the minimum $p$, for which the relationship is satisfied.

# Input data
The first line of the file `spp.in` contains a natural number $Q$. The lines $2, 3, ..., Q + 1$ contain one pair `x p` each that satisfies the constraints.

# Output data
The output file `spp.out` will contain the answer to each query.

# Constraints and clarifications
* $1 \leq Q \leq 10^5$;
* $1 \leq x \leq 10^5$;
* $1 \leq p \leq 10^9$;
* For 30% of the tests, $Q \leq 100$ or $p \leq 10^3$.

# Example

`spp.in`
```
2
1 5
10 19
```

`spp.out`
```
4
12
```

## Explanation

- $1^2 + 2^2 + 3^2 + 4^2 = 29 \geq 5^2$;
- $10^2 + 11^2 + 12^2 = 385 \geq 19^2$.
