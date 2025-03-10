In Romania, the bear population is continuously growing. Researchers from the Institute of the Future (IV) have decided to study this phenomenon more closely, analyzing the behavior of a small bear population under special conditions and in a confined space.

They found that a "family" consisting of 2 bears (male and female) has, on average, $a$ cubs. We assume an equal number of males and females are born. Thus, in a simplistic mathematical model, the number of bears multiplies by $\\frac{a}{2}$ from one generation to the next. Additionally, there are small migrating groups of bears. These do not participate in the propagation of the species and are treated separately. Researchers have observed that from one generation to the next, on average, $b$ "foreign" bears arrive in the studied space, and $c$ "foreign" bears leave.

In short, if in one generation there are $x$ "native" bears and $y$ "foreign" bears, in the next generation there will be $\\frac{ax}{2}$ "native" bears and $y + b - c$ "foreign" bears.

The most important conclusion drawn by the researchers is that both the population of "native" bears and the population of "foreign" bears grow strictly.

# Task

At the beginning of the study (generation 1), there are $x$ "native" bears and no "foreign" bears.

Given: the task number ($t$) and $q$ queries, each containing a number $n$. Depending on the task number, determine:

1. How many bears will exist in total in generation $n$?
2. The space, being confined, allows for a maximum of $n$ bears in total. Up to which generation can the experiment be conducted without exceeding the limit of $n$ bears?

# Input data

The first line contains two natural numbers, $t$ (task number) and $q$ (number of queries).

The second line contains a natural number, $x$ (initial number of bears) and three **positive decimal real** numbers, $a$, $b$ and $c$, with the meaning described in the statement (characterizing the population growth).

The next $q$ lines each contain a natural number $n$ (generation number for task 1 and maximum number of bears for task 2).

# Output data

The $q$ lines of the output will contain the answers to the queries. Line $i$ will contain the answer to question $i$. All numbers displayed will be **natural numbers**. In the case of the first task, the answer to the query will be **rounded** to the nearest integer.

**To display the `double` variable `x` rounded to the nearest integer, include the `cmath` library and use the instruction `std::cout << (long long)std::round(x);`.**

# Constraints and clarifications

* It is recommended to use the `double` data type (instead of `float`) for representing real numbers.
* $t \\in \\{1, 2\\}$
* $1 \\leq q \\leq 10^6$
* $2 \\leq x \\leq 10$
* $2 < a < 4$
* $0 \\leq c < b \\leq 10^9$
* The study lasts for a maximum of $500$ generations.
* The maximum number of bears in a generation is $10^{14}$.
* For task 1, it is guaranteed that $n$ is at least equal to $1$ and strictly less than the number of the first generation in which the number of bears exceeds $10^{14}$ for each query.
* For task 2, it is guaranteed that $n$ is at least equal to $x$ and at most equal to the number of bears in generation $500$ for each query.
* You will receive 40 points for solving task 1 and 60 points for solving task 2.
* For fast input and output, it is recommended to use these lines of code at the beginning of the `main` function:
```cpp
ios::sync_with_stdio(false);  
cin.tie(NULL);  
cout.tie(NULL);  
```

# Example 1

`stdin`
```
1 4
6 2.45 7.55 3.88
3
1
5
2
```

`stdout`
```
16
6
28
11
```

## Explanation

We solve the first task; we have four queries. Initially, there are 6 "native" bears, and $a = 2.45$; $b = 7.55$; $c = 3.88$.

In the second generation, there will be approximately $\\frac{6\\cdot 2.45}{2} = 7.35$ "native" bears and $0 + 7.55 - 3.88 = 3.67$ "foreign" bears.
In the third generation, there will be approximately $\\frac{7.35\\cdot 2.45}{2} = 9.00375$ "native" bears and $3.67 + 7.55 - 3.88 = 7.34$ "foreign" bears. In total, $9.00375 + 7.34 = 16.34375$ bears. This number rounded to the nearest integer is $16$, so $16$ will be displayed.

The same process is followed for the other queries.

# Example 2

`stdin`
```
2 3
6 2.45 7.55 3.88
12
8
29
```

`stdout`
```
2
1
5
```

## Explanation

We solve the second task; we have three queries. Initially, there are 6 "native" bears, and $a = 2.45$; $b = 7.55$; $c = 3.88$.

Using the calculations made earlier, in the first generation there are $6$ bears, in the second generation there are $7.35 + 3.67 = 11.02$, and in the third $16.34375$. The experiment can only be conducted up to the second generation without exceeding the limit of $12$ bears.

The same process is followed for the other queries.