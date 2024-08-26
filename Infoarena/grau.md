# Wheat

Fane has decided to become a magnate of wheat, but now he faces significant problems due to European standards. According to EU standards, each type of soil is characterized by two properties, $pH$ and the Feng Shui index, and a farmer can only grow wheat on soil types with fixed $pH$ and Feng Shui index. Fortunately, for any type of soil, several operations can be performed, each operation costing one leu, with the effect of modifying one of the two properties by one unit. Fane found out which $N$ types of soils are accepted by the EU, so he wants to know for each type of soil on which he plans to grow wheat, what is the minimum cost to turn it into an approved soil. Unfortunately, Fane lives in Romania where many of the European standards were poorly introduced, so the legislation often changes through operations like: approving all soils with certain properties or banning soils of a certain type. Since Fane's questions can be preceded by legislative changes, find the answers to them at those respective moments.

## Input data

The first line of the input file contains the number $N$, and the following $N$ lines contain the two properties of the soils. Line $N+2$ contains the number $M$ of operations, and each of the next $M$ lines contains 3 numbers, $op$, $X$, $Y$, which describe the operations as follows: $X$ and $Y$ describe the $pH$ and Feng Shui index of a type of soil and the value of $op$ is $0$ in the case of a question from Fane, $1$ if a new law needs to be introduced to approve the described type of soil, or $2$ if a law needs to be repealed.

## Output data

The answers to Fane's questions will be found in the output file, one per line, in the order they were asked.

## Constraints and clarifications

$1 \leq N, M \leq 250\ 000$

At any moment, there can be multiple laws approving the same type of soil, all of which will be banned in the case of an operation of type $2$. All numbers in the input file are integers smaller than $2^{28}$ in absolute value.

## Example

`grau.in`
```
4
2 3
1 1
0 0
5 7
4
1 5 6
0 5 5
2 1 1
0 1 1
1 1 2
```

`grau.out`
```
1
2
```

## Explanation

The soil type $(5, 5)$ can be transformed at a cost of $1$ into a soil type $(5, 6)$, while the soil type $(1, 1)$ is transformed into a soil type $(0, 0)$ at a cost of $2$.