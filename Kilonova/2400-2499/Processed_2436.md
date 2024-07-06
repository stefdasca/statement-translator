Adi just opened a fast-food restaurant that serves only burgers. To start the business, Adi cooked $x$ classic burgers, $y$ cheeseburgers, and $z$ vegan burgers on the first day.

Adi, being a great businessman, wants the restaurant to operate in a very strict manner and serve customers according to well-defined rules. For each customer, he creates a unique menu. The menu is created as a selection of burgers that the customer will be served, following these rules:
* Each customer receives at least one burger (of any kind), which means the menu is not empty;
* Each customer can receive at most one burger of each kind, which means the menu does not have more than one burger of each kind;
* Each customer must have a different set of burgers from the others, which means the menu, representing a subset of burger types, must be unique for each customer.

What is the maximum number of customers Adi can serve?

# Task

Given $x$, $y$, $z$, determine:
1. The total number of burgers Adi has available.
2. The maximum number of customers Adi can serve.

# Input data

The input file `burger.in` contains:
The first line contains an integer, $C$.
The second line contains $T$, the number of test cases.
The following $T$ lines contain $x$, $y$, and $z$, representing the number of burgers of each type.

# Output data

If $C = 1$, the output file `burger.out` will contain $T$ numbers, each on a separate line, representing the total number of burgers for each test case.
If $C = 2$, the output file `burger.out` will contain $T$ numbers, each on a separate line, representing the maximum number of customers that can be served for each test case.

# Constraints and clarifications

* $1 \leq T \leq 500$;
* $1 \leq x, y, z \leq 10$;
* $C \in \{ 1, 2 \} \rightarrow$ represents the task to answer in the $T$ test cases;
* For correct resolution of task $1$, $20$ points will be awarded;
* For correct resolution of task $2$, $80$ points will be awarded.

# Example 1

`burger.in`
```
1
7
1 2 1
0 0 0
9 1 7
2 2 3
2 3 2
3 2 2
4 4 4
```

`burger.out`
```
4
0
17
7
7
7
12
```

# Example 2

`burger.in`
```
2
7
1 2 1
0 0 0
9 1 7
2 2 3
2 3 2
3 2 2
4 4 4
```

`burger.out`
```
3
0
4
5
5
5
7
```

## Explanation

For $C = 1$, the total number is calculated for each test case ($1 + 2 + 1 = 4$, $9 + 1 + 7 = 17$, $\dots$).

For $C = 2$, in the first test Adi can form the $3$ sets: $\{$classic burger$\}$, $\{$cheeseburger$\}$, $\{$cheeseburger, vegan burger$\}$. In the third test, Adi can form the following $4$ menus: $\{$classic burger, cheeseburger, vegan burger$\}$, $\{$classic burger$\}$, $\{$vegan burger$\}$, $\{$classic burger, vegan burger$\}$. Although not all products were used, Adi cannot serve other customers.