## Task

Given $N$, $B$ and $M$, calculate $G_B(N)$ modulo $M$.

## Input data

The input file `voodoo.in` contains on a single line 3 numbers separated by a single space $N$, $B$ and $M$ as described in the problem statement.

## Output data

The output file `voodoo.out` contains the value of $G_B(N)$ modulo $M$. The response should be printed in base 10.

## Constraints and clarifications

  $0 \leq N \leq 10^{18}$

  $2 \leq B \leq 10^{18}$

  $B$ will not be of the form $6k + 1$ or $9k + 1$ for any integer $k$

  $1 \leq M \leq 3^{12}$

  $M$ is of the form $3^k$ where $k$ is an integer

  For tests worth 20 points, $G_B(N) \leq 10^{18}$

  For other tests worth 50 points, $N \leq 250\ 000$
  
  Chaos.

## Example

`voodoo.in`
```
3 10 531441
199 3 9
27 26 250000
5007329433060514 531441 425803
1000000000000000000 5007329433060514 531441
384844
```

`voodoo.out`
```
213
37
24
```

## Explanation

The first example does not meet the problem's constraints (10 is of the form $9 \cdot 1 + 1$). It was included only to clarify the statement. 

The sum of the digits of $199$ is $1 + 9 + 9 = 19$. The sum of the digits of $19$ is $1 + 9 = 10$. The sum of the digits of $10$ is $1 + 0 = 1$. We calculated the sum of the digits three times, so $F_{10}(199) = 3$. This is the smallest number for which this result is obtained.

In the second example, the result is $161_{10} = 188_{9}$. The sum of the digits of $188_{9}$ is $1 + 8 + 8 = 17 \equiv 18_{9}$. The sum of the digits of $18_{9}$ is $1 + 8 \equiv 9 \equiv 10_{9}$. The sum of the digits of $10_{9}$ is $1 + 0 = 1$. We calculated the sum of the digits three times, so $F_9(161_{10}) = 3$. This is the smallest number for which this result is obtained. $161 \mod 27$ will be 26.

The last two examples are too chaotic to have an explanation.