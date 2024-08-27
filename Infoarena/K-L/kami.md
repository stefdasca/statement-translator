## Task

On Mount Athos Olimp, there are $N$ levels. For each level, the amount of snow $z_i$ is known. Zeus can strike a level with lightning and cause an avalanche starting from there. The avalanche phenomenon on a level $i$ proceeds as follows: the snow from level $i$ falls to level $i - 1$. If the quantity of snow on level $i-1$ is greater than or equal to the quantity of snow on level $i$, then the avalanche stops. If not, the snow quantities add up and the avalanche continues further down by one level. $M$ operations of 2 types are given:
$0\ x\ val$ - Poseidon changes the value on level $x$ to $val$
$1\ b$ - Athena wants to know if Zeus strikes level $b$ with lightning and causes an avalanche from there, what would be the level $a$ where the avalanche would stop?

## Input data

The input file `kami.in` will contain on the first line $N$. The second line will contain $N$ natural numbers representing $z_i$. The third line will contain $M$ and the next $M$ lines will contain the $M$ operations.

## Output data

The output file `kami.out` will contain one response for each question asked by Athena, representing the position where the avalanche stops. If the avalanche does not stop even at position $1$, we consider that it stops at $0$.

## Constraints and clarifications

$1 \leq N \leq 100\ 000$  

$1 \leq M \leq 100\ 000$  

$1 \leq z_i \leq 1\ 000\ 000\ 000$  

## Example

`kami.in`
```
5
10 4 1 2 3
4
1 4
1 5
0 1 9
1 5
```

`kami.out`
```
2
1
0
```