# Task

Alex, with the fresh money received from the Olympiads, has decided to invest in cryptocurrencies. Initially, he possesses $1$ `BTC` and wishes to increase this amount. To achieve this, he will conduct trades over the next $N$ days.

On the platform Alex uses, there are $K$ cryptocurrencies, numbered from $1$ to $K$, where $1$ represents `BTC`.

Each day, Alex receives a list of available exchanges in the form of a matrix $A$, where $A[i][j]$ means he can exchange an amount $x$, not necessarily the entire amount, from currency $i$ to $A[i][j] \cdot x$ in currency $j$. Each transaction takes exactly one day to process, so Alex cannot use the exchanged funds on the same day. Alex can choose not to make any exchange on a given day.

# Task

After the $N$ days, Alex wants to have as much `BTC` as possible. Determine the maximum amount of `BTC` he can end up with. Note, as this value might not be an integer, you must display the result with a maximum error of $10^{-6}$ (see the output section for additional details and code).

# Input data

The first line will contain $N$ and $K$, the number of days and the number of cryptocurrencies, respectively. There will follow $N$ matrices of $K$ rows by $K$ columns. For a matrix, the number on row $i$ and column $j$ represents the exchange rate on that day for trades from $i$ to $j$. The matrices will contain real numbers $ 10^{-5} < A[i][j] < 10^5 $.

# Output data

Print the real number $x$, which represents the maximum amount of `BTC` Alex can end up with. Since $x$ is a real number, your answer must have a relative error of at most $10^{-6}$.

It is guaranteed that for the final answer: $x \leq 10^{13}$.

Let $x_{\textrm{real}}$ be the correct answer and $x_{\textrm{conc}}$ the contestant's answer. Points will be awarded if:

$$
\left|\frac{x_{\textrm{conc}}}{x_{\textrm{real}}} - 1\right| \leq 10^{-6}
$$

To ensure calculation precision, we suggest using the `double` or `long double` data type and including the following in your program:

```cpp
#include <iomanip>
#include <iostream>

// ...

std::cout << std::fixed << std::setprecision(10) << x;
```

# Constraints and clarifications

* $1 \le N \le 80$;
* $1 \le K \le 50$;
* $10^{-5} < A{[}i{]}{[}j{]} < 10^5$ for any $i$ and $j$.

|#| Score | Constraints | 
|-|-------|-------------|
|1| 15    | $N = 1$ |
|2| 15    | $K = 2$ |
|3| 20    | $N, K \leq 8$ |
|4| 50    | No additional constraints |

# Example

`stdin`
```
1 3
2.0 1.0 2.5
1.4 1.0 3.14159265359
3.0 3.0 3.0
```

`stdout`
```
2.0000000000
```

## Explanation

$N = 1$, so we have a single day of exchanges. We will name currency $2$ `ETH` and currency $3$ `TON` for simplicity in explanations. The possible exchanges here are:

-----

* `BTC` -> 2.0 $\\cdot$ `BTC` (we will not comment on the ethics of Alex's investments)
* `BTC` -> 1.0 $\\cdot$ `ETH`
* `BTC` -> 2.5 $\\cdot$ `TON`

-----

* `ETH` -> 1.4 $\\cdot$ `BTC`
* `ETH` -> 1.0 $\\cdot$ `ETH`
* `ETH` -> 3.14159265359 $\\cdot$ `TON`

-----

* `TON` -> 3.0 $\\cdot$ `BTC`
* `TON` -> 3.0 $\\cdot$ `ETH`
* `TON` -> 3.0 $\\cdot$ `TON`

-----

**Attention!** A transaction takes $24$ hours to complete, so Alex cannot use $2$ transactions on the same day. Thus, he CANNOT do `BTC` -> `ETH` -> `BTC` with the rates from a single day. However, he can do `BTC` -> `ETH` on one day and `ETH` -> `BTC` on a subsequent day. In this example, the optimal solution is taking `BTC` -> 2 $\\cdot$ `BTC`.