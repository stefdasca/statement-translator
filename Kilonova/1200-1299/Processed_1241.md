As you well know, Professor Utonium created the Powerpuff Girls by "adding sugar, spice, and everything nice, and accidentally, element $X$.â€ Element $X$ distinguishes the three girls and simultaneously defines their powers. In our problem, element $X$ is a natural number with a maximum of $6$ digits. The digits that make up this number define the girls' powers.

Mojo Jojo, the evil scientist, conducts numerous experiments trying to create villains capable of defeating the girls. Mojo Jojo creates villains by "adding" for each one an element $Y$, which is also a natural number with a maximum of $6$ digits.

The three girls fight each in turn with all the villains. After each fight, the power of the girl who fought increases by the sum of the defining elements that the villain does not have, meaning, the girlâ€™s number $X$ is increased by the sum of those digits in $X$ that do not exist in the corresponding villain's number $Y$. Moreover, the digits in the villain's number $Y$ that are not part of the girlâ€™s number are subtracted from the girl's number $X$. With the new element $X$, the girl goes to another fight.

The order of fights is: the first girl, Blossom, fights with villains $1$, $2$, $\ldots$, $n$, then the second girl, Bubbles, fights with villains $1$, $2$, $\ldots$, $n$, and then the third girl, Buttercup, fights in the same order with the $n$ villains. Note that only the elements $X$ corresponding to the girls change after each fight, and not the elements $Y$ of the villains, which remain unchanged.

# Task

Knowing the elements $X$, i.e., the three numbers that define the powers of Blossom, Bubbles, and Buttercup, the number of villains $n$, and the elements $Y$ corresponding to the villains, determine what powers the girls will have at the end of all the fights.

# Input data

It is read from the input file `powerpuff.in`:
- The first line contains three numbers: $x_1$, $x_2$, $x_3$ corresponding to the initial powers of each girl.
- The second line contains the number $n$ of villains.
- The following $n$ lines contain the numbers $Y$, corresponding to the powers of each villain: $r_1$, $r_2$, $\cdots$, $r_n$.

# Output data

The output file `powerpuff.out` will contain on one line the three numbers $X$ which correspond to the final powers of each girl.

# Constraints and clarifications

* $1 \leq n \leq 20$;
* $1 \leq x_1, x_2, x_3 \leq 999\ 999$;
* $0 \leq r_1, r_2, \cdots r_n \leq 999\ 999$;
* All input data are positive integers.
* For the chosen input data, the powers of the girls will never become negative or zero.

# Example

`powerpuff.in`
```
234 133 88
2
554
451
```

`powerpuff.out`
```
232
125
89
```

## Explanation

First, $x_1$ (value $234$) is compared with $r_1$ (value $554$). $234$ has "extraâ€ digits $2$, $3$ and "missesâ€ $5$ and $5$ so $234+2+3-5-5 = 229$. $229$ has "extraâ€ digits $2$, $2$ and $9$ and "missesâ€ $4$, $5$ and $1$ so $229+2+2+9-4-5-1 = 232$ (the final power of the first girl).

Similarly, $133+1+3+3-5-5-4 = 126$; $126+1+2+6-4-5-1 = 125$ (the final power of the second girl).

For the third girl, $88+8+8-5-5-4 = 90$; $90+9+0-4-5-1 = 89$ (the final power of the third girl).