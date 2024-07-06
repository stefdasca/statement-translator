In a group of friends, it is not uncommon for some to lend money to others. The resulting debts are later settled. For example, if Gigel buys a beer for Ghiță, next time Ghiță will pay for both, and the debts will be resolved.
If after a longer time the loans are not resolved on their own, the group of friends gathers to solve financial problems. At such a meeting, it is desirable to minimize the number of transactions. For example, if Gigel owes Ghiță $10$ RON, and Ghiță owes Daniel $10$ RON, it is enough for Gigel to give $10$ RON to Daniel, and all debts will be settled.

# Task

Knowing all the loans that have been made within the group of friends, determine a way to settle the debts with the minimum number of transactions. If there are multiple possibilities with the minimum number of transactions, determine a way for the total amount of money transacted to be minimal. If there are multiple possibilities with the minimum number of transactions and the minimal total amount of money, display any of them.

# Input data

The input file `datorii.in` will contain on the first line two natural numbers separated by space $N \\ M$, representing the number of friends in the group and the number of loans made. The friends are numbered from $1$ to $N$. The next $M$ lines will contain three natural numbers separated by space $A \\ B \\ C$ meaning: "$A$ has to pay $C$ RON to $B$".

# Output data

The output file `datorii.out` will contain on the first line two natural numbers separated by space $K \\ S$, where $K$ represents the minimum number of transactions, and $S$ the minimal total sum for $K$ transactions. The following $K$ lines will contain three natural numbers separated by space $X \\ Y \\ Z$ meaning: $X$ pays $Z$ RON to $Y$.

# Constraints and clarifications

* $2 \\leq N \\leq 20$
* $1 \\leq M \\leq 100$
* $1 \\leq C \\leq 100$

# Example

`datorii.in`
```
6 5
1 2 10
2 3 10
4 5 5
5 6 5
6 4 5
```

`datorii.out`
```
1 10
1 3 10
```

## Explanation

A single transaction was made: person $1$ gave $10$ RON to person $3$. The minimal amount transacted is $10$ RON.