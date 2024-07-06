Mrs. Principal needs to divide the 7th-grade students into $k$ groups for a competition. The number of students in any two groups should differ by at most $1$, and the number of girls and boys in each group should also differ by at most $1$. Knowing that there are a maximum of $200$ students in the 7th grade, Mrs. Principal, after forming the groups, wants to check if they are well-formed (each child appears in only one group and the groups meet the required conditions).

For example:
- For $10$ students in the 7th grade, a number of $3$ groups, the sequence indicating the composition of girls or boys: `fbfbfbfbfb` with the meaning that the child with the number $1$ is a girl, the one with number $2$ is a boy, etc.
- The first group has $3$ children and the composition: $1 \ 2 \ 10$;
- The second group has $3$ children and the composition: $3 \ 4 \ 9$;
- The third group has $4$ children and the composition: $5 \ 6 \ 7 \ 8$;
- The answer is: the groups were correctly formed.
- The numbers that form a group represent the rank number that each child has in the initial series.

# Task

Write a program that, knowing the total number of children, the number of groups, a sequence consisting of the characters `f` and `b` for each child if it is a girl or boy, the number of children in each group, and the composition of the groups, answers with `YES` or `NO` if the children's groups were correctly formed or not. For each group, the number of girls and the number of boys in that group will be specified. The groups are correctly formed if all the children are included, the number of children in the groups differs by at most one child and for each group the number of girls and boys differs by at most $1$.

# Input data

The file `grupe.in` contains in the first line the natural numbers $n$ and $k$, representing the number of students in the 7th grade and the number of groups the principal wants to form. The next line contains a series of $n$ characters `f` and `b` formed as follows: if the student with order number $i$ is a girl, the character at position $i$ in the series is `f`; if the student with order number $i$ is a boy, the character at position $i$ in the series is `b`. The next $k$ lines will have the following structure: the number of children in the group followed by the order numbers of the children forming that group.

# Output data

The output file `grupe.out` will contain in the first $k$ lines two natural values representing the number of boys and the number of girls in each group, separated by a space, and on the last line the word `YES` if the groups are correctly formed or the word `NO` otherwise.

# Constraints and clarifications

* $1 \leq n, k \leq 200$;

# Example 1

`grupe.in`
```
10 3
fbfbfbfbfb
3 1 2 10
3 3 4 9
4 5 6 7 8
```

`grupe.out`
```
2 1
1 2
2 2
YES
```

## Explanation

The number of children in the groups is $3, 3, 4$, so they differ by at most $1$; in the first group there are $2$ boys and one girl, in the second group there are $2$ girls and one boy, and in the third group there are $2$ girls and $2$ boys.

# Example 2

`grupe.in`
```
10 2
fffffbbbbb
7 1 2 3 4 6 7 8
3 5 9 10
```

`grupe.out`
```
3 4
2 1
NO
```

## Explanation

The number of children in the first group is $7$ and in the second group $3$, so they differ by more than $1$ child.