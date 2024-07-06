In Papurǎ Vodǎ's country, the first democratic elections were recently organized. As a result, a parliament was formed with deputies having various political doctrines, left-wing or right-wing. These are described by non-zero natural numbers (the political orientation is more left-wing the smaller the number). The parliamentarians have associated themselves into political parties based on each one's doctrine. Any two deputies whose doctrines correspond to consecutive numbers are part of the same party. Therefore, the parties will be composed of deputies whose doctrines are consecutive numbers. (For example, if the parliament has $5$ deputies with doctrines $1$, $2$, $3$, $5$, and $6$, then they are grouped into two parties: one composed of $1$, $2$, and $3$ and another composed of $5$ and $6$.)
A government must have the support of more than half of the parliament members. For example, if the parliament is composed of $7$ deputies, a government needs the support of at least $4$ deputies.
To be able to govern, parties can group themselves into coalitions. The rule for forming coalitions is as follows: two parties $A$ and $B$, with $A$ being more left-wing, can be part of the same coalition only if all the parties with doctrines more right-wing than $A$ and more left-wing than $B$ are also part of that coalition. For example, if the parliament is composed of deputies with political orientations $1$, $2$, $4$, $5$, $7$, and $8$, then the party composed of $1$ and $2$ cannot associate with the party composed of $7$ and $8$ unless the party composed of $4$ and $5$ is also part of that coalition.

# Task

Given the parliament of Papurǎ Vodǎ's country through a strictly increasing sequence of non-zero natural numbers, determine the number of parliamentary parties and the number of majority coalition options.

# Input data

The input file `politic.in` contains on the first line a non-zero natural number $N$, representing the number of deputies in the parliament.
The second line contains $N$ non-zero natural numbers separated by spaces, strictly increasing, representing the doctrines of the parliamentarians.

# Output data

The output file `politic.out` will contain on the first line a non-zero natural number $X$, representing the number of parties in the parliament, and the second line will contain another non-zero natural number $Y$, representing the number of possible majority coalitions that can be formed.

# Constraints and clarifications

* $0 \\lt N \\leq 20 \\ 000$
* The numbers in the sequence are less than or equal to $30 \\ 000$
* For correctly determining the number of parliamentary parties, $30\\%$ of the score is awarded, and for correctly displaying the number of possible majority coalitions, $70\\%$ of the score is awarded.

# Example

`politic.in`
```
10
1 2 3 5 6 8 10 11 14 15
```

`politic.out`
```
5
4
```

## Explanation

The parliamentary parties are: $P_1 = (1, 2, 3)$, $P_2 = (5, 6)$, $P_3 = (8)$, $P_4 = (10, 11)$, and $P_5 = (14, 15)$.
The possible majority coalition options are:
- $P_1 + P_2 + P_3$
- $P_1 + P_2 + P_3 + P_4$
- $P_1 + P_2 + P_3 + P_4 + P_5$
- $P_2 + P_3 + P_4 + P_5$