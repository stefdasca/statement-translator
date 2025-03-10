Mare matematician, Micul Gates is studying the following sequence of numbers: $1^n$, $3^n$, $5^n$, $7^n$, $9^n$, $11^n$, $\dots$

# Task

1. Determine the units digit of the number at position $k$ in the sequence.
2. Determine the sum of the units digits of the first $k$ numbers in the sequence.

# Input data

The first line of the input file `sir.in` contains the number $c$ of the task, which can only be $1$ or $2$. The second line contains two nonzero natural numbers, $n$ and $k$, separated by a space, with the significance described in the statement.

# Output data

The first line of the output file `sir.out` will contain the value determined according to the task.

# Constraints and clarifications

* $1 \leq n, k \leq 1 \ 000 \ 000$;
* For task 1, $32$ points are awarded;
* For task 2, $68$ points are awarded. For $12$ points, we have $n=1$.

# Example 1

`sir.in`
```
1
2 3
```

`sir.out`
```
5
```

## Explanation

The task is $1$, $n=2$, $k=3$.  
The numbers in the sequence are: $1^2$, $3^2$, $5^2$, $7^2$, $\dots$.  
The third number in the sequence is $5^2$, which is $25$ and has the units digit $5$.  

# Example 2

`sir.in`
```
2
6 10
```

`sir.out`
```
50
```

## Explanation

The task is $2$, and $n=6$, $k=10$.  
The first $10$ numbers in the sequence are: $1^6$, $3^6$, $5^6$, $7^6$, $9^6$, $11^6$, $13^6$, $15^6$, $17^6$, $19^6$.  
The sum of the units digits is $1+9+5+9+1+1+9+5+9+1=50$.