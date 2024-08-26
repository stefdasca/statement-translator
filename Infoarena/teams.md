## Task 

Ash wants to participate in a Pokémon contest. For that, he needs a team of 2 Pokémon whose total strength is between $A$ and $B$. He has $N$ Pokémon that he loves very much, but because he is undecided, he wants to know in how many ways he can choose a team.

## Input data 

The first line of the input file `teams.in` contains 3 natural numbers $N$, $A$, and $B$ as described above, and the next line contains $N$ numbers representing the strength of each Pokémon.

## Output data 

The output file `teams.out` will contain the number Ash wants.

## Constraints and clarifications:

$1 < N < 100001$ 

$1 < A < B < 32768$ 

The strength of each Pokémon is a natural positive number less than or equal to $32767$ 

A team is made up of exactly 2 different Pokémon

## Example 

`teams.in` 

```
8 5 8 
1 2 3 4 5 6 6 7 
```

`teams.out` 

```
12
```