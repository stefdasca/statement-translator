# Arbxyz

Ojilă, in his tireless pursuit towards OJI 2016, has just found out from the dictionary that the plural of palindrome is palindromes and not palindromes, as many diligent IT people believe. Therefore, he proposes a problem with trees (make sure not to say trees in a different incorrect way, or Ojilă will get upset!). Given a tree with $N$ nodes and three values $X$, $Y$, and $Z$, where $X + Y + Z = N$. Verify if by cutting two edges from the tree, three subtrees can be obtained, each having $X$, $Y$, and $Z$ nodes, respectively.

## Task

The input file `arbxyz.in` contains on the first line a natural number $T$ representing the number of tests. Each test contains on the first line the numbers $N$, $X$, $Y$, and $Z$ separated by a space. The following $N-1$ lines contain two numbers $v$ and $w$ representing the ends of an edge in the tree.

## Input data

The input file `arbxyz.in` contains on the first line a natural number $T$ representing the number of tests. Each test contains the following lines:
* The first line contains the numbers $N$, $X$, $Y$, and $Z$ separated by a space.
* The following $N-1$ lines contain two numbers $v$ and $w$ representing the ends of an edge in the tree.

## Output data

The output file `arbxyz.out` will contain $T$ lines. Each line will have the value 1 if the division is possible, or the value 0 if it is not.

## Constraints and clarifications

$3 \leq N \leq 100 \ 000$

$1 \leq T \leq 10$

"Infatigabil" means tireless, and the plural is not "infatigabiluri"

## Example

`arbxyz.in`
```
1
8 3 2 3
2 3
4 2
2 1
1 5
1 8
5 6
5 7
```

`arbxyz.out`
```
1
```

## Explanation

For example, edges $(2,1)$ and $(1,5)$ are cut.