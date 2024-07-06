Cristi, already familiar with the notion of density from physics classes, wants to study it from the perspective of computer science. Thus, he chooses an array of $N$ natural numbers $A_1, A_2, \dots, A_N$ and wants to experiment.

# Task

Calculate the number of non-empty subarrays that have the property that the ratio of even elements to the length of the subarray is exactly $D$.

# Input data

In the input file `densitate.in`, the first line contains the number $N$, which represents the length of the array. The second line contains, separated by a space, $N$ natural numbers. The third line contains the density $D$, represented with $2$ decimal places in the form $0.ab$.

# Output data

The output file `densitate.out` will contain a single line that will print the number of subarrays that satisfy the condition in the statement.

# Constraints and clarifications

* $1 \leq N \leq 100 \ 000$
* $0 \leq A_i \leq 1 \ 000 \ 000$;
* $0 \leq D \leq 0.99$ 
* By a subarray of the array $A$, we understand any succession of elements on consecutive positions $A_j, A_{j+1}, A_{j+2}, \dots, A_k$, with $1 \leq j \leq k \leq N$.

# Example

`densitate.in`
```
6
1 0 3 5 2 7
0.50
```

`densitate.out`
```
5
```

## Explanation

There are $5$ subarrays with density $0.50$: $1 \ 0$; $0 \ 3$; $5 \ 2$; $2 \ 7$; $0 \ 3 \ 5 \ 2$