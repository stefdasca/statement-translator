## Task

While trying to start a business in Izbiceni, Fane began studying the vegetable market. He observed that there are $N$ types of vegetables, numbered from $1$ to $N$, that can be bartered but only according to certain fixed rules. He learned from his friend Emil which types of exchanges can be made in the market and now he wonders: if he manages to monopolize a certain type of vegetable, how many different types of vegetables can he own at most if he uses barter at the market. Since he doesn't know exactly which vegetable to invest in at the moment, Fane wants to find out this information for each of the $N$ types of vegetables.

## Input data

The first line of the input file contains the number $N$, representing the number of types of vegetables existing in the market. The lines $i+1$ contain a number representing the number of types of vegetables into which the vegetables of type $i$ can be exchanged, followed by their order numbers.

## Output data

The output file must contain the $N$ required numbers on the first line.

## Constraints

$1 \leq N \leq 250.000$

On the Izbiceni Vegetable Market, there are at most $3.000.000$ exchange relations that can be made.

If one type of vegetable can be exchanged for another, the inverse relation is not implicit.

Fane is sure that there are no more than $7.777$ types of vegetables $A$ with the property that if they can be exchanged into vegetables of type $B$, then vegetables of type $B$ cannot be exchanged into vegetables of type $A$ or $B > A$.

## Example

`control.in`
```
7 
2 5 
2 0 1 
2 3 3 
5 1 2 1 2 3 
1 2 
3 2 5 6 
3 1 2 5 
```

`control.out`
```
3 5 6 
```