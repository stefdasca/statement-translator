George received the following math homework problem. A number $X$ is given, on which the following transformations can be performed:

1) In this order (all these $3$ steps represent a transformation):
    - multiply the number by $5$ (e.g.: $X=416$ becomes $416 \cdot 5 = 2080$)
    - remove all zeros from the number ($2080$ becomes $28$)
    - reverse the number ($28$ becomes $82$)
2) In this order (all these $3$ steps represent a transformation):
    - multiply the number by $2$ (e.g.: $X = 32$ becomes $32 \cdot 2 = 64$)
    - remove all zeros from the number ($64$ remains $64$)
    - reverse the number ($64$ becomes $46$)

George has to alternatively apply these two transformations on the number $X$. First, he applies transformation $1$, then the result applies transformation $2$, then the result again applies transformation $1$, and then transformation $2$ again, and so on. George has to apply exactly $K$ transformations on the number $X$, in the order described above.

# Task

Given the numbers $X$ and $K$ determine:
1) The product of the last digit of the number $X \cdot X \cdot X \cdot \ldots \cdot X$ (repeated $K$ times) and the first digit of $X$.
2) The number obtained after applying the $K$ transformations.

# Input data

The first line of the input file `rotire25.in` contains three numbers separated by spaces $C, X$ and $K$. If $C=1$, only the first task will be solved, and if $C=2$, only the second task will be solved.

# Output data

The output file `rotire25.out` will contain a single number. If $C = 1$, this number represents the result for the first task, and if $C = 2$, this number represents the result for the second task.

# Constraints and clarifications

* $1 \leq X \leq 999$;
* $1 \leq K \leq 1\ 000\ 000\ 000$;
* For tests worth $29$ points, $C = 1$.
* For tests worth $71$ points, $C = 2$.
* For tests worth $7$ points, $C = 1$ and it is guaranteed that the number obtained after multiplications is $\leq {10}^{18}$ ($1\ 000\ 000\ 000\ 000\ 000\ 000$).
* For other tests worth $11$ points: $C = 1$ and $K \leq 100\ 000$.
* For tests worth $39$ points: $C = 2$ and $K \leq 100\ 000$.
* For other tests worth $9$ points: $C = 2$ and $X \leq 9$.

# Example 1

`rotire25.in`
```
1 27 3
```

`rotire25.out`
```
6
```

## Explanation

Solving the first task: $X = 27, K = 3$. $27 \cdot 27 \cdot 27 = 19\ 683 \implies$ the last digit is $3$. The first digit of $27$ is $2$, so the result is $2 \cdot 3 = 6$.

# Example 2

`rotire25.in`
```
2 13 3
```

`rotire25.out`
```
551
```

## Explanation

For the second example, solving the second task: $X = 13, K = 3$.
The transformations are as follows:
* $13 \cdot 5 = 65$, remove zeros and reverse $\implies 56$;
* $56 \cdot 2 = 112$, remove zeros and reverse $\implies 211$;
* $211 \cdot 5 = 1055$, remove zeros $\implies 155$; reverse $\implies 551$;

# Example 3

`rotire25.in`
```
2 42 1782321
```

`rotire25.out`
```
12
```

## Explanation

Solving the second task: $X = 42, K = 1782321$.
After performing the $K$ transformations, the number obtained is $12$.