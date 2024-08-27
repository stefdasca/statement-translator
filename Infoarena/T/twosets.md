## Task

Tassadar has a set of numbers written in base $2$ that he wants to convert to base $10$. Because the numbers in the set are very large, Tassadar is afraid of making mistakes. To ensure the correctness of the conversion, he provides you with the two encoded sets (one in base $2$, the other in base $10$) and asks you to tell him if they are identical.

## Input data

The input file `twosets.in` contains on the first line the number $T$, representing the number of tests. The next $T$ pairs of lines follow. The first line in each pair describes the first set (in base $2$), and the second line in each pair describes the second set (in base $10$). A set is described by a string of characters, each symbol having the following meaning:

- "i" followed by a digit means adding that digit to the end of the current number
- "d" means deleting the last digit of the current number
- "t" means inserting the current number into the described set

Initially, the number is empty (has no digits).

## Output data

In the output file `twosets.out` you will print $T$ numbers, each on a new line, indicating the answers to Tassadar's questions ($1$ if the answer is "YES", $0$ if the answer is "NO").

## Constraints and clarifications

The input file will be at most $3$ MB.

It is guaranteed that no number will be added more than once to the same set.

It is guaranteed that no numbers will be inserted that have the first digit $0$ in any set.

It is guaranteed that an empty number will not be inserted into any set.

No other situations will appear in the strings that describe the sets.

## Example

`twosets.in`
```
2
i1ti1dd
i3td
i1ti1i1tddd
i1tdi7td
```

`twosets.out`
```
0
1
```
