## Task

Agent P., bored of interactive geometry and match algorithms in $O(N)$ with random knapsack, resigned from the Cool Acronym-less Organization and started composing Cool Acronym Problems. Doctor Heinz Doofenshmirtz was working on a new inator when he got hungry and thought of ordering some spicy chicken wings through FoodPlatypus. The chicken wings can be of 2 types: seasoned (coded by $1$) or unseasoned (coded by $0$). His order through FoodPlatypus has the following instructions: "I want to receive a string of wings, split into $N$ alternating segments. Thus, the first segment should contain $V_1$ unseasoned wings, the second segment should contain $V_2$ seasoned wings, the third segment should contain $V_3$ unseasoned wings $\dots$"

The company owner, the renowned chef Gordon Ramsay, now has a string of chicken wings in front of him, some seasoned, some not. He defines a maximal spicy subarray as a subarray of wings of the same type that cannot be extended to the left or right. In one step, he can change the type of a maximal spicy subarray if and only if it has next to it another maximal spicy subarray of length greater than or equal to it. Secretly passionate about algorithmic problems, he wonders what is the total number of initial configurations of wings he can have so that, applying the above operation as many times as he wants, he can obtain Dr. Doofenshmirtz's final order. However, being too busy preparing the order and insulting employees, he asks you what this number is, modulo $998244353$. 

## Input data

The input file `pwca.in` will contain on the first line the natural number $N$ representing the number of segments.

The next line will contain $N$ numbers $V_1$, $V_2$, $\dots$, $V_N$ representing Dr. Doofenshmirtz's wing order.

## Output data

The output file `pwca.out` will print the number of sought initial configurations, modulo $998244353$.

## Constraints and clarifications

Subtask $1$ $(10$ points$)$

Subtask $2$ $(20$ points$)$

Subtask $3$ $(30$ points$)$

Subtask $4$ $(40$ points$)$

No additional constraints.

## Example

`pwca.in`

```
3
5 3 2
```

`pwca.out`

```
15
```

`pwca.in`

```
4
1 15 30 626
```

`pwca.out`

```
30626
```

## Explanation

### Example $1$

The configuration in the example is the bit string $000$.

This can be obtained from the following configurations:
- $000$
- $100 \rightarrow 000$
- $010 \rightarrow 000$
- $001 \rightarrow 000$
- $101 \rightarrow 100 \rightarrow 000$

### Example $2$

The configuration in the example is the bit string $001110$.

This can be obtained from the following configurations:
- $001110$
- $101110 \rightarrow 001110$
- $001010 \rightarrow 001110$
- $101010 \rightarrow 001010 \rightarrow 001110$