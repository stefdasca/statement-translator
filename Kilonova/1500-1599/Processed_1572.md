# Task
Skippie, the lucky bunny, loves digits and has established a way to obtain the control digit of a number: the sum of its digits is computed, then the sum of the digits of this sum, and so on until the obtained sum is a single-digit number. This last digit, Skippie says, is called the control digit.  
Skippie has hidden $n$ red eggs in the forest. On each egg, he painted a non-zero natural number. Now he wonders what the sum between the largest and the smallest natural number that can be formed from all distinct digits used in writing the painted number is.  
Additionally, because Skippie likes complicated problems, for each number painted on an egg, he wants to find out how many times the control digit of the painted number appears in the writing of all natural numbers less than or equal to the painted number.

# Task
Write a program that solves the following tasks:
1. For each of the $n$ numbers painted by Skippie, find the sum between the largest and smallest natural number that can be formed from all distinct digits used in writing the painted number.
2. For each of the $n$ numbers painted by Skippie, find out how many times the control digit of the painted number appears in the writing of all natural numbers less than or equal to the painted number.

# Input data
The input file `iepuras.in` contains a natural number $C$. This can have the values $1$ or $2$ and represents the task of the problem. The second line of the input file contains a natural number $n$ representing the number of red eggs painted by Skippie. Each of the next $n$ lines in the input file contains a non-zero natural number representing the painted numbers on the $n$ red eggs.

# Output data
The output file `iepuras.out` will contain $n$ integers, each on a separate line. In the order of appearance of the painted numbers in the input file, print the answers to task $C$.

# Constraints and clarifications

* $1 \leq C \leq 2$;
* $1 \leq n \leq 100000$;
* the numbers painted by the bunny are smaller than or equal to $10^{18}$

|#|Score|Constraints|
|-|-|-----------|
|1|16|$C = 1$, $n = 1$, painted numbers $ \leq 10^9$|
|2|24|$C = 1$, $1 < n \leq 10^5$, painted numbers $ \leq 10^9$|
|3|24|$C = 2$, $1 \leq n \leq 100$, painted numbers $ \leq 2000$|
|4|36|$C = 2$, $100 < n \leq 10^5$, painted numbers $ \leq 10^{18}$|

# Example 1

`iepuras.in`
```
1
2
121
33343
```

`iepuras.out`
```
33
77
```

## Explanation

Task $1$ is solved. There are $2$ painted eggs ($n = 2$). For the first egg, painted with the number $121$:
- the largest natural number with distinct digits formed with all distinct digits of the painted number is $21$;
- the smallest natural number with distinct digits formed with all distinct digits of the painted number is $12$.
Therefore, the sum of the two numbers is $33$ ($21 + 12 = 33$).

For the second egg painted with the number $33343$:
- the largest natural number with distinct digits formed with all distinct digits of the painted number is $43$;
- the smallest natural number with distinct digits formed with all distinct digits of the painted number is $34$.
Therefore, the sum of the two numbers is $77$ ($43 + 34 = 77$).

# Example 2


`iepuras.in`
```
2
2
123
191
```

`iepuras.out`
```
22
39
```

## Explanation

Task $2$ is solved. There are $2$ painted eggs ($n = 2$). On the first egg, the number $123$ is written and on the second egg, the number $191$ is written. 
The control digit of the number $123$ is $6$ ($1 + 2 + 3 = 6$). The number of occurrences of the digit $6$ in the writing of all natural numbers less than or equal to $123$ is $22$. 
The digit $6$ appears in the writing of the numbers: $6$, $16$, $26$, $36$, $46$, $56$, $60$, $61$, $62$, $63$, $64$, $65$, $66$, $67$, $68$, $69$, $76$, $86$, $96$, $106$, $116$ **22** times.
The control digit of the number $191$ is $2$ ($1 + 9 + 1 = 11$; $1 + 1 = 2$). The number of occurrences of the digit $2$ in the writing of all natural numbers less than or equal to $191$ is $39$. 
The digit $2$ appears in the writing of the numbers: $2$, $12$, $20$, $21$, $22$, $23$, $24$, $25$, $26$, $27$, $28$, $29$, $32$, $42$, $52$, $62$, $72$, $82$, $92$, $102$, $112$, $120$, $121$, $122$, $123$, $124$, $125$, $126$, $127$, $128$, $129$, $132$, $142$, $152$, $162$, $172$, $182$ **39** times.