# # Bottles

After shooting all the windows, Geminski returns home where he finds a note from Miss C. that reads: "On the kitchen table, you will find $N$ bottles of wine, of which exactly one is poisoned. Anyone who drinks from that bottle will surely die within 24 hours. By the time I get home, you must find out which bottle is poisoned!" Being very passionate about animals, Geminski has an almost unlimited number of chitosvarta on the balcony of his house. He wants to find the poisoned bottle by testing the wine bottles on the chitosvarta, but he wants to use as few animals as possible. Additionally, Geminski cannot use the same chitosvarta more than once, because Miss C. will arrive in less than 47 hours.

## Task

Write a program to determine the minimum number of chitosvarta needed for a given $N$ to find the poisoned bottle.

## Input data

The first line of the input file `sticle.in` contains the number of tests $T$. The next $T$ lines each contain a number $N$ on each line, representing the number of bottles for that test.

## Output data

The output file `sticle.out` will contain $T$ lines, with the required number on each line.

## Constraints

1 $\leq$ $N$, $T$ $\leq$ $50 \ 000$   
Geminski has only one day available   
A single chitosvarta can drink from multiple bottles in the same day   


## Example
`sticle.in`
```
2
3
47
```

`sticle.out`
```
2
6
```

## Explanation

For the first test, Geminski gives bottles $1$ and $3$ to one chitosvarta and bottles $2$ and $3$ to the next chitosvarta. If the first bottle is poisoned, only the first chitosvarta will die, if the second bottle is poisoned the second chitosvarta will die, if the third bottle is poisoned both will die. The second test is somewhat more complicated$\dots$