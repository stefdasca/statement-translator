## Task

Let $S$ be a set of pairs $(a,b)$ of natural numbers. $S = \{(a_{1} ,b_{1}), (a_{2} ,b_{2}), (a_{3} ,b_{3}), \dots \}$ We say that a pair $(x,y)$ is $S$-compatible if it can be written as a linear combination of the pairs in $S$ with coefficients from $[0, 1]$. More precisely, the pair $(x,y)$ is $S$-compatible if there exist real coefficients $c_{1} , c_{2} , \dots , c_{N}$ belonging to the interval $[0, 1]$ such that 
$$x = c_{1} * a_{1} + c_{2} * a_{2} + c_{3} * a_{3} + \dots + c_{N} * a_{N}$$ 
$$y = c_{1} * b_{1} + c_{2} * b_{2} + c_{3} * b_{3} + \dots + c_{N} * b_{N}$$
where $(a_{1} ,b_{1}) , (a_{2} ,b_{2}) , (a_{3} ,b_{3}) , \dots , (a_{N} ,b_{N})$ are the pairs in $S$. Starting from an initially empty set $S$, you must support the following operations: 
- Insert $(a,b)$ - insert the pair $(a,b)$ into $S$ 
- Erase $(a,b)$ - remove the pair $(a,b)$ from $S$ 
- Query $(x,y)$ - check if the pair $(x,y)$ is $S$-compatible 

## Input data

The input file `combl.in` will contain on the first line a single natural number $Q$ representing the number of operations to be executed. The following $Q$ lines will each describe an operation as follows:
- If the first number on the line is $1$, the operation described is an Insert operation. After the number $1$, there will follow $2$ natural numbers $a$ and $b$ representing the pair to be added to the set $S$. 
- If the first number on the line is $2$, the operation described is an Erase operation. After the number $2$, there will follow $2$ natural numbers $a$ and $b$ representing the pair to be removed from the set $S$. 
- If the first number on the line is $3$, the operation described is a Query operation. After the number $3$, there will follow $2$ natural numbers $x$ and $y$ representing the pair for which it is checked if it is $S$-compatible or not.

## Output data

The output file `combl.out` must contain as many lines as the number of Query operations in the input file `combl.in`. Thus, on line $a_{i}$ of the output file, it must contain the word "DA" (without quotes) if the pair $(x,y)$ from the $a_{i}$-th Query operation was $S$-compatible with the set $S$ at that moment or "NU" (without quotes) otherwise.

## Constraints and clarifications

$1 \leq Q \leq 150\ 000$ 

$0 \leq number of Insert operations \leq 50\ 000$ 

$1 \leq a_{i} , b_{i} \leq 10\ 000$

$0 \leq x, y \leq 1\ 500\ 000 \ 000$

The pairs from the Insert operations are pairwise distinct 

Any Erase operation is valid, meaning no pair $(a,b)$ that is not in $S$ will be erased

Any Query operation is valid, meaning whenever such an operation appears, the set $S$ will be non-empty 

For tests worth $20$ points, there will only be $2$ Insert operations in the input file 

For tests worth another $40$ points, $Q \leq 3\ 000$

## Example

`combl.in` 
```
9
1 1 2
1 2 1
3 2 2
2 1 2
3 2 2
1 1 3
1 4 2
3 0 3
3 5 4
```

`combl.out` 
```
DA
NU
NU
DA
```

## Explanation

At the first Query operation, the set $S$ is formed by the pairs $(1,2)$ and $(2,1)$. 

We can obtain the pair $(2,2)$ as 
$$x = \frac{2}{3} * 1 + \frac{2}{3} * 2 = 2$$ 
$$y = \frac{2}{3} * 2 + \frac{2}{3} * 1 = 2$$

At the second Query operation, the set $S$ is formed only by the pair $(2,1)$. 

We cannot obtain $(2,2)$ in any way. 

At the third Query operation, the set $S$ is formed by the pairs $(2,1)$, $(1,3)$ and $(4,2)$. 

To obtain $x = 0$, all coefficients $c$ must be $0$, therefore $y$ should also be $0$, but we need $y = 3$.

At the fourth Query operation, the set $S$ is formed by the pairs $(2,1)$, $(1,3)$ and $(4,2)$. 

We can obtain the pair $(5,4)$ as 
$$x = 0.2 * 2 + 0.6 * 1 + 1 * 4 = 0.4 + 0.6 + 4 = 5$$ 
$$y = 0.2 * 1 + 0.6 * 3 + 1 * 2 = 0.2 + 1.8 + 2 = 4$$