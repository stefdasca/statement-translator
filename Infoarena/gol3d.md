# Gol3d

Gigel has invented a new game: game of life 3d. Let's see the rules: the game takes place inside a cube divided into cubic cells of unit volume, with dimensions $N \times N \times N$ (a total of $N^3$ cells). In each cell there is a living or dead organism. The game consists of tracking the evolution of organisms for multiple generations. In each generation, some organisms evolve according to the following rules: the neighbors of a cell located at coordinates $(i,j,k)$ $(0 \leq i, j, k \leq n-1)$ are those cells $(i',j',k')$ different from $(i,j,k)$, located at a distance less than or equal to $d = \left\lfloor \frac{i + j + k}{5} \right\rfloor + 1$ from the cell $(i,j,k)$ (the integer part of the division by 5 is considered) the distance between 2 cells $(a_1, b_1, c_1)$ and $(a_2, b_2, c_2)$ is defined as $\max \{ |a_1 - a_2 |, |b_1 - b_2 |, |c_1 - c_2 | \}$
- If a cell has strictly less than $25\%$ living neighbors, it will die of loneliness in the next generation (if it was alive)
- If a cell has strictly more than $75\%$ living neighbors, it will die of suffocation in the next generation (if it was alive)
- If a cell has between $45\%$ and $55\%$ (open interval) living neighbors, it will change its state (it will revive if it was dead / it will die if it was alive)
- If the percentage of living neighbors does not fall within the above rules, then the cell will be alive in the next generation regardless of its state in the previous generation
All births and deaths in a generation occur simultaneously (in other words, modifying a cell in one generation cannot affect the evolution, in the same generation, of any other cell)
Knowing the number of generations of the game, Gigel asks you to calculate the number of living organisms for each generation.

## Input data

The input file `gol3d.in` will contain on the first line two natural numbers: $N$ and $G$ representing the size of the cube and the number of generations of the game (including the first one). Then, for each $i$ from $0$ to $N-1$, there are $N$ lines with $N$ elements each - the element $(j,k)$ in the matrix will represent the state of the organism in the cell $(i,j,k)$ in the first generation. After each matrix, except the last one, there will be an empty line. The following encoding will be used: $0$ - dead organism, $1$ - living organism.

## Output data

The output file `gol3d.out` will contain on a single line $G$ numbers representing the number of living organisms after each generation.

## Constraints and clarifications

$2 \leq N \leq 64$

$1 \leq G \leq 100$

## Example

`gol3d.in`  
`2 2`
`0 1`
`0 0`
`0 0`
`0 1`

`gol3d.out`  
`2 6`

## Explanation

The first generation is the initial one where we have only $2$ living organisms. The next generation will be:
`1 0`
`1 1`
`1 1`
`1 0`
All cells are neighbors with each other (because the $d$ calculated according to the formula in the statement always gives $1$). The organisms in cells $(1,1,1)$ and $(0,0,1)$ have one living neighbor out of 7 (hence less than $25\%$) and die of loneliness. The other cells have $2$ living neighbors out of $7$, hence ~ $28\%$ and will be alive according to the second-last rule of the game.