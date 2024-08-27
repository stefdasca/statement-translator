# Missing Digit

In the year $2070$, due to inflation, Demiurgu is dealing with huge sums of money. Since he likes permutations (second to money), every time he spends, it is done by permuting the digits of the total amount in his account. When Demiurgu asks for a receipt to see how much money he has left in his account, due to nervousness and sweat accumulating in his trembling palms, one digit from the current balance gets erased. Help Demiurgu find out which digit is missing.

##  Task

Given a string of digits representing Demiurgu's current account balance after the small accident mentioned earlier, determine the missing digit.

##  Input data

The input file `cifralipsa.in` will contain on the first line $T$ representing the number of tests in the file. The following $T$ lines will each contain a string of digits for which you need to find the missing digit.

##  Output data

The output file `cifralipsa.out` will contain $T$ lines, where the $i$-th line contains the result for the $i$-th test.

##  Constraints and clarifications

$1 \leq T \leq 10$

Demiurgu will not spend more than he has in his account

The number of digits on each line will not exceed $100\ 000$

Demiurgu knows that the missing digit was not the digit $'0'$

A test can start with the character $'0'$

For each test, the existence of a solution is guaranteed 

##  Example

`cifralipsa.in`
```
2
44086
367179073
```

`cifralipsa.out`
```
5
2
```

##  Explanation

For the first test, the initial sum is $543\ 210$, and the spent value is $102\ 345$. The remaining balance after purchases is $440\ 865$ and the last digit is erased.

For the second test, the initial sum is $5\ 152\ 535\ 658$, and the spent value is $1\ 525\ 356\ 585$. The remaining balance after purchases is $3\ 627\ 179\ 073$ and the third digit is erased.