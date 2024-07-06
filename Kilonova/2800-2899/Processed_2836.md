Following are the translations based on the given instructions:

---

Gimi has become very popular among his classmates due to the good results he has achieved. However, not in the way he wanted. Now, most of his classmates have started asking him various theoretical questions.

Gimi received a list of $N$ questions from his classmates, and he intends to answer them in order. The $i$-th question $q_i$ consists of a string of characters consisting only of lowercase English letters. However, he noticed that he can receive the same question, formulated differently – so, if the question $q_i$ resembles at least one question $q_j \\ (with $1 \\leq j < i)$ to which he has already answered, then he will not answer the question $q_i$.

Gimi has defined the following similarity criteria between the question $q_j$ and the question $q_i$:
* Equality $(E)$: If question $q_i$ is equal to question $q_j$, then $q_i$ and $q_j$ resemble according to the $E$ criterion.
* Insertion $(I)$: If by inserting a single character into $q_i$, it becomes equal to $q_j$, then $q_i$ and $q_j$ resemble according to the $I$ criterion.
* Deletion $(S)$: If by deleting a single character from $q_i$, it becomes equal to $q_j$, then $q_i$ and $q_j$ resemble according to the $S$ criterion.
* Modification $(M)$: If by modifying a single character in $q_i$, it becomes equal to $q_j$, then $q_i$ and $q_j$ resemble according to the $M$ criterion.

We denote by $T$ the set of similarity criteria he uses. For example, if $T = EI$, he will only use the $E$ and $I$ criteria to determine if questions resemble each other or not. If $T = EISM$, then he will use all $4$ criteria.

Gimi starts with the first question on the list and will answer it. After that, starting from the second question until the last, he proceeds as follows:
* If the question $q_i$ resembles at least one question $q_j$ based on at least one of the criteria from $T$, then he will **NOT** answer question $q_i$.
* Otherwise, he will answer question $q_i$.

Being a very large set of questions, Gimi wants to determine: for a set of criteria $T$, which questions will he answer (and which not).

# Task

Write a program that, given $N$, the number of questions, $T$, the similarity criteria used, and the $N$ questions $q_1, q_2, \ldots, q_N$, displays for each of these questions if it will be answered or not.

# Input data

The input file `gimigpt.in` contains on the first line a natural number $N$, representing the number of questions, and a string $T$, which contains the similarity criteria, separated by a space.
The next $N$ lines contain, in order, the $N$ questions, one question per line.

# Output data

The output file `gimigpt.out` will contain $N$ lines. Line $i$ will contain the value $1$ if the $i$-th question in the input file will be answered, otherwise, it will contain the value $0$.

# Constraints and clarifications

* $T \in \{E$, $EI$, $ES$, $EM$, $EIS$, $EIM$, $ESM$, $EISM \}$
* $1 \\leq N \\leq 80\ 000$
* $2 \\leq LEN(q_i) \\leq 26$, for any $1 \\leq i \\leq N$, where LEN represents the length of the string.
* The tests are grouped. Within each subtask, the associated test groups are specified.

|#|Score|Constraints|
|-|-|-|
|1|5+6+6+6 (gr. 1, 2, 3, 4)|$N = 800,T \in \{ E, EI, ES, EM \}$|
|2|3+3+3+3 (gr. 5, 6, 7, 8)|$N = 10\ 000,T \in \{ E, EI, ES, EM \}$|
|3|5 (gr. 9)|$N = 800,T = EISM$|
|4|7 (gr. 10)|$N = 4\ 000,T = EISM$|
|5|12 (gr. 11)|$N = 10\ 000,T = EISM$|
|6|12 (gr. 12)|$N = 30\ 000,T = EISM$|
|7|2+2+4 (gr. 13, 14, 15)|$N \in \{ 800, 10\ 000, 80\ 000 \}$, $T= EISM$, $2 \\leq len(q_i) \\leq 10$|
|8|2+2+4 (gr. 16, 17, 18)|$N \in \{ 800, 10\ 000, 80\ 000 \}$, $T = EISM$, $q_i$ contains only the letters $a$ and $b$|
|9|13 (gr. 19, 20)|$N = 80\ 000$, $T = EISM$|

# Example 1

`gimigpt.in`
```
5 EISM
abc
abb
abbx
abc
bbb
```

`gimigpt.out`
```
1
0
1
0
1
```

## Explanation

The first question $abc$ will be answered. The second question $abb$ resembles the question $abc$ based on the $M$ criterion (the last letter from $b$ is changed to $c$), so it will not be answered.
The third question $abbx$ will be answered. It can be seen that, if the question $abb$ had been answered, the current question would not be answered.
The fourth question $abc$ resembles the question $abc$ based on the $E$ criterion (the strings are equal), so it will not be answered.
The question $bbb$ will be answered.

# Example 2

`gimigpt.in`
```
4 EI
abc
abb
ac
abbx
```

`gimigpt.out`
```
1
1
0
1
```

## Explanation

The first question $abc$ will be answered.
The second question $abb$ will be answered.
It does not resemble the question $abc$ based on the $E$ and $I$ criteria.
The third question $ac$ will not be answered. It resembles the question $abc$ based on the $I$ criterion (by inserting the letter $b$).
The question $abbx$ will be answered. It resembles the question $abx$ based on the $S$ criterion (by deleting the letter $x$), which is not part of $T$. The $I$ criterion strictly involves inserting a letter into the current string $(abbx)$ and not inserting a letter into a question that has already been answered.

---

This completes the required translation and fixes potential grammar and syntax errors.