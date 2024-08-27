Unter

Your mother asks you to call your aunt Valeria because she needs your help. Aunt Valeria tells you that she wants you to talk to her son, Hermecito, as he would like to ask you a favor. These people have no respect for your time. Your cousin Hermecito recently installed a ride-sharing application and became a driver. After each ride, he receives a rating from the client, a natural number from the interval $[1, 5]$. In an effort to ensure client safety, the application does not show Hermecito each rating but instead shows him the arithmetic mean of all the ratings received until now. This mean is truncated to $D$ decimal places (more details in the ## Constraints section). Hermecito has been suspicious from the start about this rating system, which is why he noted down the mean displayed after each ride. Now he gives you this list and asks if it is indeed possible for there to be a series of ratings that produce these means, or if the application is lying to him, conspiring against him.

And why would you have anything better to do?

## Input data

The input file `unter.in` contains on the first line the value $T$, representing the number of tests in the file. The structure of a test is as follows: the first line contains the values $N$ and $D$, representing the number of rides completed by Hermecito, and respectively the number of decimal places to which the means displayed by the application are truncated. The second line contains $N$ values, representing the series of means: the $i$-th value in the series represents the mean rating for the first $i$ rides, truncated to $D$ decimal places.

## Output data

The output file `unter.out` will contain $T$ lines. Each line will contain the string $YES$, if the corresponding series of means is possible under the given conditions, or $NO$, otherwise.

## Constraints

$1 \leq T \leq 30$

$1 \leq D \leq 5$

The sum of the values of $N$ within the same input file will be at most $300\ 000$.

Each number in the series of means will contain exactly $D + 2$ characters: A first digit in the interval $[1, 5]$, a dot, and $D$ digits in the interval $[0, 9]$. 

Truncation to $D$ decimal places keeps only the first $D$ decimal places of a number. For example, if $D = 2$, both $4.337881$ and $4.3301$ are rounded to $4.33$.

## Example

`unter.in`

```
3
3 1
1.0 3.0 3.3
2 2
4.27 5.00
3 1
1.0 2.0 4.0
```

`unter.out`

```
YES
NO
NO
```

