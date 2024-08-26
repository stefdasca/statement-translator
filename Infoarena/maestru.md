## Task

Legend has it that Master Su Elf-chi received from the gods the secrets of a magical elixir with formidable powers meant to "delight the soul". The only oath he had to take was not to exceed certain consumption concentrations of this elixir to avoid unleashing chaos in the universe. For centuries, humanity lived in peace and prosperity. However, this was to change with the appearance of brass cauldrons. The elixir broke loose and began to take on evil forms, bewildering people's minds and condemning them to eternal torment. The only chance to save humanity was for the master to do the gods' bidding and complete their trials. The first trial was to cross a river made entirely of water. The gods placed $N$ stones on this river on which the master could jump once before they sink. The positions of the stones are given as a sorted sequence of integers $x_1 , x_2 , \dots x_N$, where $x_1$ and $x_N$ represent the left and right banks of the river. Having just emerged from transcendental meditation, the master can jump from one stone to another only if the distance between them is at most a given value $P$, where by distance we mean $x_j - x_i$, for any $i$ and $j$ with $i < j$. His goal is to get from the left bank noted with $x_1$ to the right bank noted with $x_N$ and back to $x_1$. We know that the number of stones is insufficient for the master to accomplish this task, but visions caused by the evil elixir have clouded his mind. It is your duty to intervene and add a minimum number of stones to save the master from the fate of touching the water.

## Input data

The first line of the input file contains $T$, the number of tests. The first line of each test contains the numbers $N$ and $P$, followed by the next line describing the sorted sequence $x_1 , x_2 , \dots x_N$.

## Output data

The output file will contain $T$ lines, each containing an integer representing the minimum number of stones that need to be added. If there is a configuration where you can add the indicated minimum number of stones so that the master can complete his journey, the solution is considered correct.

## Constraints and clarifications

$
1 \leq T \leq 4000 
$

$
3 \leq N \leq 5000 
$

$
3 \leq P \leq 10^9 
$

$
1 \leq x_i \leq 10^9 
$

Both the positions of the stones in the input file and the positions of any newly added stones must be distinctly different from each other.

## Example

`maestru.in`
```
3
3 7
1 6 12
3 4
2 4 6
4 4
1 5 10 11
```

`maestru.out`
```
1
0
3
```

## Explanation

In the first test, the master cannot jump directly from one bank to the other; he needs the stone at position 6, and to return, we think of adding a stone at position 5. For the second test, oddly enough, the master does not need any other stone to move between the two banks. For the third test, we think of adding stones at positions 3, 6, and 9. A possible path then would be $1 \to 5 \to 9 \to 11 \to 10 \to 6 \to 3 \to 1$.