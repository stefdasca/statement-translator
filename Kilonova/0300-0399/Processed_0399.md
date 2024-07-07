
In the technology education class of the 5th grade, Professor Forus, who is passionate about mathematics, brought each of the $N$ students a card with a natural non-zero number written on it. Each student can use the card as received or cut the card exactly once between two digits and attach the left part to the end of the right part. The student is NOT allowed to make a cut in front of the digit $0$, so none of the obtained numbers CAN start with the digit $0$. Among all the numbers they can obtain, the student chooses the one with the minimum number of divisors, and if they can obtain multiple such numbers, they choose the smallest one among them. At the end of the class, the professor collects the cards with the chosen numbers, in the order they were distributed. For example, if initially the student receives the card with the number $\\boxed{\\color{red}{25082}}$ then they have only the following three cutting and pasting options:
$ 
\displaystyle
\begin{array}{cc}
\boxed{\color{red}{2}} & \boxed{\color{red}{5082}} & \rightarrow & \boxed{\color{red}{50822}} \\
\boxed{\color{red}{250}} & \boxed{\color{red}{82}} & \rightarrow & \boxed{\color{red}{82250}} \\
\boxed{\color{red}{2508}} & \boxed{\color{red}{2}} & \rightarrow & \boxed{\color{red}{22508}} 
\end{array}
$

# Task

Write a program that reads the natural number $N$ and the $N$ numbers written on the cards brought by Professor Forus, then solves the following two tasks:
1. Determine the number of cards that students are allowed to cut from anywhere (DO NOT contain digits in front of which they are NOT allowed to cut);
2. Determine, in the order of collecting the cards, the numbers taken by Professor Forus at the end of the class.

# Input data
The input file `forus.in` contains on the first line a natural number $C$ representing the task from the problem that needs to be solved ($1$ or $2$). The second line of the file contains a natural number $N$, representing the number of students, and the third line of the file contains $N$ natural numbers, separated by a space, representing the numbers written on the cards brought by the professor, in the order of their distribution.

# Output data
If $C = 1$, the output file `forus.out` contains the first line that contains a natural number representing the answer to task $1$.
If $C = 2$, the output file `forus.out` contains the first line $N$ natural numbers, separated by a space, representing the answer to task $2$; the numbers are written in the order in which they were collected.

# Constraints and clarifications

* $2 \leq N \leq 30$;
* $1 \leq \text{natural number on the card} < 1 \ 000 \ 000 \ 000$;
* For correctly solving task $1$ $25$ points are awarded; for correctly solving task $2$ $75$ points are awarded.

# Example 1

`forus.in`
```
1
5
1234 25082 543 52 150
```

`forus.out`
```
3
```

## Explanation

# Example 2

`forus.in`
```
2
5
51 1234 50822 345 150
```

`forus.out`
```
15 2341 25082 453 501
```

## Explanation

The task is $2$. For the card number $51$, the numbers $15$ and $51$ can be obtained. Both numbers have $4$ divisors. Thus, the number $15$ is chosen, being the smallest. For the card number $1234$ ($4$ divisors), the numbers can be obtained: $2341$ ($2$ divisors), $3412$ ($6$ divisors), and $4123$ ($8$ divisors). The number $2341$ will be chosen because it has the minimum number of divisors. The same procedure will be followed for all the other numbers in the sequence.
