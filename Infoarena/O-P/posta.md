## Task

Lance recently got a job at the post office, and his job involves sorting the received letters. The letters arrive through a special device with multiple drawers arranged in a line one after another and numbered starting from $0$. To make his life easier, Lance wants to buy some collection wagons to help him gather all the letters that arrive through the device. Due to the crisis, Lance wants to minimize the number of wagons he needs. To move between two consecutive drawers, a wagon requires one second. Moreover, at the beginning of the day, Lance can position the wagons wherever he wants. Knowing that there are a total of $N$ letters and knowing for each of them the drawer and the time it arrives, find the minimum number of collection wagons needed. It must be considered that Lance wants each letter to be collected instantly, meaning that a wagon should be at the drawer at the moment of arrival.

## Input data

The input file `posta.in` contains on the first line the number $N$ of received letters. The next $N$ lines contain two numbers $S_i$ and $T_i$ representing the drawer and the time at which each letter arrives, respectively.

## Output data

The first line of the output file `posta.out` will contain a single number $V$, representing the minimum number of wagons needed. On the next line, there will be $N$ integers between $1$ and $V$, representing the wagons associated with the letters in the order from the input file.

## Constraints and clarifications

$1 \leq N \leq 100000$

$0 \leq S_i, T_i \leq 10^9$

If there are multiple solutions, any of them can be displayed.

## Example

`posta.in`

```
4
1 1
2 4
3 3
4 1
```

`posta.out`

```
2
1 2 1 2
```