## Task

Two interesting logical formulas in the same $n$ variables $a_1 , a_2 , \dots a_n$ are given. A logical formula is interesting if and only if it is a disjunction of elementary conjunctions. An elementary conjunction is a formula of the type $(b_1 \text{ AND } b_2 \text{ AND } \dots \text{ AND } b_n)$, where $b_i$ is $c_i$ or $\text{NOT } c_i$, the set $\{ c_1 , c_2 , \dots c_n \}$ is a permutation of the set $\{ a_1 , a_2 , \dots a_n \}$ and $\text{NOT } c_i$ is the negation of the variable $c_i$. An example of an interesting formula in 3 independent variables is $(a_1 \text{ AND NOT } a_3 \text{ AND } a_2) \text{ OR } (a_3 \text{ AND NOT } a_1 \text{ AND NOT } a_2)$. Given two elementary formulas in the variables $a_1 , a_2 , \dots a_n$, determine if they are equivalent (i.e., for any distribution of the variables $a_1 , a_2 , \dots a_n$, the formulas produce the same result).

## Input data

The file `amlei.in` contains $W$ tests. The first line of each test contains the natural numbers $n$, $t$, and $u$, where $t$ and $u$ represent the number of elementary conjunctions from which each of the two formulas is formed. The second line contains $n \cdot t$ non-zero integers between $-n$ and $n$, representing the variables in the first formula when ignoring the parentheses and considering that $i$ and $-i$ signify $a_i$, respectively $\text{NOT } a_i$. The third line describes in a similar way the second formula through $n \cdot u$ integers. For example, the formula $(a_1 \text{ AND NOT } a_3 \text{ AND } a_2) \text{ OR } (a_3 \text{ AND NOT } a_1 \text{ AND NOT } a_2)$ would be described by the sequence of numbers: `1 -3 2 3 -1 -2`. 

## Output data

For each of the $W$ tests, print on a separate line in the file `amlei.out` "DA" or "NU" (without quotes), depending on whether the two formulas are or are not equivalent. 

## Constraints and clarifications

$1 \leq W \leq 10$

$1 \leq n \leq 50$

$1 \leq t$

$u \leq 500$

## Example

`amlei.in`

```
3
3 4
1 -2 -3 3 1 2 2 -1 3
2 -1 3 -3 -1 2 3 -1
2 2
1 -3 3 3 4
-3 -2 -1
3 1 2 -2 3
-1 1 2 3
-3 -2 -1 -1 -3 -2 -1 -2 3
```

`amlei.out`

```
NU
DA
```