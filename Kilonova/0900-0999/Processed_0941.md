

A cuckoo clock manufacturing workshop needs plates with the hours' numbers to place on the clock disks. These numbers are printed by a printer.

Due to an error, the printer prints plates with natural numbers, some greater than $12$. The workshop can only use plates with numbers between $0$ and $12$. To use these numbers, they need to be cut starting from the right in groups of up to two digits, each group representing the value on a plate, which should be a digit from $0$ to $9$ or one of the numbers $10$, $11$, $12$. If a plate contains a number greater than $12$, then the plate must be cut so that the resulting numbers have at most $2$ digits. If the tens digit of the number on a plate is $0$, then the units digit is taken first, otherwise, if the number formed with the tens and units digits is greater than $12$, the units digit is cut first, but if the number formed with the tens and units digits is $10$, $11$ or $12$, the number formed by the last two digits is cut first, and then the process repeats until the plate is completely cut. The printer has produced $N$ plates. For example, if the plate is $12030$, after cutting we get $0$, $3$, $0$, $12$.

# Task
1. Determine the total number of occurrences of the digit $X$ on the plates before cutting.
2. Determine the number of cuts made according to the statement.

# Input data

The first line of the file `ceas.in` contains the values $C$, $X$ and $N$ separated by a single space. The second line contains $N$ natural numbers separated by a single space, having the significance from the statement. For $C = 1$ solve only task $1$, and for $C = 2$ solve only task $2$.

# Output data

The file `ceas.out` contains on the first line a single natural number representing the value calculated according to the task.

# Constraints and clarifications

* $1 \leq N \leq 100 \ 000$;
* $0 \leq X \leq 9$;
* The values in the array are natural numbers $\leq 50 \ 000$;
* For the tests where $C = 2$ the value $X$ is present in the input file even if it is not used in the solution.
* For tests worth $39$ points we have $C = 1$
* For tests worth $61$ points we have $C = 2$

# Example 1

`ceas.in`
```
1 0 6
1010 40 201 5123 31 6
```

`ceas.out`
```
4
```

## Explanation

On the plates, the digit $0$ appears four times.

# Example 2

`ceas.in`
```
2 0 6
120 40 201 5123 31 6
```

`ceas.out`
```
7
```

## Explanation

In the order of the cuts we get: {$0,12$}; {$0,4$}; {$1,0,2$}; {$3,12,5$}; {$1,3$}; {$6$}. The number of cuts is $7$.
