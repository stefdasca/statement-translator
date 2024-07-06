# Task

To respond to the commission's questions.

# Input data

The first line of the input file `gand.in` contains the natural numbers $N$ and $Q$ separated by a space, representing the number of students participating in the two trials, respectively the number of actions (reporting a thought, rectifying a thought, question asked by the commission).
On the next $Q$ lines are, in the first place, the type of action, $1$ if Mr. Acob reports a thought, $2$ if Mr. Acob rectifies a previous thought, or $3$ if a question is asked by the commission. If the type of action is $1$ or $2$, then on the same line there will be $2$ more numbers, $A$ and $B$, the indices of the $2$ people to whom the thought refers, separated by spaces.

# Output data

In the output file `gand.out`, each line will contain the response to one question.
On line $i$ will contain the answer to the $i$-th question.

# Constraints and clarifications

* $1 \leq N, Q \leq 200 \ 000$;
* $1 \leq A, B \leq N, \ A \ne B$;
* The commission will ask at least one question;
* If a maximal group of interconnected students consists of a single student, then it is considered that Mr. Acob did not lie about that group;
* Students cannot have equally good days on both days;
* Mr. Acob cannot report a thought more than once, without being rectified in the past. For example, he can report a thought between students $1$ and $2$, then rectify it, and then report it again, but he cannot report it again if it is already reported and not rectified;
* Thoughts are bidirectional.

| # | Score | Constraints                                          |
|---|-------|-----------------------------------------------------|
| 1 | 20    | There will be only one question (action of type $3$); |
| 2 | 20    | $1 \leq N, Q \leq 1 \ 000$;                          |
| 3 | 40    | There will be no actions of type $2$;                |
| 4 | 20    | No additional constraints.                           |

# Example 1

`gand.in`
```
4 11
1 1 2
1 4 3
3
1 1 4
1 2 3
3
1 1 3
3
2 1 2
2 4 1
3
```

`gand.out`
```
0
0
1
0
```

## Explanation

Before the first question, the representation of the thoughts looks like in the drawing below, where we have $2$ maximal groups of students interconnected by thoughts, namely: $\\{1, 2\\}, \\{3, 4\\}$. Mr. Acob is not found guilty of lying, for no group (for now).
~[graf1.png]
Before the second question, the representation of the thoughts looks like in the drawing below, where we have a single maximal group of students interconnected by thoughts, namely: $\\{1, 2, 3, 4\\}$. Mr. Acob is not found guilty of lying this time either.
~[graf2.png]
Before the third question, the representation of the thoughts looks like in the drawing below, where we have a single maximal group of students interconnected by thoughts, namely: $\\{1, 2, 3, 4\\}$. This time, Mr. Acob is caught lying! Students $1$ and $3$ must have a different best day from the best day of student $2$ (because both students are connected by thoughts to student $2$), so their best day must be the same, but the two students are also connected to each other by thoughts $=>$ impossible.
~[graf3.png]
Before the fourth question, the representation of the thoughts looks like in the drawing below, where we have a single maximal group of students interconnected by thoughts, namely: $\\{1, 2, 3, 4\\}$. Mr. Acob can no longer be found guilty this time.
~[graf4.png]