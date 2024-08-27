# Parties

As you know, Rick is a big fan of parties. Whenever he goes to a party, he always aims to drink at least a certain quantity of milk. Today, he has noted down $N$ parties on his calendar, each with a number $a[i]$, the number of units of milk he wants to consume at that party. When he left for the first one, he realized that he had forgotten all his milk in another dimension and all he has is his empty bottle that can hold $T$ units of liquid. He knows that at each party, one unit of milk costs $c[i]$ money (it's not his first time there), so he wonders what the minimum amount of money he has to pay to meet his minimum requirements is, knowing that between parties he can carry only $T$ units of milk in his bottle.

## Input data

The first line of the input file `petreceri.in` contains the numbers $N$ and $T$. The next line contains $N$ numbers, the $i$-th of them being $a[i]$. The third line contains $N$ numbers, the $i$-th of them being $c[i]$. 

## Output data

The first line of the file `petreceri.out` will contain the minimum amount of money that Rick has to pay to meet his goals.

## Constraints and clarifications

Rick can only go to parties in the given order, as he does not want to use time travel. Rick can buy milk at the beginning, at the end, or anytime during a party.
$$0 \leq T \leq 10^9$$
$$0 \leq N \leq 10^6$$
$$0 \leq a[i] \leq T$$ 
$$0 \leq c[i] \leq 10^9$$
It is guaranteed that the solution will be less than $$10^{18}$$ 

For tests worth 10 points 
$$N, T \leq 2000$$ 

For other tests worth 20 points 
$$N \leq 2000$$ 

For other tests worth 30 points 
$$N \leq 200000$$ 

For other tests worth 40 points there are no additional constraints 

ATTENTION!
Given the large tests, it is recommended to parse the file `petreceri.in`. You can use the code provided here (both for C++ users with syntax similar to `fstream`, and for pure C enthusiasts)

## Example

`petreceri.in` 
```
5 2
1 1 1 1 1
1 2 3 4 5
```
`petreceri.out` 
```
8
```

## Explanation

In the first example Rick will buy 1 unit of milk at the first party and drink it on the spot, and he will buy 2 more at the end of the party to take with him. At the second party he will drink one unit of milk from the bottle and buy another one from the bar. He will do the same at the third, leaving with a full bottle. At the last 2 parties, he will finish the milk from the bottle. Thus, Rick will buy 3 units at the first party, one at the second party, and one at the third, paying $1+1+1+2+3 = 8$ money.