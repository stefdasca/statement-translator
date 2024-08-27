## Beers

After another exhausting week at university, Gapdan, a student at FMI Unibuc, wants to go out to drink beer. His favorite bar has $N$ types of beer. Our student wants to drink exactly $K$ beers. Each beer has a price of $C[i]$ lei ( $1 \leq i \leq N$ ), as follows: the first beer has the price $C[1] = Q$ ( $Q$ is a given natural number). The next $N-1$ beers have prices determined by the following formula: $C[i] = ( C[i-1] * X + Y ) \% Z + K$ ( $X$, $Y$, $Z$ are given natural numbers). Since he has just received his scholarship, he wants to spend as much money as possible. It is known that Gapdan, being a professional drinker, drinks one beer per minute without taking any breaks (not even to go to the bathroom) and, most importantly, he does not like to drink the same type of beer more than once. Additionally, since it is game day, the bar has a special offer: the price of all beers decreases by 1 leu per minute.

## Task

Determine the maximum amount of money Gapdan can spend. 

## Input data

The input file `beri.in` contains on the first line 2 natural numbers: $N$ and $K$, with the meanings from the statement. The next line contains 4 natural numbers $Q$, $X$, $Y$, and $Z$. 

## Output data

The output file `beri.out` will contain on the first line a single number representing the required value. 

## Constraints

$1 \leq K \leq N \leq 10^6$

$1 \leq Q, X, Y, Z \leq 10^9$

You do not need to worry that Gapdan might get drunk.

## Example

`beri.in` 
```
4 2 3 2 5 16
```

`beri.out` 
```
29
```

## Explanation

The initial prices of the beers are $3$, $13$, $17$, and $9$. Gapdan drinks the beer costing $17$. Then the prices decrease by 1 leu and become $2$, $12$, $16$, and $8$. Gapdan drinks the beer costing $12$ and goes home. In total, he spent $17 + 12 = 29$ lei, the maximum possible.