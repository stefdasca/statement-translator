Hello Master

It took the Master $4653$ days to clean London of mobsters. Only one is left, namely the bourgeois metabalzacian Stănică Raţiu. Therefore, the Master came to Bucharest to fulfill his goal once and for all.

## Task

For an array of numbers $a$, we define the cost as the sum of the $gcd$s $\dagger$ of all prefixes of $a$. For example, the cost of the array $[12, 6, 9, 2]$ is $gcd(12) + gcd(12, 6) + gcd(12, 6, 9) + gcd(12, 6, 9, 2) = 12 + 6 + 3 + 1 = 22$. We define $f(n,k)$ as the sum of the costs of all partitions of $n$ into $k$ terms. $\ddagger$ Given $n$ and $m$, and an array $k_1, k_2, \dots, k_m$, you need to calculate $f(n, k_1), f(n, k_2), \dots, f(n, k_m)$. As these numbers can be very large, the Master asks you to display them modulo $998244353$. 
$\dagger$ By $gcd(a_1, a_2, \dots, a_i)$ we denote the greatest common divisor of the numbers $a_1, a_2, \dots, a_i$. 
$\ddagger$ By a partition of $n$ into $k$ terms, we mean an array of positive numbers $a_1, a_2, \dots, a_k$ with the property that $a_1 \cdot a_2 \cdot \dots \cdot a_k = n$.

## Input data

The first line of the file `jupanul.in` contains the numbers $n$ and $m$ separated by a space. The second line contains $m$ numbers $k_1, k_2, \dots, k_m$.

## Output data

The first and only line of the file `jupanul.out` will contain the remainders modulo $998244353$ of the numbers $f(n, k_1), f(n, k_2), \dots, f(n, k_m)$ separated by exactly one space. 

## Constraints

$1 \leq n \leq 10^{12}$

$1 \leq m \leq 1\ 500\ 000$

$1 \leq k_i \leq 1\ 500\ 000$, for any $i$ that respects $1 \leq i \leq m$

Due to the large size of the tests, it is recommended to parse input and output files

### Subtasks

* **Lucky you, Gavrilescu!** - $11$ points (tests $1-2$): $n \leq 5\ 000$, $m \leq 80\ 000$, $k_i \leq 100\ 000$
* **So much lucidity, so much drama** - $12$ points (tests $3-4$): $n \leq 100\ 000$, $m \leq 80\ 000$, $k_i \leq 100\ 000$
* **Give me back my nights** - $10$ points (tests $5-6$): $n \leq 1\ 000\ 000$, $m \leq 80\ 000$, $k_i \leq 100\ 000$
* **Only AIB should come here** - $24$ points (tests $7-10$): $m \leq 500$, $k_i \leq 200\ 000$
* **Go, but you won't forget me** - $42$ points (tests $11-15$): $m \leq 80\ 000$, $k_i \leq 200\ 000$
* **And eternity to receive as a gift** - $1$ point (test $16$): No additional constraints

## Example

`jupanul.in`

``` 
6 2 
1 2 
```

`jupanul.out`

``` 
6 16 
```

`jupanul.in`

``` 
8 1 
2 
```

`jupanul.out`

``` 
12152 
```

`jupanul.in`

``` 
8 8 
1 2 3 4 5 6 7 8 
```

`jupanul.out`

``` 
12152 27468 57294 111704 207030 369846 642894 1093344 
```

## Explanation

The number $6$ can be decomposed into $2$ terms as follows: 
* $[1, 6]$, cost = $gcd([1]) + gcd([1, 6]) = 1 + 1 = 2$
* $[6, 1]$, cost = $gcd([6]) + gcd([6, 1]) = 6 + 1 = 7$
* $[2, 3]$, cost = $gcd([2]) + gcd([2, 3]) = 2 + 1 = 3$
* $[3, 2]$, cost = $gcd([3]) + gcd([3, 2]) = 3 + 1 = 4$

So $f(6, 2) = 2 + 7 + 3 + 4 = 16$.