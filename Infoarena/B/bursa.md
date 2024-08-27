# The Stock Market

Gigi has an insider tip on the stock market. He knows the price $P[i]$ of a share of company X for each of the following $N$ days. Knowing that he has gathered a sum of money $S$ (from relatives and friends), display the maximum profit that Gigi can achieve. Assume that Gigi can buy any number of shares he wants each day, provided he has enough money. Also, assume that Gigi can sell any number of shares he wants each day, from those he owns. The transfer of money/shares is instantaneous.

## Input data

The input file `bursa.in` contains on the first line the number of days, $N$, and the sum of money Gigi possesses, $S$.  
The second line contains the price of a share in each of the $N$ days.

## Output data

The output file `bursa.out` will contain on the first line the maximum profit that Gigi can achieve.

## Constraints and clarifications

$1 \leq N \leq 100\,000$  
$1 \leq S \leq 10\ 000\ 000\ 000$  
$1 \leq P[i] \leq 500\ 000$  
It is guaranteed that the sum of money Gigi possesses will fit into a 64-bit integer at any moment in time.

## Example

`bursa.in`  
```
3 100
7 1 12
```

`bursa.out`  
```
1100
```

## Explanation

$N = 3$, $S = 100$.  
The shares will cost 7 lei each on the first day, 1 leu on the second, and 12 lei on the third day.  
To achieve maximum profit, Gigi should buy 100 shares on the second day and sell them all on the third day, thus achieving a profit of 1100 lei.