# Tequila

Returning home from ONI, Antonio is walking through the Public Garden in Barlad with his best friend, Zetul. Antonio tells Zetul the following problem, which will be given at JBOI 2016 (a sure thing, found out by Antonio): Antonio imagined a company with $N$ employees, numbered from $1$ to $N$. Each employee in the company has a direct boss (except for the supreme boss), and each employee has the supreme boss as an indirect boss. It is also known that every member of the company (including the supreme boss) has an associated value, $v_i$. There are $2$ types of operations:

1. Update: The new value associated with employee $i$ will be $v_i$;
2. Query: As long as the supreme boss is not fired, Zetul randomly selects an employee $i$ and will have to drink $v_i$ tequila shots, and then he will fire both $i$ and all employees who have $i$ as an indirect boss.

Antonio is curious about how many tequila shots Zetul will drink on average (expected value).

## Task

For the initially associated values, as well as after each update operation, Antonio will ask you to find the answer to the query operation.

## Input data

The input file `tequila.in` will contain:
- In the first line, there are two natural numbers $N$ and $Q$, representing the number of employees in the company and the number of updates, respectively;
- The next line will contain $N$ natural numbers $v_1 \dots v_N$ for each employee $i$ $(1 \le i \le N)$ initially associated value, $v_i$;
- The next $N - 1$ lines will describe the company - for each employee $i$ $(2 \le i \le N)$, their direct boss;
- The next $Q$ lines will describe the update operations in the form: $i x$ (the new value associated with $i$ is $x$, equivalent to $v_i = x$).

## Output data

The output file `tequila.out` will contain $Q + 1$ lines, representing the answer to each query.

## Constraints and clarifications

- The supreme boss will have the direct boss encoded with $-1$ (it is not necessarily the employee encoded with $1$)
- Let $b_i$ be the direct boss of employee $i$. We say that an employee $j$ is an indirect boss of $i$ if it is either $b_i$ or an indirect boss of $b_i$.
- After a query operation, Zetul will rehire all the company members.
- The displayed result will be considered correct if and only if either the absolute error or the relative error is up to $10^{-6}$. More precisely, let $x$ be the calculated answer, and $y$ the correct answer; we will accept the answer $x$ if and only if either $|x - y| \le 10^{-6}$ or $\frac{|x - y|}{y} \le 10^{-6}$.
- Antonio frequently uses the phrase "pe mangleala" and the word "gen".

Subtask 1 $(30$ points$)$: $N, Q \le 10^3$ $(Feedback test 1)$

Subtask 2 $(20$ points$)$: $N, Q \le 10^4$ and there will be no employees with the same direct boss $(Feedback test 2)$

Subtask 3 $(50$ points$)$: $N, Q \le 10^5$ $(Feedback test 3)$

## Example

`tequila.in`
```
3 1
1 1 1
-1 1 1
2 2
```

`tequila.out`
```
2.00000
3.00000
```

`tequila.in`
```
3 0
1 1 1
2 -1
```

`tequila.out`
```
1.83333
```

## Explanation

For test 1, there are $5$ possibilities to fire employees (considering the order of firings as well):

- Employee $1$ with a probability of $\frac{1}{3}$, in this case Zetul will drink $1$ shot;
- Employees $2, 1$ with a probability of $\frac{1}{6}$, in this case Zetul will drink $2$ shots;
- Employees $3, 1$ with a probability of $\frac{1}{6}$, in this case Zetul will drink $2$ shots;
- Employees $2, 3, 1$ with a probability of $\frac{1}{6}$, in this case Zetul will drink $3$ shots;
- Employees $3, 2, 1$ with a probability of $\frac{1}{6}$, in this case Zetul will drink $3$ shots;

Therefore:

For the initially associated values, Zetul will drink on average $1.83333$ tequila shots;
After the first update, Zetul will drink on average $3.00000$ tequila shots;