Little Gates has always been passionate about mathematics since he was young. He decided that it's time to learn the multiplication table and the powers table, in an attempt to expand his knowledge.

However, he didn't stop there and decided that his next project would be the creation of a special table where the elements of the multiplication table are squared. Gates's problem is that he doesn't know how to design this table.

The first table for $n = 3$ and $m = 4$ is:

| | | | |
|-|-|-|-|
|1|2|3|4|
|2|4|6|8|
|3|6|9|12|

And the second table for the same $n$ and $m$ is:

|  |  |  |  |
|--|--|--|--|
|1 | 4| 9|16|
|4 |16|36|64|
|9 |36|81|144|

Help Little Gates solve the following task:

# Task

What is the value at position $k$ in the sorted sequence formed from all numbers present in both tables?

# Input data

The first line of the input file `tabele.in` contains the dimensions of the table $n$, $m$, and $k$.

# Output data

The output file `tabele.out` contains a single line where the required value is present.

# Constraints and clarifications

* $n, m \leq 10\ 000$;
* For $37\%$ of the score, $n, m \leq 100$;
* For $65\%$ of the score, $n, m \leq 1\ 500$.

# Example 1

`tabele.in`
```
3 4 5
```

`tabele.out`
```
3
```

# Example 2

`tabele.in`
```
3 4 20
```

`tabele.out`
```
36
```

## Explanation

The array formed by the union of both tables and their sorting is: 
$1$, $1$, $2$, $2$, $3$, $3$, $4$, $4$, $4$, $4$, $6$, $6$, 
$8$, $9$, $9$, $9$, $12$, $16$, $16$, $36$, $36$, $64$, $81$, $144$.