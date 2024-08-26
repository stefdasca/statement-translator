## Task

An international company has $N$ employees, numbered from $1$ to $N$. They are organized in a hierarchical structure with the following properties:
- each employee has a direct superior, except for employee number $1$ who is the manager of the company
- each employee can be the direct superior of $0$, $1$, or at most $2$ other employees.

To improve the efficiency of their business, the company's owners have decided to split it into three smaller companies. In addition to other problems they had to solve, a very important one arose: how should the employees be distributed to the three newly created companies?

The following conditions need to be considered:
- each employee must be distributed to one of the three companies
- an employee and their superior should not be distributed to the same company
- if two employees have the same superior, then they must be distributed to different companies

To ensure that the three companies are equally efficient, an additional condition emerged. Let $N_1$ be the number of employees distributed to the first company, $N_2$ be the number of employees distributed to the second company, and $N_3$ be the number of employees distributed to the third company ($N_1 + N_2 + N_3 = N$). With these notations, the difference $\max(N_1, N_2, N_3) - \min(N_1, N_2, N_3)$ should be as small as possible.

## Input data

The input file `comp.in` contains on the first line a single natural number $N$, which represents the number of employees in the company. Each of the following $N-1$ lines contains two natural numbers $a$ and $b$ between $1$ and $N$, separated by a single space, indicating that employee $b$ is the direct superior of employee $a$.

## Output data

The output file `comp.out` will contain a single line with $N$ numbers, separated by spaces, from the set ${1, 2, 3}$. The first number represents the number of the company to which employee number $1$ was distributed, the second number represents the number of the company to which employee number $2$ was distributed, the third number represents the number of the company to which employee number $3$ was distributed, and so on.

## Constraints and clarifications

- $0 \leq N \leq 16000$
- $\max(a, b, c)$ represents the maximum of the values $a$, $b$, and $c$
- $\min(a, b, c)$ represents the minimum of the values $a$, $b$, and $c$
- any solution that minimizes the specified difference is accepted
- the input data is correct

## Example

`comp.in`
```
6
2 1
3 2
4 2
5 3
6 3
```

`comp.out`
```
3 1 3 2 1 2
```