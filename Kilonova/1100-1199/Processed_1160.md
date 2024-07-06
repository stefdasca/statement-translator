Here's the translated competitive programming problem statement:

---

In the army, a company consists of $n$ soldiers. At the morning inspection, the soldiers stand in a straight line in front of the captain. He is not satisfied with what he sees; it is true that the soldiers are arranged in the order of code numbers $1$, $2$, $\dots$, $n$ from the register, but not in order of height. The captain asks some soldiers to step out of the line, so that those remaining, without changing their positions but just moving closer together (to avoid large gaps between them) form a line in which each soldier, looking along the line, can see at least one of the ends (left or right). A soldier can see an end if there is no soldier between him and that end with a height greater than or equal to his own.

# Task

Write a program that determines, knowing the height of each soldier, the minimum number of soldiers that must leave the formation so that the remaining line meets the condition in the statement.

# Input data

The first line of the input file `aliniere.in` contains the number $n$ of soldiers in the line, and the next line contains a line of $n$ real numbers, with a maximum of $5$ decimal places each and separated by spaces. The $k$-th number on this line represents the height of the soldier with code $k$.

# Output data

The file `aliniere.out` will contain on the first line the number of soldiers who must leave the formation, and on the next line their codes in ascending order, separated two by two by a space. If there are multiple possible solutions, only one will be written.

# Constraints and clarifications

* $2 \leq n \leq 1 \ 000$
* The heights are real numbers in the range $[0.5, 2.5]$

# Example

`aliniere.in`
```
8
1.86 1.86 1.30621 2 1.4 1 1.97 2.2
```

`aliniere.out`
```
4
1 3 7 8
```

## Explanation

The remaining soldiers have the codes $2$, $4$, $5$, $6$ with heights $1.86$, $2$, $1.4$, $1$.

The soldier with the code $2$ sees the left end.
The soldier with the code $4$ sees both ends.
The soldiers with codes $5$ and $6$ see the right end.

---

Please review for any potential grammar and syntax errors according to the rules of the English language.