Certainly! Here is the translated competitive programming problem statement:

---

A list with a known number of words is considered. From this list, two arbitrary words are chosen. The goal is to transform the first word into the second by passing through intermediate words that exist in the given list. The transition from one word to another can be made using the following operations: changing, adding, or deleting a single character.

# Task

Given a list of words and two words from this list, find the shortest sequence of operations that transforms the first word into the second using the allowed operations.

# Input data

Input file: `cuvinte.in`

Line $1$: $N$, $P$, $Q$, three non-zero natural numbers, representing the number of words in the list ($N$), the position of the first word in the list ($P$), and the position of the second word in the list ($Q$);

Lines $2 \ldots N+1$: $word$, these $N$ lines each contain a word, belonging to the list.

# Output data

Output file: `cuvinte.out`

Line $1$: $M$, a natural number, representing the minimum number of steps needed to reach from the first word to the second;

Lines $2 \ldots M+1$: $word_i$, these lines contain in order the words from a sequence that meets the problem's requirement (one word per line), including the first word of the sequence.

# Constraints and clarifications

* $2 \leq N \leq 100$
* $1 \leq M, P, Q \leq 100$
* The maximum number of characters in a word is $100$
* If there is no solution, the digit $0$ (zero) will be written in the output file
* If there are multiple sequences of minimum length, only one will be written in the file
* The tests are not the same as those from the contest (they could not be found)

# Example 1

`cuvinte.in`
```
7 1 5
car
cer
cerc
mar
mare
rosu
inrosit
```

`cuvinte.out`
```
2
car
mar
mare
```

# Example 2

`cuvinte.in`
```
7 1 6
car
cer
cerc
mar
mare
rosu
inrosit
```

`cuvinte.out`
```
0
```

--- 

Please let me know if you need further assistance or if there's anything specific you would like me to review!