
# Task

Shepherd Pip lives at a sheepfold in the wilderness, along with his $k$ goats, numbered from $1$ to $k$, each having an associated value $x$. He likes mathematics as much as he likes his goats!

Working hard, Pip managed to accumulate this year a nice sum of money equal to $n$ factorial ($n!$). Because he is very pleased with this success, he has decided, in order to motivate his goats to be equally industrious next year, to reward one goat with a special shelter for her.

Pip will allocate for the construction of this shelter a sum of money within the interval $[a, b]$, but since he is a frugal man, he would prefer to spend as little as possible. Thus, he will select the shelter whose construction cost fits his budget and is the closest to the lower bound. If all costs are lower than $a$, then he will choose the largest one.

Pip designed a special algorithm to choose the winning goat. Since he likes prime numbers, he decided to build a shelter for a goat whose rank number is prime. The cost of a shelter is equal to the product of the associated value $x$ of the goat and the number of hours required for its construction, represented by the power of the goat's index in the prime factorization of the sum of money accumulated by Pip this year.

Help shepherd Pip find out which goat will have a shelter built for her.

# Input data

The first line of the input file `capre.in` contains the natural number $n$.

The second line contains the natural numbers $a$ and $b$.

The third line contains the natural number $k$.

The next line contains $k$ natural numbers, representing the value associated with each goat.

# Output data

The output file `capre.out` contains a single number $c$, representing the rank number of the chosen goat. If there are multiple goats that meet the requirements, the goat with the smallest rank number will be chosen, and if all costs are greater than $b$, no shelter will be built, and $-1$ will be printed.

# Constraints and clarifications

* $1 \le k \le 10^6$;
* $1 \le n \le 10^7$;
* $1 \le a, b \le 10^8$;
* It is guaranteed that $a < b$;
* $1 \le x \le 10^7$.

| # |   Points   | Constraints |
|:-:|:--------------:|:-------:|
| 1 |      30     |    $1 \le n \le 18$   |
| 2 | 30 |   $1 \le n \le 10^7; 1 \le k \le 10^5$    |
| 3 | 30 |   $1 \le n \le 10^7; 1 \le k \le 10^6$    |

# Example

`capre.in`
```
18 
200 225 
7 
21 15 28 9 32 17 12 
```

`capre.out`
```
3
```

## Explanation

The sum accumulated by Pip this year is $18! = 6402\ 3737\ 0572\ 8000$. 
Prime factorization: $18! = 2^{16}\times3^8\times5^3\times7^2\times11\times13\times17$. 
The goats that could be chosen are those numbered with $2, 3, 5,$ and $7$.

The cost of the shelter for goat $2$ is $240 = 16\times15$.

The cost of the shelter for goat $3$ is $224 = 8\times28$.

The cost of the shelter for goat $5$ is $96 = 3\times32$.

The cost of the shelter for goat $7$ is $24 = 2\times12$.

In this case, the cost of the shelter for goat $3$ is the only one that fits within Pip's budget, so goat $3$ is chosen.
