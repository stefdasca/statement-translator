# Euro

You have just opened a new bank account where you will receive sums of money in euros. When you opened the account, you had neither euros nor lei. Over the next $N$ days, you will receive various sums of euros; these sums can be negative, in which case the total number of euros in the account will decrease. Sometimes it's possible to have a negative amount of money in your account. At the end of each day, the bank will allow you to convert the entire amount of euros in your account into lei. The price of one euro varies according to the following rule: on the $K$-th day, one euro can be exchanged for $K$ lei. The bank will charge a fee of $T$ lei for each conversion. Therefore, if at the end of day $K$ you have $S$ euros in your account and you decide to convert them, you will receive $S \cdot K - T$ lei in exchange for them (of course, $S$ can be negative). At the end of day $N$ you will be required to convert the entire amount of money from the account into lei, even if it is non-positive.

## Task

Your objective is to maximize the amount of lei you will have at the end of day $N$.

## Input data

The first line of the input file `euro.in` contains two integers, $N$ and $T$, separated by spaces. The next line contains $N$ integers representing the number of euros you will receive at the beginning of each day.

## Output data

The output file `euro.out` contains a single number representing the maximum amount of lei you can obtain.

## Constraints and clarifications

$1 \leq N \leq 34567$

$0 \leq T \leq 34567$

80\% of the tests will have $T \leq 255$

The number of euros you will receive each day is an integer in the range $[-1000, 1000]$

It is allowed to convert euros into lei only, not lei into euros

For the result, it is recommended to use data types like $int64$ or $extended$ in Pascal, and $long \, long$ or $long \, double$ in C/C++ (depending on your preference for real or integer numbers); it is guaranteed that the result fits within these data types, but it might be too large for other smaller data types

## Example

`euro.in`
```
7 1 
-10 3 -2 4 -6 2 3
```

`euro.out`
```
17
```

## Explanation

At the end of the first day, you will convert the $-10$ euros you received for $-11 = -10 \cdot 1 - 1$ lei. The second conversion takes place at the end of day $5$ when you have $-1$ euros in your account ($3 - 2 + 4 - 6$). The amount of lei you obtain is $-6 = (3 - 2 + 4 - 6) \cdot 5 - 1$. You will make the last conversion at the end of day $7$, using the last $5$ euros in your account ($2 + 3$). The amount of lei you obtain is $34 = (2 + 3) \cdot 7 - 1$. The final sum of lei you obtain is $17 = -11 - 6 + 34$.