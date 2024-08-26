## Task

Let $P$ be a permutation of the numbers from $1$ to $N$. Let $S(P) = \{ s \ | \ the \ first \ s \ numbers \ of \ P \ are \ a \ permutation \ of \ the \ numbers \ from \ 1 \ to \ s \}$. In other words, $S(P)$ represents the set of prefixes of $P$ (excluding the empty prefix) that are also a permutation. Calculate how many permutations $P$ of length $N$ have the property that $|S(P)| = K$. 

## Input data

The input file `permutari2.in` contains the first line with two natural numbers $N$ and $K$ separated by a space. 

## Output data

In the output file `permutari2.out` you will print the answer modulo $10007$. 

## Constraints and clarifications

$1 \leq N \leq 300$

$1 \leq K \leq N$

## Example

`permutari2.in`  
`8 4`

`permutari2.out`  
`531`