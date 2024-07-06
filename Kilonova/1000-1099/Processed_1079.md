Gigel is extremely passionate about numismatics and, for this reason, he collects coins. To keep them organized, he has grouped them into $N$ arrays, numbered from $1$ to $N$, each containing $M$ stacks of coins. Within an array, the stacks are numbered from $1$ to $M$ from left to right. Each stack contains a certain number of coins. Gigel is allowed to perform only one type of operation: moving an arbitrary number of coins from one stack and placing them into another stack.

Gigel wants all stacks with the number $i$, $1 \leq i \leq M$, from all $N$ arrays to contain the same number of coins. To achieve this, he can perform as many permitted operations as he wishes.

Write a program that determines the minimum number of coins that Gigel needs to move through permitted operations so that in the end all stacks follow the rule described above in the task.

# Input data

The input file `monede.in` contains on its first line two natural numbers $N$ and $M$, separated by a space, representing the number of arrays and the number of stacks in each array, respectively. Each of the next $N$ lines contains $M$ non-zero natural numbers, separated by spaces, representing the number of coins in each stack, in order from left to right.

# Output data

The output file `monede.out` will contain a single line that will contain the minimum number of coins determined.

# Constraints and clarifications

* $1 \leq N \leq 1 \ 000$
* $1 \leq M \leq 1 \ 000$
* $0 \leq$ initial number of coins in each stack $\leq 10 \ 000$
* It is guaranteed that for any test there is a solution

# Example

`monede.in`
```
2 4
1 2 7 5
4 2 9 6
```

`monede.out`
```
3
```

## Explanation

Take one coin from the first stack in the second array and place it on the fourth stack in the first array. The result is:
`1 2 7 6`
`3 2 9 6`
Then take two coins from the third stack in the second array and place them on the first stack in the first array. The result is:
`3 2 7 6`
`3 2 7 6`
Notice that after performing two permitted operations, moving a total of $3$ coins, the stacks with the same order number contain the same number of coins. There are also other sequences of permitted operations that can result in the same minimum number of coins moved ($3$).