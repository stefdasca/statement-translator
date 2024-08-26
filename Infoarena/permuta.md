## Task

Ojilă loves permutations. He has a permutation $a = a_1, a_2, \dots, a_n$ of the set $\{1,2,\dots,n\}$ stored in the array $a$ and constructs a new permutation in the array $b$ as follows: he takes $a_1$, adds it to $b$, takes $a_2$ and moves it to the end of $a$, takes $a_3$ and adds it to $b$, then takes $a_4$ and moves it to the end of $a$, and so on until all elements from $a$ are transferred to $b$. For example, for the permutation $a = (2, 6, 4, 1, 5, 3)$, he proceeds as follows: initially $a = (2, 6, 4, 1, 5, 3)$ $b = ()$ 
step 1 $a = (4, 1, 5, 3, 6)$ $b = (2)$ step 2 $a = (5, 3, 6, 1)$ $b = (2, 4)$ step 3 $a = (6, 1, 3)$ $b = (2, 4, 5)$ step 4 $a = (3, 1)$ $b = (2, 4, 5, 6)$ step 5 $a = (1)$ $b = (2, 4, 5, 6, 3)$ step 6 $a = ()$ $b = (2, 4, 5, 6, 3, 1)$ Ojilă gives you the permutation $b$ and you need to reconstruct the initial permutation $a$. 

## Input data

The input file `permuta.in` contains the number $n$ on the first line. The next line contains $n$ natural numbers separated by a space, representing the final permutation $b$. 

## Output data

The output file `permuta.out` will contain a single line that will contain the initial permutation $a$, with the numbers in the permutation separated by a space. 

## Constraints and clarifications

$3 \leq N \leq 100 \ 000$ 

## Example

`permuta.in`
```
6
2 4 5 6 3 1
```

`permuta.out`
```
2 6 4 1 5 3
```

