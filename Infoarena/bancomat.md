# ATM

Consider an ATM containing 6 types of banknotes, each type with a different value. The 6 possible values are: 1 leu, 5 lei, 10 lei, 50 lei, 100 lei, and 500 lei. For each type, there is a finite number of banknotes contained in the ATM.

## Task

During the course of a day, $N$ clients come to withdraw money from the ATM. Knowing, for each client, the amount of money they want to withdraw and the number of banknotes of each type present in the ATM, the task is to determine if it is possible to offer each client the desired amount of money. 

## Input data

The first line of the input file `bancomat.in` contains a single value $T$ which indicates the number of days for which you need to provide an answer. Following this are the input data for each individual day.

For each day, there will be 3 lines:

The first line will contain 6 values separated by a space, representing the number of banknotes of each type in the order: $1$, $5$, $10$, $50$, $100$, $500$.

The second line will contain a single value $N$ which signifies the number of clients on that day.

On the third line, there will be $N$ values representing the amount of money each client intends to withdraw, in the order in which they come to the ATM that day.

## Output data

The output file `bancomat.out` will contain $T$ lines. On each of the $T$ lines will be the word "YES" (without quotes) if it is possible to provide each client the desired amount of money on that day, or "NO" (also without quotes) if it is not. The $T$ lines correspond to the days in the input file in the order they were read.

## Constraints and clarifications

$1 \leq T \leq 50$ 

$1 \leq N \leq 5000$ 

$0 \leq Banknote \leq 230$ 

$0 \leq Amount \leq 230$ 

$Banknote$ represents the value for any of the 6 possible types of banknotes.

$Amount$ represents the amount of money for any of the $N$ clients withdrawing from the ATM.

Attention!!! The ATM must offer the exact amount to each client. In other words, it cannot give more money to a client to cover the desired amount.

## Example

`bancomat.in` 

```
3
4 3 2 0 0 0
2
17 15
1 3 10 0 0 0
2
6 3
99 99 99 99 99 0
4
233 213 233 244
```

`bancomat.out` 

```
YES
NO
YES
```

## Explanations

There are 3 days in which the ATM is used.

On the first day, the ATM contains 4 banknotes of 1 leu, 3 banknotes of 5 lei, and 2 banknotes of 10 lei. The first client who comes to the ATM wants to withdraw 17 lei and receives two 1 leu banknotes, one 5 lei banknote, and one 10 lei banknote. The second client wants to withdraw 15 lei and receives one 5 lei banknote and one 10 lei banknote.

On the second day, the first client comes to the ATM and receives one 1 leu banknote and one 5 lei banknote to cover the 6 lei they want. The second client wants to withdraw 3 lei, but the ATM no longer contains any 1 leu banknotes; hence, it cannot offer the desired amount to all clients.

