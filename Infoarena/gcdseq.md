Gcdseq

Teognis has in front of him a sequence of $N$ lyrical poems with distinct beauties. Teognis sells one continuous subarray of poems at a time. A continuous subarray of length $L$ with maximum beauty equal to $M$ is sold for the price of $G$ lei, where $G$ is the greatest common divisor of $L$ and $M$. Teognis suddenly received a bunch of orders, one for each possible continuous subarray. He now wonders: what is the sum of the prices of the orders that I received?

## Input data

The input file `gcdseq.in` contains on the first line $N$, the number of poems, and on the second line the beauties of the poems.

## Output data

The output file `gcdseq.out` will contain the required sum.

## Constraints

$1 \leq N \leq 100\,000$  
$1 \leq the \ beauty \ of \ a \ poem \leq 400\,000$

For 10 points, $N \leq 100$.  
For another 20 points, $N \leq 1\,000$.

## Example

`gcdseq.in`  
```
5  
1 2 3 4 5  
```

`gcdseq.out`  
```
26  
```

`gcdseq.in`  
```
10  
1 5 3 2 4 6 9 8 7 10  
```

`gcdseq.out`  
```
107  
```

## Explanation

For the first test, the price of subarray of length $1$ is $1$; the prices of subarrays of length $2$ are $gcd(2, 2) = 2$, $gcd(2, 3) = 1$, $gcd(2, 4) = 2$, $gcd(2, 5) = 1$; the prices of subarrays of length $3$ are $gcd(3, 3) = 3$, $gcd(3, 4) = 1$, $gcd(3, 5) = 1$; the prices of subarrays of length $4$ are $gcd(4, 4) = 4$, $gcd(4, 5) = 1$; and the price of the unique subarray of length $5$ is $gcd(5, 5) = 5$. Thus, the result is $5 * 1 + 2 + 1 + 2 + 1 + 3 + 1 + 1 + 4 + 1 + 5 = 26$.