The following algorithm is given:
```
read  k , n; 
s = 0; 
for (i1 = 1 ; i1 \leq k ; i1++) 
    for (i2 = 1 ; i2 \leq i1 ; i2++) 
        for (i3 = 1 ; i3 \leq i2 ; i3++) 
            ........................................ 
                for (in = 1 ; in \leq in-1 ; in++) 
                    s = s + in; 
write s; 
stop.
```
# Task

Write a program that implements the above algorithm.

# Input data

The input file `implementare.in` contains two natural non-zero numbers $k$ and $n$ separated by a space, with the meanings given above.

# Output data

The output file `implementare.out` will contain on the first line the remainder of the division of the value $s$, calculated by the algorithm, by $666 \ 013$.

# Constraints and clarifications

* $1 \leq k, n \leq 50 \ 000$;
* 40\% of the tests have $k$ and $n \leq 500$;
* 20\% of the tests have $k$ and $n \geq 5 \ 000$;

# Example 1

`implementare.in`
```
3 2
```

`implementare.out`
```
10
```

## Explanation

$k=3$ and $n=2$. The first for statement executes for all values of its counter $i_1$ between $1$ and $3$ and the algorithm will contain exactly $2$ nested for statements. The second for statement executes for all values of its counter $i_2$ between $1$ and $i_1$ and calculates first $1$ then $1+2$ and finally $1+2+3$. The total sum calculated by the algorithm is $10$.
