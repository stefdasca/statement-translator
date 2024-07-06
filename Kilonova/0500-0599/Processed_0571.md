Our main character, Auraș, received an interesting assignment in computer science: he received ${N}$ functions ${f_i : \mathbb{Z} \rightarrow \mathbb{Z}}$, where each function contains the first ${K}$ variables from the set $\{a, b, c, d, e, x, y, z, t, u, v, k, m, n\}$, in order (which can have integer coefficients attached to them), together with integer constants, addition, subtraction, multiplication operators, and round brackets. After these ${N}$ functions are given, he has to evaluate an expression formed from these functions, together with integer constants, addition, subtraction, multiplication operators, and round brackets. Unfortunately, Auraș is not proficient at this type of problem and asks for your help to solve it, in exchange for ${100}$ points.

# Task
Solve Auraș's assignment to receive the $100$ points.

# Input data
The first line of the input file will contain the number ${N}$, followed by the next ${N}$ lines containing the functions ${f_i : \mathbb{Z} \rightarrow \mathbb{Z}}$. The last line of the input file will contain the expression to be evaluated.

# Output data
The output file will contain the result of the evaluated expression $ \%\ {773}$.

# Constraints and clarifications
- $1 \leq N \leq 100$
- $1 \leq K \leq 14$
- $1 \leq L(f_i) \leq 700$
- $1 \leq L(E) \leq 700$
- $L(f_i)$ = length of the functions ${f_i}$
- $L(E)$ = length of the expression to be evaluated
- The coefficients and constants, as well as the arguments of the functions found in the input data belong to the interval $[0, 10^3]$ and are integers
- The functions ${f_i}$ are given in order ${f_1}$, ${f_2}$, ${f_3}$ ..., ${f_N}$
- The addition, subtraction, and multiplication operators are, in order, the following: $+$, $-$, $*$
- It is guaranteed that the expression to be evaluated is correct

# Scoring
| # | Points | Constraints          |
| - | ------- | ------------------- |
| 1 | 15      | $1 \leq L(f_i) \leq 150$, $1 \leq L(E) \leq 150$ and $1 \leq K \leq 4$ |
| 2 | 85      | No additional constraints.      |

# Example
`functii.in`
```text
2
f1(a,b)=2a+5b+1
f2(a,b,c)=5b-c*1
(1*f1(3,4)-f2(1,1,1))*f2(0,0,7)+7
```

`functii.out`
```text
619
```

# Explanation
${f_1}(3,4) = 27$  
${f_2}(1,1,1) = 4$  
${f_2}(0,0,7) = -7$  
The evaluated expression will be $(27 - 4) \cdot (-7) + 7 = -154$, and $-154\\ \%\ 773 = 619$.