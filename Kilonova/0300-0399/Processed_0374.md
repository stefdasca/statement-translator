Given an initially empty list of numbers. Toor wants to complete this list by adding numbers that he considers important for the GCD. At each moment, he wants to know the GCD of all the numbers currently in the list. Sometimes, he removes a number that is in the list to add others later. By convention, the GCD of a set with $0$ elements is $1$.

Thus, the operations are of the type:
* $+X$ - add a number to the list
* $-X$ - remove a number from the list

# Task

Determine the GCD of the current set of numbers after each operation.

# Input data
The first line of the file `toorcmmdc.in` contains a natural number $N$.
The following $N$ lines contain the given operations.

# Output data

The output file `toorcmmdc.out` will contain $N$ lines, each with the required answer.

# Constraints and clarifications

* $N \leq 10^5$. Each value is less than $10^9$;
* For 30% of the tests, $N \leq 10^3$;
* If a number is not in the list, the removal will be ignored. If it is present multiple times, it will be removed only once.

# Example

`toorcmmdc.in`
```
5
+ 2
+ 6
+ 12
- 2
+ 9
```

`toorcmmdc.out`
```
2
2
2
6
3
```

## Explanation

After the first operation, the set contains only the element $2$. After the fourth operation, the set contains the elements $\\{6, 12\\}$.