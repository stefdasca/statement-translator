> *National College “Frații Buzești�* ~[logos.png|align=right|width=20rem]
> *Training Center for Informatics Performance*
> **InfoCNFB** - Edition II, Seniors
> December 9, 2023

# Task

We define the *KMedia* of an array of natural numbers as the arithmetic mean of all the elements of the array after removing the largest $k$ numbers and the smallest $k$ numbers. 
For example: for the array $1 \\ 7 \\ 4 \\ 2 \\ 5 \\ 9$ and $k = 2$, the *KMedia* of the array is $(4 + 5)/ 2 = 9/2 = 4$, where $/$ is the quotient of the division operation on natural numbers.

Three natural numbers $n$, $m$, $k$ and an array of $n$ integers are given, for which we need to calculate the sum of the KMedias of all subarrays of length $m$ modulo $1 \\ 000 \\ 000 \\ 007$.

# Input data

The first line of the file `kmedie.in` contains the three natural numbers $n$, $m$ and $k$. The next line contains $n$ natural numbers representing the elements of the array.

# Output data

The file `kmedie.out` will contain a single number representing the sum of all KMedias of subarrays of length $m$ of the array, modulo $1 \\ 000 \\ 000 \\ 007$.

# Constraints and clarifications

* $1 \\leq k,n,m \\leq 300 \\ 000$;
* $2 \\times k \\lt m \\leq n$;
* The elements of the array are natural numbers from the interval $[1; 1 \\ 000 \\ 000]$;
* For $31$ points we have $k, n, m \\leq 1 \\ 000$;
* For another $27$ points we have $k = 1$;
* For the remaining $42$ points there are no additional constraints.

# Example

`kmedie.in`
```
10 6 2 
3 1 7 4 2 5 9 3 10 2
```

`kmedie.out`
```
19
```

## Explanation

* The first subarray is $3 \\ 1 \\ 7 \\ 4 \\ 2 \\ 5$, whose KMedia is $(3+4)/2=7/2=3$;
* The second subarray is $1 \\ 7 \\ 4 \\ 2 \\ 5 \\ 9$, whose KMedia is $(4+5)/2=9/2=4$;
* The third subarray is $7 \\ 4 \\ 2 \\ 5 \\ 9 \\ 3$, whose KMedia is $(4+5)/2=9/2=4$;
* The fourth subarray is $4 \\ 2 \\ 5 \\ 9 \\ 3 \\ 10$, whose KMedia is $(4+5)/2=9/2=4$;
* The fifth subarray is $2 \\ 5 \\ 9 \\ 3 \\ 10 \\ 2$, whose KMedia is $(5+3)/2=8/2=4$.

The sum of all KMedias is $3+4+4+4+4 = 19$, which modulo $1 \\ 000 \\ 000 \\ 007$ remains $19$, because $19 \\ \\% \\ 1 \\ 000 \\ 000 \\ 007 = 19$.