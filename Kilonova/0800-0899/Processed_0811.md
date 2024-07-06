```markdown
It is considered a two-dimensional array with $m$ rows, $n$ columns, and elements as natural numbers. For each element, the number of positive divisors is determined. Groups are then formed with the elements of the array that have the same number of divisors, groups noted as $G_1, G_2, \dots, G_k$. The groups are sorted in descending order based on the number of elements they contain. It is known that a group $G_1$ is in front of another group $G_2$ if $G_1$ has more elements than $G_2$ or, in the case where the two groups contain the same number of elements, the number of divisors of the elements of group $G_1$ is greater than the number of divisors of the elements of group $G_2$. After sorting the groups in descending order, we denote the first group as $A$ and the second group as $B$. In the case where all elements will have the same number of divisors, there will be only one group, the group $A$.

# Task

Write a program that reads $m$, $n$, the elements of the array, and displays:
* the number of positive divisors for group $A$, the number of elements in the group, and the largest value in the group;
* the number of positive divisors for group $B$, the number of elements in the group, and the largest value in the group; in the case where the second group does not exist, the value $0$ will be displayed three times.

# Input data

The file `grupe.in` contains on the first line the values of $m$ and $n$ separated by a space, and on the next $m$ lines $n$ elements each separated two by two by a space, representing the elements of the array.

# Output data

The file `grupe.out` will contain:
- the first line contains the number of positive divisors of group $A$, the number of elements in group $A$, and the largest value in group $A$, values separated two by two by a single space;
- the second line contains the number of positive divisors of group $B$, the number of elements in group $B$, and the largest value in group $B$, values separated two by two by a single space.

# Constraints and clarifications

* $1 \leq m, n \leq 100$
* The initial elements of the two-dimensional array are less than or equal to $100 \ 000$ and greater than $1$;
* A group can consist of a single element;
* $50\%$ of the points are awarded for correctly displaying each line.

# Example 1

`grupe.in`
```
2 3
16 2 4
10 6 5
```

`grupe.out`
```
4 2 10
2 2 5
```

## Explanation

The number of divisors for each element of the array: $5$ divisors (for value $16$), $2$ divisors (for value $2$), $3$ divisors (for value $4$), $4$ divisors (for value $10$), $4$ divisors (for value $6$) and $2$ divisors (for value $5$).

The groups can be formed: with $2$ divisors (elements $2, 5$), with $4$ divisors (elements $10,6$), with $3$ divisors (element $4$) and with $5$ divisors (element $16$). After sorting the groups in descending order, the groups with the most elements are those that contain 2 elements: ($10, 6$), respectively ($2, 5$). Because the elements $10$ and $6$ have $4$ divisors, they will be part of group $A$, and $2$ and $5$, with only $2$ divisors each, will be part of group $B$.

So group $A$ has $4$ divisors, $2$ elements and the largest element in the group is $10$, while group $B$ has $2$ divisors, $2$ elements and the largest element in the group is $5$.

# Example 2

`grupe.in`
```
2 3
2 15 4
10 6 5
```

`grupe.out`
```
4 3 15
2 2 5
```

## Explanation

The number of divisors for each element of the array: $2$ divisors (for value $2$), $4$ divisors (for value $15$), $3$ divisors (for value $4$), $4$ divisors (for value $10$), $4$ divisors (for value $6$) and $2$ divisors (for value $5$). After sorting the groups in descending order, the group with the most elements is the one formed by the elements $10, 6, 15$, each element having exactly $4$ divisors.

This will be group $A$. Group $B$ will be the one formed by two elements, the other group having only one element. So group $A$ has $4$ divisors, $3$ elements and the largest element in the group is $15$, while group $B$ has $2$ divisors, $2$ elements and the largest element in the group is $5$.
```