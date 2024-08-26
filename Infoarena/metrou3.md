# Metrou3

This problem is about the subway in Cluj. Just kidding, of course, there is no subway in Cluj. It's actually about Zalău. The subway in Zalău is a cycle with $N$ stations, the distance between two consecutive stations not being constant. These distances are given to you through the array $D$: the value $D[i]$ represents the duration of the journey between station $i$ and station $(i + 1)$ modulo $N$ in seconds. Let $T$ be the duration of a complete round of the subway (equal to the sum of the values in $D$). We know that there are only two trains: one which will be in station $0$ at second $A$, going towards station $1$, and one which will be in station $0$ at second $B$ and going towards station $N - 1$. The seconds $A$ and $B$ are some moments when the trains are at station $0$. 

They will be at station $0$ also at moments $A + k * T$ and $B + k * T$, for any integer $k$. In other words, the trains have been running forever and will continue to run forever.

We want to evaluate the efficiency of the subway in Zalău. For this purpose, we note $getTime(Start, End, EntryTime)$ as the minimum time required to get from station $Start$ to station $End$ if we are on the platform at the second $EntryTime$. To have a general picture of a regular traveler's experience, we want to calculate the value of the expression: Sum($getTime(Start, End, EntryTime)$, $0 \leq Start \leq N - 1$, $0 \leq End \leq N - 1$, $0 \leq EntryTime \leq T - 1$) modulo $(10^9 + 7)$.

## Input data

The input file `metrou3.in` will contain on its first line the values $N$ $A$ $B$. The second line will contain the $N$ values of the array $D$. 

## Output data

The output file `metrou3.out` will contain a single value representing the sum value required modulo $(10^9 + 7)$. 

## Constraints

$3 \leq N \leq 100000$

$1 \leq D[i] \leq 200000000$

$N \leq T \leq 200000000$

$0 \leq A, B \leq T - 1$

If $Start = End$, then the value of the function $getTime()$ is $0$. 

## Example

`metrou3.in`
```
3 0 0
1 1 1
```

`metrou3.out`
```
34
```

`metrou3.in`
```
4 0 1
1 1 1 1
```

`metrou3.out`
```
120
```