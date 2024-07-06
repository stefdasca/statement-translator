David VII has recently been chosen as king, and to save his country from crisis, he is considering modifying the tax system by hiring public officials. To ensure the system works very well, he structures the officials into levels such that for every $4$ officials at level $k$, there is one official at level $k + 1$ to whom they will hand over the collected taxes, including their personal tax. If the number of officials at a level $k$ is not divisible by $4$, those who do not have a superior will pay directly to the chief official. Ordinary people are considered level $0$ officials, and the chief official is the one at the highest level. Each citizen must pay a tax of $4$ gold coins. The only person exempt from this tax is the chief official.

# Task

Given a natural number $S$ representing the total amount collected by the state from taxes, write a program to calculate how many ordinary people are in David VII's country.

# Input data

The input file `taxe.in` contains on the first line the natural number $S$ with the significance described in the statement.

# Output data

The output file `taxe.out` will contain on the first line a natural number $P$ representing the number of ordinary people in David VII's country.

# Constraints and clarifications

* $0 < S \leq 2 \ 000 \ 000 \ 000$
* The problem admits a solution for all input data.

# Example

`taxe.in`

```
112
```

`taxe.out`

```
22
```

## Explanation

At level $0$ there are $22$ ordinary people, $20$ of them pay to the officials at level $1$, and the remaining $2$ pay directly to the chief official.  
At level $1$ there are $5$ officials, $4$ of them pay to the official at level $2$, and $1$ pays directly to the chief official.  
At level $2$ there is one official who pays directly to the chief official.  
The chief official will deliver to the state $22 \cdot 4 + 5 \cdot 4 + 1 \cdot 4 = 112$