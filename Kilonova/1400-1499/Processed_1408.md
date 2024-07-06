Here is the translated text in English, with the format and custom syntax preserved:

```markdown
At ONIGIM 2013, $N$ fifth-grade students are participating, having as IDs, in order, the natural numbers from $1$ to $N$. This year, the organizers displayed all the distinct scores obtained by the fifth-grade students, in strictly increasing order $p_1$, $p_2$, $\dots$, $p_K$, and an array of $N$ values $a_1$, $a_2$, $\dots$, $a_N$, where $a_i$ represents the number of students who have scores strictly less than the score of the student with ID $i$ ($1 \leq i \leq N$).

# Task

Given the number of students ($N$), the number of distinct scores ($K$) obtained by the fifth-grade students, the scores $p_1$, $p_2$, $\dots$, $p_K$ in strictly increasing order, and the values $a_1$, $a_2$, $\dots$, $a_N$ as described, write a program that determines:

1. The score obtained by each student in the increasing order of IDs.
2. The number of awards given by the organizers. The number of awards is equal to the number of students who obtained the top three distinct scores.
3. The maximum number of students who obtained the same score.

# Input data

The input file `onigim.in` contains on the first line the natural numbers $N$ and $K$, representing the number of students and the number of distinct scores obtained by the students, respectively. The second line contains $K$ natural numbers in strictly increasing order $p_1$, $p_2$, $\dots$, $p_K$ representing the distinct scores obtained by the students, and the third line contains $N$ natural numbers $a_1$, $a_2$, $\dots$, $a_N$, where $a_i$ represents the number of students who have scores strictly less than the score of the student with ID $i$.

# Output data

The output file `onigim.out` will contain three lines. The first line contains $N$ natural numbers $v_1$, $v_2$, $\dots$, $v_N$ representing the scores obtained by the $N$ competitors ($v_i$ - the score of the competitor with ID $i$). The second line contains a natural number $D$ representing the number of awards given by the organizers. The third line contains a natural number $M$ representing the maximum number of students who obtained the same score.

# Constraints and clarifications

* $1 \leq N \leq 1\ 000$;
* $1 \leq p_i \leq 300$, ($1 \leq i \leq N$);
* $0 \leq a_i \lt 1\ 000$, ($1 \leq i \leq N$);
* $1 \leq K \leq 1\ 000$;
* For the first task solved correctly, $40\%$ of the points are awarded; for the second task solved correctly, $30\%$ of the points are awarded; for the third task solved correctly, $30\%$ of the points are awarded;
* The answers to the three tasks will be written exactly on the indicated line; in case you do not know the solution to one of the tasks, the value $-1$ will be written on the respective line;
* Each line in the input file ends with a newline character.

# Example

`onigim.in`
```
6 4
100 150 175 200
4 2 0 0 3 4
```

`onigim.out`
```
200 150 100 100 175 200
4
2
```

# Explanation

There are $4$ students who have a score lower than the score of the student with ID $1$, $2$ students with a score lower than the score of the student with ID $2$, etc.
The top $3$ scores are obtained by $4$ students.
The maximum number of students who have the same score is $2$.
```

I have double-checked the text for any grammar or syntax errors and ensured it aligns with the rules of the English language.