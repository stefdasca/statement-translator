# Groups

Before starting with computer science, Bronzarel had another occupation, namely he was an animal trader. Since he gave up this profession for computer science, he now has to sell his animals. At the market, he cannot sell just one animal; he has to sell them in groups, each group consisting of exactly $K$ animals of distinct types.

## Task

Knowing that Bronzarel had $N$ types of animals, and the quantity $A_i$ of each type, determine the maximum number of groups he can form to sell at the market.

## Input data
The first line of the file `grupuri.in` will contain the natural numbers $K$ and $N$. The next line will contain $N$ natural numbers $A_1, A_2, \dots, A_N$ representing the quantities available for each type of animal. The quantities will be given in ascending order $($ $A_i \leq A_{i+1}$ $)$.

## Output data
The first line of the file `grupuri.out` will contain a single value representing the maximum number of groups that can be formed.

## Constraints and clarifications

$1 \leq K \leq N \leq 100\ 000$ 

$0 \leq A_i \leq 1\ 000\ 000$ 

For at least 60$\%$ of the tests 

$N \leq 50$ 

## Example

`grupuri.in` 
```
3 4 
3 3 3 3
```
`grupuri.out` 
```
4
``` 

`grupuri.in` 
```
5 7 
1 2 3 4 5 6 7
```
`grupuri.out` 
```
1
```

## Explanation

Assuming the animals are cows, horses, sheep, and chickens, a distribution into groups could be: 
$($ cow, horse, sheep $)$ 
$($ cow, horse, chicken $)$ 
$($ cow, sheep, chicken $)$ 
$($ horse, sheep, chicken $)$ 

We will now consider that the types of animals are numbered from $1$ to $7$
$($ $1, 3, 5, 6, 7$ $)$ 
$($ $2, 4, 5, 6, 7$ $)$ 
$($ $2, 4, 5, 6, 7$ $)$ 
$($ $3, 4, 5, 6, 7$ $)$ 
$($ $3, 4, 5, 6, 7$ $)$