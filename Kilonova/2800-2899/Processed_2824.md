~[rac1.png|align=right]

Teo goes to his favorite cafeteria (the one at ASE) to taste the new range of foods - jellies with mash.

At the jelly buffet, he has $R$ types of jellies to choose from. The $i$-th type ($0 \leq i < R$) costs $r_i$ lei. For each type of jelly, Teo, with a probability of $\\frac{1}{2}$, puts a jelly on his plate.

At the mash buffet, he has $P$ types of mash to choose from. The mash is sold by volume, so for the $i$-th type of mash ($0 \leq i < P$), Teo can serve himself with mash worth $0$, $1$, ..., $p_i$ lei. For each type of mash, Teo randomly serves himself with an allowed amount of mash.

The cafeteria offers the following discount: if the total price of the foods chosen by Teo is strictly greater than the sum of $X$ lei, then Teo gets a 50\% discount.

# Task
What is, on average, the price paid by Teo?

# Input data

The first line of standard input contains the numbers $R$, $P$, and $X$ with the meaning from the statement.

The second line contains $R$ integers: $r_0, r_1, \dots, r_{R-1}$.

The third line contains $P$ integers: $p_0, p_1, \dots , p_{P - 1}$.

# Output data

Print the answer on a single line of standard output, modulo $10^9 + 7$.

If the answer is equal to the fraction $\\frac{A}{B}$, print the number $A \\cdot B^{-1}$ (modulo $10^9 + 7$).

# Constraints and clarifications

* $1 \leq P, R \leq 100$
* $1 \leq p_i, r_i \leq 10^3$
* $1 \leq X \leq 2 \cdot 10^5$
* In the "Attachments" section on the right side of the page, you can download a [file](aritmetica_modulara_demo.cpp) that implements basic operations of modular arithmetic in C++. This is especially useful if you are not familiar with the concept of modular inverse.
* Teo knows that the correct form is _piure_ but for marketing reasons, the cafeteria continues to use the name _pireu_.

| # | Score   | Restrictions         |
| - | ------- | -------------------- |
| 1 | 20      | $P = 0$, $R \leq 20$ and $X = 2 \cdot 10^5$ (the discount never applies). |
| 2 | 20      | $P = 0$, $R \leq 20$ |
| 3 | 20      | $P = 0$ |
| 4 | 20      | $p_i \leq 5\ \\forall\\ 0 \leq i < P$      |
| 5 | 20      | No additional restrictions |

# Example 1

`stdin`
```
5 3 10
2 7 6 2 6
6 7 10
```

`stdout`
```
142806425
```

# Example 2

`stdin`
```
10 10 100
26 27 72 11 6 30 60 90 28 15
60 68 38 48 22 65 19 75 17 1
```

`stdout`
```
413422235
