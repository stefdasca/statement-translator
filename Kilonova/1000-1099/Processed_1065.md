Numim $k$ - $p$ - platou un număr $n$ de forma $c_1 c_2 \dots c_p$ cu proprietatea că cifrele sale sunt distincte și aparțin mulțimii $\{k$, $k+1$, $\dots$, $k+p-1\}$. O $\alpha$-codificare constă în transformarea numărului $n$ în numărul $d_1 d_2 \dots d_p$, unde $d_i$ = $1$ + numărul de cifre din stânga cifrei $c_i$ care sunt mai mici decât $c_i$ pentru $1 \leq i \leq p$. Aplicând o $\alpha$-codificare unui număr obținem un $\alpha$-cod.

Fie $s$ un șir format din secvențe de cifre, în care fiecare secvență are aceeași lungime $p$. Un val este o succesiune de astfel de secvențe în care orice secvență care este un $\alpha$-cod, este urmată de o secvență care nu este un $\alpha$-cod și orice secvență care nu este un $\alpha$-cod, este urmată de o secvență care este un $\alpha$-cod, cu excepția ultimei secvențe. Un val începe obligatoriu cu o secvență ce reprezintă un $\alpha$-cod și se termină cu o secvență care nu este un $\alpha$-cod.

Primul caracter al unui val se poate afla pe o poziție din $s$ care aparține mulțimii $\{1$, $1+p$, $1+2p$, $1+3p$, $\dots\}$.

# Task

Write a program that:
1. knowing the numbers $k$, $p$ and an $\alpha$-cod, determines the $k$ - $p$-plateau to which the $\alpha$-cod was applied.
2. for a given string of digits $s$, determines the length of the longest wave.

# Input data

The input file `decod.in` contains:

* the first line contains the digits $k$ and $p$ separated by a space
* the second line contains an $\alpha$-cod of a $k$ - $p$ - plateau
* the third line contains a string of digits $s$

# Output data

The output file `decod.out` will contain:

* the first line contains the $k$ - $p$ - plateau to which the $\alpha$-cod was applied
* the second line prints the length of the longest wave


# Constraints and clarifications

* $1 \leq k \leq 9$
* $1 \leq p \leq 9$
* $k + p - 1 \leq 9$
* $1 \leq d_i \leq 9$
* the string $s$ has at most $800\ 000$ characters
* For solving task 1, $40\\%$ of the score is awarded and for solving tasks 1 and 2 $100\\%$ of the score is awarded.


# Example 1

`decod.in`
```
3 5
12124
1111012124100111234511151
```

`decod.out`
```
57346
20
```

## Explanation

The number $57346$ is a $3$ - $5$ - plateau, as its digits belong to the set {$3$, $4$, $5$, $6$, $7$}. Applying an $\alpha$ - codification to it results in $12 \ 124$, $1$ because to the left of $5$ there are no digits smaller than $5$ ($1 + 0$), $2$ because to the left of $7$ there is one digit smaller than $7$ ($1 + 1$), etc.

In the string 11110**12124100111234511151** we have a wave of length $20$.


# Example 2

`decod.in`
```
8 2
12
10121011101012101110111011101110
```

`decod.out`
```
89
20
```

## Explanation

The number $12$ is a $\alpha$-cod of the number $89$.
In the string 10**12101110**10**11101110111011201110** we have two waves, and the maximum wave length is equal to $20$.

