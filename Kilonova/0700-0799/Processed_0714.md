Every working day of the week, Pinocchio tells a lie due to which his nose grows by $p$ centimeters per day. On Saturday and Sunday, when Grandpa Geppetto comes home, to avoid upsetting him too much, Pinocchio manages not to tell any lies, and by looking in the mirror, he sees that on each of these days the length of his nose decreases by $1$ centimeter per day. When a new week begins, and he is left alone at home, Pinocchio continues his string of lies.

# Task

What is the length of Pinocchio's nose after $k$ days, knowing that initially, his nose measured $n$ centimeters?

# Input data

From the input file `pinochio.in` read the values $n$, $p$, $k$, which are contained on the first line of the file and are separated by a space.

# Output data

In the output file `pinochio.out` print on the first line a single natural number, the number of centimeters required by the problem.

# Constraints and clarifications

* $1 \leq n \leq 1\ 000$;
* $1 \leq k \leq 256$;
* $1 \leq p \leq 100$;

# Example

`pinochio.in`
```
2 1 8
```

`pinochio.out`
```
6
```

## Explanation

The days start with Monday. For the given example, the days are Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, Monday.