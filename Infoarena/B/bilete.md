# Tickets

In a large metropolis of a country in SE Europe, people still travel without paying for tickets $\dots$ The bus tickets in that city have a $N \times N$ grid of squares, of which the punching machines punch exactly $K$ squares. The ticket can be inserted into the machine only at one end (the other end being attached to the spine), but it can be inserted either face up or face down. In this way, some of the possible configurations of $K$ holes in the $N \times N$ grid are mirror reflections of other configurations. For $N=3$ and $K=2$, the tickets below are reflections of each other (the black squares are considered punched): A seasoned fare dodger collects perforated tickets and wants to catalog all possible configurations of holes, ignoring the reflections (since theoretically, they represent the same configuration). To this end, he encodes each configuration by a sequence of the form $l_1 c_1 l_2 c_2 \dots l_k c_k$, where $(l_i, c_i)$ are the coordinates of the $i$-th hole relative to the top-left corner of the ticket. The holes are thus numbered from left to right and from top to bottom. If the fare dodger encounters two configurations that are reflections of each other, he will classify only the lexicographically smallest one. For example, among the two tickets above, he will keep the one with the code $1123$, because, alphabetically, it is smaller.

## Task

Print in lexicographical (alphabetical) order the codes of the tickets cataloged by the fare dodger.

## Input data

The first line of the input file `bilete.in` contains two natural numbers $N$ and $K$, the size of a ticket, respectively, the number of holes that the puncher can make in any bus ticket of the metropolis. The two numbers are separated by exactly one space.

## Output data

The output file `bilete.out` will contain all possible configurations that are kept by the fare dodger, ordered alphabetically.

## Constraints

$1 \leq N \leq 9$  
$1 \leq K \leq 3$  
Any attempt to avoid paying the fare is penalized with a fine.

## Example

`bilete.in`
```
3 2
```

`bilete.out`
```
1112
1113
1121
1122
1123
1131
1132
1133
1221
1222
1231
1232
2122
2123
2131
2132
2133
2231
2232
3132
3133
```